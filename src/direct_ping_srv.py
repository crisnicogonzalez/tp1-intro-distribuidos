from payload_builder import build_ping_msg, build_pong_msg, decode_ping_message
from constants import STOP, MSG_SIZE
import socket
import time

def direct_ping_srv(conn, verbose, seq):

    ping = build_ping_msg(seq)
    if verbose:
        print("Direct ping request recieved")

    while not ping.startswith(STOP):
        try:
            # send  "pong" message
            conn.send(build_pong_msg(seq).encode())

            # recieve "ping" message
            ping = conn.recv(MSG_SIZE).decode()

            seq = int(decode_ping_message(ping)[1])

        except Exception as e:
            if e == socket.timeout:
                continue

            else:
                break

    if verbose:
        print("direct ping finished")