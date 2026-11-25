"""WebSocket-чат на FastAPI."""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


app = FastAPI(
    title="WebSocket Chat",
    description="Многопользовательский чат",
    version="1.0.0",
)


class ConnectionManager:
    """Управляет подключениями пользователей к чату."""

    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        """Подключает нового пользователя."""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        """Отключает пользователя."""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str) -> None:
        """Отправляет сообщение всем подключенным пользователям."""
        for connection in self.active_connections.copy():
            await connection.send_text(message)


manager = ConnectionManager()


@app.get("/", response_class=HTMLResponse)
async def chat_page() -> str:
    """Возвращает HTML-интерфейс чата."""
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WebSocket Chat</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 700px;
                margin: 40px auto;
                padding: 20px;
                background: #f2f4f8;
            }

            .chat {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 2px 10px #0001;
            }

            #messages {
                min-height: 200px;
                padding: 15px;
                background: #f8f9fa;
                border-radius: 8px;
                list-style: none;
            }

            #messages li {
                padding: 8px;
                margin-bottom: 5px;
                background: #e3edff;
                border-radius: 5px;
            }

            form {
                display: flex;
                gap: 10px;
            }

            input {
                flex: 1;
                padding: 12px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }

            button {
                padding: 12px 20px;
                background: #0d6efd;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }

            #status {
                color: #198754;
                margin-bottom: 15px;
            }
        </style>
    </head>
    <body>
        <div class="chat">
            <h1>Общий чат</h1>

            <p id="status">Подключение...</p>

            <ul id="messages"></ul>

            <form id="message-form">
                <input
                    id="message-input"
                    type="text"
                    placeholder="Введите сообщение..."
                    maxlength="500"
                    required
                >
                <button type="submit">Отправить</button>
            </form>
        </div>

        <script>
            const protocol =
                location.protocol === "https:" ? "wss" : "ws";

            const socket = new WebSocket(
                `${protocol}://${location.host}/ws`
            );

            const status = document.getElementById("status");
            const messages = document.getElementById("messages");
            const form = document.getElementById("message-form");
            const input = document.getElementById("message-input");

            socket.addEventListener("open", () => {
                status.textContent = "Соединение установлено";
            });

            socket.addEventListener("close", () => {
                status.textContent = "Соединение закрыто";
            });

            socket.addEventListener("error", () => {
                status.textContent = "Ошибка соединения";
            });

            socket.addEventListener("message", (event) => {
                const item = document.createElement("li");
                item.textContent = event.data;
                messages.appendChild(item);
            });

            form.addEventListener("submit", (event) => {
                event.preventDefault();

                const message = input.value.trim();

                if (message && socket.readyState === WebSocket.OPEN) {
                    socket.send(message);
                    input.value = "";
                }
            });
        </script>
    </body>
    </html>
    """


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    """Обрабатывает WebSocket-подключение пользователя."""
    await manager.connect(websocket)

    try:
        while True:
            message = await websocket.receive_text()
            message = message.strip()

            if message:
                await manager.broadcast(message)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
