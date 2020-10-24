from constants import CHUNK_SIZE, PING, REVERSE, PONG
from datetime import datetime


def send_msg(socket, msg):
    socket.send(msg.encode())


def send_ping_msg(socket):
    print("send ping message")
    send_msg(socket, PING)


def get_msg(socket):
    return socket.recv(CHUNK_SIZE).decode()


def get_msg(socket, bytes_to_read):
    return socket.recv(bytes_to_read).decode()


def wait_pong_msg(socket):
    print("wait pong message")
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        received_ping_msg = msg == PONG


## send ping message and wait pong message
## return the rtt time in ms

def send_ping(socket):
    start = datetime.now()
    send_ping_msg(socket)
    wait_pong_msg(socket)
    end = datetime.now()
    diff = end - start
    return int(diff.microseconds / 1000)
