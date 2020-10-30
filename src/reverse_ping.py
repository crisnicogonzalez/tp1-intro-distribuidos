from constants import MSG_SIZE, PING, TIMEOUT
from payload_builder import build_reverse_msg, build_pong_msg, decode_ping_message, decode_rtt_message
from socket_client import print_info_message, print_packet_loss_message, send_msg, recv_msg
import time


def wait_ping_msg(socket, seq, verbose):
    if verbose:
        print("Wait ping message")
    received_ping_msg = False
    while not received_ping_msg:
        msg = recv_msg(socket)
        received_ping_msg = msg.startswith(PING) and decode_ping_message(msg)[1] == seq
    if verbose:
        print("Ping message received")


def send_pong_msg(socket, seq, verbose):
    if verbose:
        print("Sending pong message")
    send_msg(socket, build_pong_msg(seq))


def get_rtt_measure(socket, seq):
    rtt = decode_rtt_message(recv_msg(socket))
    if rtt[1] == seq:
        return rtt[2]
    else:
        raise Exception


def reverse_ping(socket, counts, quiet, verbose):
    measures = []
    msg = build_reverse_msg(counts)
    try:
        send_msg(socket, msg)

    except Exception:
        print("Error: connection with server lost")
        return measures
    socket.settimeout(None)

    for seq in range(1, counts + 1):
        try:
            wait_ping_msg(socket, seq, verbose)
            send_pong_msg(socket, seq, verbose)
            measure = float(get_rtt_measure(socket, seq))
            measures.append(measure)
            print_info_message(seq, measure, quiet)

        except Exception as e:
            print(e)
            print_packet_loss_message(seq, quiet)
            time.sleep(1)

    socket.settimeout(TIMEOUT)

    return measures
