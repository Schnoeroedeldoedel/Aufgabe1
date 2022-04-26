""" Websocket client

    source: https://codingpointer.com/python-tutorial/python-websockets
"""

import asyncio
import time

import websockets
import threading

current_output = ""
current_args = [""]
test = asyncio.Event()
send_event = threading.Event()
new_cycle = threading.Event()
write_lock = threading.Lock()
send_flag = False
new_command = False


def put_values(args):
    global current_args, send_flag, new_command
    send_event.clear()

    new_cycle.wait()  # set new args while socket is stuck in loop, to ensure new args are used
    current_args = args  # release socket from spin
    new_cycle.clear()
    test.set()
    send_event.wait()  # wait till ne output is set
    print("thread fertig")


def check_login(user, password):
    recv_output(["check-user", user, password])
    return current_output == "True"


def get_schema():
    recv_output(["get-schema"])
    return current_output


def get_all_courses():
    recv_output(["all-courses"])
    return current_output


def get_course_info(guid):
    recv_output(["get-course", guid])
    return current_output


def get_booked_courses(username):
    recv_output(["get-booked-courses", username])
    return current_output


def recv_output(args):
    thread = threading.Thread(target=put_values, args=[args])
    thread.start()
    thread.join()


# Coroutine that takes in a future
async def communicate():
    global current_args, send_flag, new_command
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            test.clear()
            new_cycle.set()
            await test.wait()

            command = current_args[0]
            if command == "q": break
            # send args
            for arg in current_args:
                await websocket.send(arg)

            resp = await websocket.recv()

            if resp != "placeholder":
                await update(resp)


async def update(resp):
    global current_output, send_flag
    current_output = resp
    send_event.set()
    print("fertig")
