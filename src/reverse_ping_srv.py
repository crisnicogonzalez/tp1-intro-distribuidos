from socket_client import send_ping, send_msg
import time

time_to_wait = 1


def reverse_ping_srv(socket_client, counts):
    print("reverse ping request received counts -> {}".format(counts))
    for counts in range(counts):
        time.sleep(time_to_wait)
        measure_in_ms = send_ping(socket_client)
        send_msg(socket_client, str(measure_in_ms))
    print("reverse ping finished")
