from fastapi import FastAPI, Depends
from message_queue import MessageQueue

app = FastAPI()
queue = MessageQueue()  # Shared message queue instance

@app.get("/")
def read_root():
    return {"message": "Service A is running"}

@app.post("/publish/{topic}")
async def publish_message(topic: str, message: str):
    await queue.publish(topic, message)
    return {"message": "Message published", "topic": topic}
