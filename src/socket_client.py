from constants import MSG_SIZE, PING, PONG
from payload_builder import build_ping_msg
import time
import socket

def create_socket(host, port):
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    sock.settimeout(3)
    return sock


def send_msg(socket, msg):
    socket.send(msg.encode())


def send_ping_msg(socket):
    send_msg(socket, build_ping_msg())


def recv_msg(socket):
    try:
        msg = socket.recv(MSG_SIZE).decode()
        return msg

    except Exception as e:
        print('Error: message lost')
        return ""



def wait_pong_msg(socket):
    received_ping_msg = False
    while not received_ping_msg:
        msg = recv_msg(socket)
        received_ping_msg = msg.startswith(PONG)


# send ping message and wait pong message
# return the rtt time in ms

def send_ping(socket):
    start = time.time()
    send_ping_msg(socket)
    wait_pong_msg(socket)
    end = time.time()
    diff = end - start
    return float(diff * 1000)
