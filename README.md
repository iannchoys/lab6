# Лабораторная работа №6

**ФИО:** Егорова Анна Антоновна

**Группа:** 220042-11

**Вариант:** 5

**Дисциплина:** Методы и технологии программирования

## Тема

Веб-программирование на Python. Flask, FastAPI, REST API, WebSocket и Pydantic.

## Выполненные задания

### Задания средней сложности

- №1 — Flask-приложение Hello World.
- №5 — веб-страница с использованием Bootstrap.
- №7 — FastAPI endpoint, возвращающий JSON.

### Задания повышенной сложности

- №6 — многопользовательский чат с использованием WebSocket и FastAPI.
- №8 — использование Pydantic-схем для проверки и обработки данных.

## Структура проекта

- `task_medium_1.py` — Flask Hello World.
- `task_medium_5.py` — Flask-приложение с Bootstrap.
- `task_medium_7.py` — FastAPI JSON endpoint.
- `task_hard_6.py` — WebSocket-чат.
- `task_hard_8.py` — API с Pydantic-схемами.
- `templates/` — HTML-шаблоны.
- `tests/` — автоматические тесты.

## Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

## Запуск приложений

Flask Hello World:

```bash
python task_medium_1.py
```

Bootstrap:

```bash
python task_medium_5.py
```

FastAPI JSON:

```bash
python -m uvicorn task_medium_7:app --reload --port 8000
```

WebSocket-чат:

```bash
python -m uvicorn task_hard_6:app --reload --port 8001
```

Pydantic API:

```bash
python -m uvicorn task_hard_8:app --reload --port 8002
```

## Проверка проекта

Компиляция:

```bash
python -m py_compile task_medium_1.py task_medium_5.py task_medium_7.py task_hard_6.py task_hard_8.py
```

Проверка PEP 8:

```bash
python -m flake8 . --exclude=.git,__pycache__,.venv,venv
```

Автоматические тесты:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## Примечание

Для WebSocket-чата используется браузерный интерфейс. Данные студентов в Pydantic-приложении хранятся в оперативной памяти и сбрасываются после перезапуска сервера.