import asyncio, json
import websockets

class VESSL_WS:
    vessl_url = "ws://localhost:8000/api"
    ws = None

    # Async functions, could be run asynchronously, but for this example it will be synchronous
    async def __connect(self):
        self.ws = await websockets.connect(self.vessl_url)

    async def __send_some_data(self, data):
        await self.ws.send(json.dumps(some_data))
        resp = await self.ws.recv()
        return resp

    # Run the async functions synchronously, i.e. wait for async process to finish, lets us communicate from code that is not "async def" (almost all code)
    def connect(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(asyncio.gather(*[self.__connect()])) # Block until connection is established and login is completed
        return result[0]

    def send_some_data(self, data):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(asyncio.gather(*[self.__send_some_data(data)])) # Block until connection is established and login is completed
        return result[0]


some_data = {
    'something': 0,
    'test_change': 'a string here'
}

v = VESSL_WS()
v.connect() # Connect to server
print('Connection up')
response = v.send_some_data(some_data) # Send example data to the server, have it modified by it, and get a response back
print(response)