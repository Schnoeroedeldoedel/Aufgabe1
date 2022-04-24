""" Websocket server

    source: https://codingpointer.com/python-tutorial/python-websockets
"""

import asyncio
import websockets

# Coroutine that takes in a future
import CourseXMLParser


async def chat(websocket, path):
    while(True):
        msg = await websocket.recv()

        if msg == "q": break
        if msg == "check-user":
            print("Check")
            username = await websocket.recv()
            password = await websocket.recv()
            msg = "True"
        if msg == "get-schema":
            print("Schema")
            msg = CourseXMLParser.parse_schema()
        await websocket.send(msg)


# websockets.serve() creates, starts, and returns a WebSocket server
# 'chat' is a WebSocket handler/callback routine
start_server = websockets.serve(chat, 'localhost', 8765)

# Simple event loop
# get_event_loop() is a low-level function to create an event loop instance
loop = asyncio.get_event_loop()

# run_until_complete() runs until the future (see argument) has completed
loop.run_until_complete(start_server)

# run_forever() runs the event loop indefinitely
# This causes the main thread to block indefinitely
# End the loop with stop() method or Ctrl-C
loop.run_forever()

