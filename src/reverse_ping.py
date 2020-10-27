from constants import MSG_SIZE, REVERSE, PING, PONG
from payload_builder import build_reverse_msg, build_pong_msg


def send_msg(socket, msg):
    socket.send(msg.encode())


def get_msg(socket):
    return socket.recv(MSG_SIZE).decode()


def wait_ping_msg(socket):
    print("wait ping msg")
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        print("msg -> {}".format(msg))
        received_ping_msg = msg.startswith(PING)
        print("received_ping_msg", received_ping_msg)


def send_pong_msg(socket):
    print("send pong msg")
    send_msg(socket, build_pong_msg())


def get_rtt_measure(socket):
    print("get rtt measure")
    return get_msg(socket)


def reverse_ping(socket, counts):
    print("reverse ping")
    measures = []
    msg = build_reverse_msg(counts)
    send_msg(socket, msg)
    for count in range(counts):
        try:
            wait_ping_msg(socket)
            send_pong_msg(socket)
            measure = get_rtt_measure(socket)
            print("measure -> {}".format(measure))
            measures.append(float(measure))
        except Exception as e:
            print("exception handled", e)

    return measures
