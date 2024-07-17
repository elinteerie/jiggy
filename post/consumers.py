import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging
logger = logging.getLogger(__name__)


class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "posts",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "posts",
            self.channel_name
        )

    async def receive(self, text_data):
        pass  # We won't handle incoming messages for now

    async def post_created(self, event):
        post_data = event['post']
        #logger.info(f"New post created: {post_data}")

        await self.send(text_data=json.dumps({
            'type': 'post_created',
            'post': event['post']
        }))
