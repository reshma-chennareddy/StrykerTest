
import asyncio
from typing import Callable, Optional, Dict, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class MessageQueue:
    def __init__(self):
        self.queues: Dict[str, asyncio.Queue] = {}  # Queues for topics
        self.subscribers: Dict[str, List[Callable]] = {}  # Subscribers for topics
        self.failed_messages: Dict[str, List[str]] = {}  # For retrying failed messages

    async def publish(self, topic: str, message: str):
        """Publish a message to a topic."""
        if topic not in self.queues:
            self.queues[topic] = asyncio.Queue()
        await self.queues[topic].put(message)
        await self._notify_subscribers(topic, message)

    def subscribe(self, topic: str, callback: Callable, filter_fn: Optional[Callable] = None):
        """Subscribe to a topic."""
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        self.subscribers[topic].append((callback, filter_fn))

    async def _notify_subscribers(self, topic: str, message: str):
        """Notify all subscribers of a topic."""
        if topic in self.subscribers:
            for callback, filter_fn in self.subscribers[topic]:
                if filter_fn and not filter_fn(message):
                    continue
                try:
                    await callback(message)
                except Exception as e:
                    logging.error(f"Error notifying subscriber: {e}")
                    self.failed_messages.setdefault(topic, []).append(message)

    async def retry_failed_messages(self):
        """Retry all failed messages."""
        for topic, messages in self.failed_messages.items():
            for message in messages:
                await self.publish(topic, message)
            self.failed_messages[topic] = []

    async def cleanup(self):
        """Cleanup all queues and subscribers."""
        self.queues.clear()
        self.subscribers.clear()
        self.failed_messages.clear()
