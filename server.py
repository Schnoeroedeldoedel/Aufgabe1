""" Websocket server

    source: https://codingpointer.com/python-tutorial/python-websockets
"""

import asyncio
import websockets
import CourseXMLParser


# Coroutine that takes in a future
async def chat(websocket, path):
    while (True):
        msg = await websocket.recv()
        print(f"From Client: {msg}")
        if msg == "q": break
        if msg == "1":
            msg = CourseXMLParser.parse_schema()
        if msg == "2":
            msg = str(CourseXMLParser.parse_courses())
        if msg == "3":
            pass
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
