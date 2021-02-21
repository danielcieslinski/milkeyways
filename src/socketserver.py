# WS server example
import asyncio
import websockets
import json
import logging
from time import time

SEND_RESPONSE = False
DEBUG = True
import logging

def parse_chrome_data(data):
    out = None
    try:
        parsed = json.loads(data)
        out = {'time': time(),
               'data': parsed}

    except Exception as e:
        logging.log(logging.WARNING, "")
        print(e)

    return out

class Server:
    def init(self, host='localhost', port=3234):
        self._ws_receive = websockets.serve(self._receive, host, port)

    def run(self):
        asyncio.get_event_loop().run_until_complete(self._ws_receive)
        asyncio.get_event_loop().run_forever()

    async def _receive(self, websocket, path):
        data = await websocket.recv()
        parsed = parse_chrome_data(data)

        if DEBUG:
            print(parsed)

        if SEND_RESPONSE:
            ans = f"Received {data}!"
            await websocket.send(ans)
            if DEBUG:
                print(f"> Sent: {ans}")
                print('\n\n')


if __name__ == '__main__':
    ws = Server()
    ws.init()
    ws.run()