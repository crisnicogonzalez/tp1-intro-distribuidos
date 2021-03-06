from constants import MSG_SIZE, PONG, TIMEOUT
from payload_builder import build_ping_msg, decode_pong_message
import time
import socket


def create_socket(host, port):
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    try:
        sock.connect(server_address)

    except Exception:
        print("ping: server {} not found".format(host))
        exit(1)

    return sock


def print_info_message(seq, response, quiet):
    if not quiet:
        print("{} bytes from 127.0.0.1: seq={} time={:.3f} ms".format(str(MSG_SIZE), seq, response))


def print_packet_loss_message(seq, quiet):
    if not quiet:
        print("Error: packet lost, seq={}".format(seq))


def send_msg(socket, msg):
    socket.send(msg.encode())


def send_ping_msg(socket, seq, verbose):
    if verbose:
        print("Sending ping message")
    send_msg(socket, build_ping_msg(seq))


def recv_msg(socket):
    return socket.recv(MSG_SIZE).decode()


def wait_pong_msg(socket, seq, verbose):
    received_pong_msg = False
    while not received_pong_msg:
        msg = recv_msg(socket)
        if verbose:
            print("Received message")
        received_pong_msg = msg.startswith(PONG) and decode_pong_message(msg)[1] == seq


# send ping message and wait pong message
# return the rtt time in ms
def send_ping(socket, seq, verbose):
    start = time.time()
    send_ping_msg(socket, seq, verbose)
    wait_pong_msg(socket, seq, verbose)
    end = time.time()
    diff = end - start
    return float(diff * 1000)
