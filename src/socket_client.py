from constants import CHUNK_SIZE, PING, PONG
import time


def send_msg(socket, msg):
    socket.send(msg.encode())


def send_ping_msg(socket):
    send_msg(socket, PING)


def get_msg(socket):
    return socket.recv(CHUNK_SIZE).decode()


# def get_msg(socket, bytes_to_read):
#     return socket.recv(bytes_to_read).decode()


def wait_pong_msg(socket):
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        received_ping_msg = msg == PONG


# send ping message and wait pong message
# return the rtt time in ms

def send_ping(socket):
    start = time.time()
    send_ping_msg(socket)
    wait_pong_msg(socket)
    end = time.time()
    diff = end - start
    return float(diff * 1000)
