import pytest
import asyncio
from message_queue import MessageQueue

@pytest.fixture
def event_loop():
    """Create a fresh asyncio event loop for each test."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def message_queue():
    """Provide a fresh instance of MessageQueue for each test."""
    return MessageQueue()

@pytest.mark.asyncio
async def test_publish_and_subscribe(message_queue):
    received_messages = []

    async def mock_callback(message):
        received_messages.append(message)

    message_queue.subscribe("test_topic", mock_callback)
    await message_queue.publish("test_topic", "Hello, World!")
    await asyncio.sleep(0.1)  # Allow time for async callback to execute

    assert received_messages == ["Hello, World!"]

@pytest.mark.asyncio
async def test_message_filtering(message_queue):
    received_messages = []

    def filter_fn(message):
        return "important" in message

    async def mock_callback(message):
        received_messages.append(message)

    message_queue.subscribe("test_topic", mock_callback, filter_fn=filter_fn)
    await message_queue.publish("test_topic", "This is not important.")
    await message_queue.publish("test_topic", "This is important!")

    await asyncio.sleep(0.1)
    assert received_messages == ["This is important!"]

@pytest.mark.asyncio
async def test_retry_failed_messages(message_queue):
    received_messages = []

    async def mock_callback(message):
        if message == "Fail":
            raise Exception("Simulated failure")
        received_messages.append(message)

    message_queue.subscribe("test_topic", mock_callback)
    await message_queue.publish("test_topic", "Fail")
    await message_queue.retry_failed_messages()

    await asyncio.sleep(0.1)
    assert received_messages == ["Fail"]

@pytest.mark.asyncio
async def test_cleanup(message_queue):
    await message_queue.publish("test_topic", "Message before cleanup")
    await message_queue.cleanup()
    
    assert not message_queue.topics
    assert not message_queue.subscribers
    assert not message_queue.failed_messages
