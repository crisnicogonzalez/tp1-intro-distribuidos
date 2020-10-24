from constants import CHUNK_SIZE

PROTOCOL_FORMAT = "{}-{}"
PROTOCOL_MSG = "reverse"
ping = "ping"
pong = "pong"


def send_msg(socket, msg):
    socket.send(msg.encode())


def get_msg(socket):
    return socket.recv(CHUNK_SIZE).decode()


def build_msg(count):
    return PROTOCOL_FORMAT.format(PROTOCOL_MSG, count)


def wait_ping_msg(socket):
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        received_ping_msg = msg is ping


def send_pong_msg(socket):
    send_msg(socket, pong)


def get_rtt_measure(socket):
    return int(get_msg(socket))


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
