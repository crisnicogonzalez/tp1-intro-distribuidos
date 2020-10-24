from constants import CHUNK_SIZE, REVERSE, PING, PONG


PROTOCOL_FORMAT = "{}-{}"


def send_msg(socket, msg):
    socket.send(msg.encode())


def get_msg(socket):
    return socket.recv(CHUNK_SIZE).decode()


def build_msg(count):
    return PROTOCOL_FORMAT.format(REVERSE, count)


def wait_ping_msg(socket):
    print("wait ping msg")
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        print("msg -> {}".format(msg))
        received_ping_msg = msg == PING
        print("received_ping_msg", received_ping_msg)


def send_pong_msg(socket):
    print("send pong msg")
    send_msg(socket, PONG)


def get_rtt_measure(socket):
    print("get rtt measure")
    return get_msg(socket)


def reverse_ping(socket, counts):
    print("reverse ping")
    measures = []
    msg = build_msg(counts)
    send_msg(socket, msg)
    for count in range(counts):
        wait_ping_msg(socket)
        send_pong_msg(socket)
        measure = get_rtt_measure(socket)
        measures.append(measure)
    return measures
