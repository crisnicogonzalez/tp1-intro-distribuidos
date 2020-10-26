from socket_client import send_ping, send_msg


def reverse_ping_srv(socket_client, counts):
    print("reverse proxy request received counts -> {}".format(counts))
    for counts in range(counts):
        measure_in_ms = send_ping(socket_client)
        send_msg(socket_client, str(measure_in_ms))
    print("reverse ping finished")
