""" Websocket server

    source: https://codingpointer.com/python-tutorial/python-websockets
"""

import asyncio
import websockets

# Coroutine that takes in a future
import CourseXMLParser


async def chat(websocket, path):
    while (True):
        recv = await websocket.recv()
        msg = "placeholder"
        if recv == "q": break
        if recv == "all-courses":
            print("Alle Kurse")
            msg = CourseXMLParser.parse_all_courses()
        if recv == "check-user":
            print("Check")
            username = await websocket.recv()
            password = await websocket.recv()
            msg = "True"
        if recv == "get-schema":
            print("Schema")
            msg = CourseXMLParser.parse_schema()
        if recv == "get-course":
            guid = await websocket.recv()
            print(f"Frage Kurs {guid} ab")
            msg = CourseXMLParser.parse_course(guid)
        if recv == "book-course":
            print("Buchen")
            kurs = await websocket.recv()
        if recv == "get-booked-courses":
            username = await websocket.recv()
            print(f"Kurse für {username} finden")
            msg = CourseXMLParser.get_courses_for_user(username)
        if recv == "courses-for-user":
            print("Buchungen anzeigen")
            user = await websocket.recv()
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
