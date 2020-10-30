from constants import MSG_SIZE, PING, TIMEOUT
from payload_builder import build_reverse_msg, build_pong_msg, decode_ping_message, decode_rtt_message
from socket_client import print_info_message, print_packet_loss_message
import time

def send_msg(socket, msg):
    socket.send(msg.encode())


def get_msg(socket):
    msg = socket.recv(MSG_SIZE).decode()
    return decode_rtt_message(msg)


def wait_ping_msg(socket, seq):
    received_ping_msg = False
    while not received_ping_msg:
        msg = get_msg(socket)
        received_ping_msg = ( msg.startswith(PING) and decode_ping_message(msg)[1] == seq )


def send_pong_msg(socket, seq):
    send_msg(socket, build_pong_msg(seq))


def get_rtt_measure(socket, seq):
    rtt = get_msg(socket)
    print(rtt)
    if rtt[1] == seq:
        return rtt[2]
    else:
        return rtt[1]

def reverse_ping(socket, counts, quiet):
    measures = []
    msg = build_reverse_msg(counts)
    try:
        send_msg(socket, msg)

    except:
        print("Error: connection with server lost")
        return measures
    socket.settimeout(None)

    for seq in range(1, counts + 1):
        try:
            wait_ping_msg(socket, seq)
            send_pong_msg(socket, seq)
            measure = float(get_rtt_measure(socket, seq))
            measures.append(measure)
            print_info_message(seq, measure, quiet)

        except Exception as e:
            print_packet_loss_message(seq, quiet)
            time.sleep(1)

    socket.settimeout(TIMEOUT)

    return measures
