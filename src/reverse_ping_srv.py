from socket_client import send_ping, send_msg
import time
import socket
from constants import TIMEOUT
from payload_builder import build_rtt_response_msg

time_to_wait = 1


def reverse_ping_srv(socket_client, counts, verbose):
    if verbose:
        print("reverse proxy request received counts -> {}".format(counts))

    for seq in range(1, counts + 1):
        try:

            measure_in_ms = send_ping(socket_client, seq, verbose)
            if verbose:
                print("Sending rtt")
            print(measure_in_ms)
            response = build_rtt_response_msg(seq, str(measure_in_ms))
            send_msg(socket_client, response)
            time.sleep(time_to_wait)

        except socket.timeout:
            continue

    if verbose:
        print("reverse ping finished")