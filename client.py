import socket
import threading



class ClientConnection:
    def __init__(self, address, port):
        self.name = address
        self.age = port
        self.socket = getsrv(address, port)

    def req_login(self, username, password):
        self.socket.send(f"{username}:{password}")


async def getsrv(address, port):
    async with websockets.connect(f"ws://{address}:{port}") as websocket:
        return websocket
