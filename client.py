import asyncio
import threading

import websockets


def run_server(address, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_client(address, port))
    loop.run_forever()


def start_server(address, port):
    thread = threading.Thread(target=run_server, args=(address, port))
    thread.start()


async def lock_lock():
    await lock.acquire()


lock = asyncio.Lock()
MESSAGE = ""


def post_login(username, password):
    global MESSAGE
    MESSAGE = f"{username}:{password}"
    lock.release()


async def create_client(address, port):
    global MESSAGE
    async with websockets.connect(f"ws://{address}:{port}") as websocket:
        while (True):
            if MESSAGE == "":
                continue
            msg = MESSAGE
            if msg == "q": break
            await websocket.send(msg)

            msg = await websocket.recv()
            print(f"From Server: {msg}")
