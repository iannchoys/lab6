"""Простейшее веб-приложение Hello World на Flask."""

from flask import Flask


# Создаём Flask-приложение.
app = Flask(__name__)


# Главная страница сайта.
@app.route("/")
def hello() -> str:
    """Возвращает приветственное сообщение."""
    return "Привет, Flask!"


# Запускаем сервер при непосредственном запуске файла.
if __name__ == "__main__":
    app.run(debug=True)
