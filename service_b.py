from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from message_queue.message_queue import MessageQueue

app = FastAPI()
queue = MessageQueue()  # Shared message queue instance

@app.get("/")
def read_root():
    return {"message": "Service B is running"}

@app.websocket("/ws/{topic}")
async def websocket_endpoint(websocket: WebSocket, topic: str):
    await websocket.accept()

    async def message_callback(message: str):
        await websocket.send_text(message)

    queue.subscribe(topic, message_callback)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        print(f"Client disconnected from topic: {topic}")
