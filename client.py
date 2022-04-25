""" Websocket client

    source: https://codingpointer.com/python-tutorial/python-websockets
"""

import asyncio
import time

import websockets
import threading

current_output = ""
current_args = [""]
send_event = threading.Event()
write_lock = threading.Lock()


def put_values(args):
    global current_args
    current_args = args
    send_event.wait()
    current_args = [""]


def check_login(user, password):
    put_values(["check-user", user, password])
    return current_output


def get_schema():
    put_values(["get-schema"])
    return current_output


# Coroutine that takes in a future
async def communicate():
    global current_args, current_output
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            args = current_args.copy()
            command = args[0]
            write = command != ""
            if command == "q": break
            # send args
            for arg in args:
                await websocket.send(arg)

            resp = await websocket.recv()
            if write:
                current_output = resp
                # lock, so value can be safely returned
                send_event.set()
