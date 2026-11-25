"""Автоматические тесты лабораторной работы №6."""

import unittest

from fastapi.testclient import TestClient

from task_hard_6 import app as chat_app
from task_hard_8 import app as student_app
from task_hard_8 import students


class WebSocketChatTests(unittest.TestCase):
    """Проверяет работу WebSocket-чата."""

    def test_chat_page_and_broadcast(self) -> None:
        with TestClient(chat_app) as client:
            page = client.get("/")

            self.assertEqual(page.status_code, 200)
            self.assertIn("WebSocket", page.text)

            with client.websocket_connect("/ws") as first:
                with client.websocket_connect("/ws") as second:
                    message = "Проверка WebSocket-чата"

                    first.send_text(message)

                    self.assertEqual(first.receive_text(), message)
                    self.assertEqual(second.receive_text(), message)


class PydanticSchemaTests(unittest.TestCase):
    """Проверяет валидацию Pydantic-схем."""

    def setUp(self) -> None:
        students.clear()

    def test_create_and_read_student(self) -> None:
        with TestClient(student_app) as client:
            payload = {
                "full_name": "Егорова Анна Антоновна",
                "group": "220042-11",
                "variant": 5,
            }

            response = client.post("/students", json=payload)

            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()["variant"], 5)
            self.assertEqual(response.json()["id"], 1)

            listing = client.get("/students")

            self.assertEqual(listing.status_code, 200)
            self.assertEqual(len(listing.json()), 1)

            detail = client.get("/students/1")

            self.assertEqual(detail.status_code, 200)
            self.assertEqual(detail.json()["full_name"], payload["full_name"])

    def test_invalid_variant_is_rejected(self) -> None:
        with TestClient(student_app) as client:
            payload = {
                "full_name": "Егорова Анна Антоновна",
                "group": "220042-11",
                "variant": 11,
            }

            response = client.post("/students", json=payload)

            self.assertEqual(response.status_code, 422)
            self.assertEqual(students, [])


if __name__ == "__main__":
    unittest.main()
