from constants import CHUNK_SIZE, PING, REVERSE, PONG
import time


def send_msg(socket, msg):
    print("send_msg -> {}".format(msg))
    socket.send(msg.encode())


def send_ping_msg(socket):
    print("send ping message")
    send_msg(socket, PING)


def get_msg(socket):
    return socket.recv(CHUNK_SIZE).decode()


def wait_pong_msg(socket):
    print("wait pong message")
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        received_ping_msg = msg == PONG


def reverse_ping_srv(socket_client, addr, counts):
    print("reverse proxy request received counts -> {}".format(counts))
    for counts in range(counts):
        start = time.time()
        send_ping_msg(socket_client)
        wait_pong_msg(socket_client)
        end = time.time()
        diff = str(end - start)
        send_msg(socket_client, diff)
    print("reverse ping finished")

