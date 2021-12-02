import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class VESSL_API_Consumer(AsyncJsonWebsocketConsumer):
    """
    Handles connections with any API clients
    """

    async def connect(self):
        await self.accept()
        print('Connected to client')

    async def disconnect(self, code):
        print('Disconnected from client')


    async def receive_json(self, content):
        content["test_change"] = "an entirely different string"
        content["stuff_added"] = 1243567
        print(content)
        await self.send_json(content)