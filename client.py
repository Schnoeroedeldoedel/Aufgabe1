import asyncio
import threading
import ast
import websockets
import json

def run_client(address, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_client(address, port))
    loop.run_forever()


def start_client(address, port):
    thread = threading.Thread(target=run_client, args=(address, port))
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

        await websocket.send("1")
        schema = await websocket.recv()
        await websocket.send("2")
        courses = await websocket.recv()
        courses = json.loads(courses)
        for course in courses:
            print(f"{course} {courses[course]['GUID']} {courses[course]['Name']}")
        while (True):
            msg = input("gib was ein:")
            if msg == "q": break
            await websocket.send(msg)

            msg = await websocket.recv()
            print(f"From Server: {msg}")


if __name__ == '__main__':
    run_client("localhost", 8765)
