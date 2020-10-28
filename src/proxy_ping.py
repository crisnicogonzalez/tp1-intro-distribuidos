from payload_builder import build_proxy_msg
from constants import MSG_SIZE, PONG
from socket_client import recv_msg


def proxy_ping(socket, counts, dest):

    dest_splitted = dest.split(":")
    ip_dest = dest_splitted[0]
    port_dest = dest_splitted[1]
    rtts = []

    proxy_message = build_proxy_msg(counts, ip_dest, port_dest)
    socket.send(proxy_message.encode())

    pong = recv_msg(socket)

    if not pong.startswith(PONG):
        print("Error: destination server not found")
        socket.close()
        exit(1)

    for seq in range(1, counts + 1):
        rtt_response = float(recv_msg(socket))
        print("{} bytes from 127.0.0.1: seq={} time={:.3f} ms".format(str(MSG_SIZE), seq, rtt_response))
        rtts.append(rtt_response)

    return rtts
