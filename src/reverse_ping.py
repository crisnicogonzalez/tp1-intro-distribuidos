from constants import MSG_SIZE, PING
from payload_builder import build_reverse_msg, build_pong_msg


def send_msg(socket, msg):
    socket.send(msg.encode())


def get_msg(socket):
    return socket.recv(MSG_SIZE).decode()


def wait_ping_msg(socket):
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        received_ping_msg = msg.startswith(PING)


def send_pong_msg(socket):
    send_msg(socket, build_pong_msg())


def get_rtt_measure(socket):
    return get_msg(socket)


def reverse_ping(socket, counts):
    measures = []
    msg = build_reverse_msg(counts)
    send_msg(socket, msg)

    for seq in range(1, counts + 1):
        try:
            wait_ping_msg(socket)
            send_pong_msg(socket)
            measure = float(get_rtt_measure(socket))
            print("{} bytes from 127.0.0.1: seq={} time={:.3f} ms".format(str(MSG_SIZE), seq, measure))
            measures.append(measure)
        except Exception as e:
            print("exception handled", e)

    return measures
