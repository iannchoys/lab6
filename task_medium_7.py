"""FastAPI-приложение с JSON endpoint."""

from fastapi import FastAPI


# Создаём FastAPI-приложение.
app = FastAPI(
    title="Лабораторная работа №6",
    description="Демонстрация JSON endpoint",
    version="1.0.0",
)


# Главная конечная точка.
@app.get("/")
def root() -> dict[str, str]:
    """Возвращает приветствие в формате JSON."""
    return {
        "message": "Привет, FastAPI!",
        "lab": "№6",
        "variant": "5",
    }


# Дополнительная конечная точка с информацией.
@app.get("/api/info")
def get_info() -> dict[str, str]:
    """Возвращает информацию о приложении."""
    return {
        "application": "FastAPI",
        "discipline": "Методы и технологии программирования",
        "laboratory_work": "Лабораторная работа №6",
        "variant": "5",
        "status": "работает",
    }
