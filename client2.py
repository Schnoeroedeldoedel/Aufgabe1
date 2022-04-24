""" Websocket client

    source: https://codingpointer.com/python-tutorial/python-websockets
"""

import asyncio
import time

import websockets
import threading

current_output = ""
current_message = ""
current_args = []
output = False
arg_lock = asyncio.Lock()
server_lock = asyncio.Lock()
lock = threading.Lock()
cond = threading.Condition()


def put_values(message, args):
    global current_message, current_args, output
    current_message = message
    current_args = args
    while not output:
        continue
    output = False
    return current_output


def check_login(user, password):
    current_message = "check-user"
    current_args = [user, password]
    put_values(current_message, current_args)


def get_schema():
    current_message = "get-schema"
    put_values(current_message, [])


# Coroutine that takes in a future
async def communicate():
    global current_args, current_message, current_output, output
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            msg = current_message
            out = msg != ""
            if msg == "q": break
            # send server request
            await websocket.send(msg)
            for arg in current_args:
                await websocket.send(arg)
            current_args = []
            current_message = ""
            msg = await websocket.recv()
            if out:
                current_output = msg
                output = True
