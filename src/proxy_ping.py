from payload_builder import build_proxy_msg, decode_rtt_message
from socket_client import recv_msg, print_info_message, print_packet_loss_message
import time
from constants import PONG


def proxy_ping(socket, counts, dest, quiet, verbose):

    dest_splitted = dest.split(":")
    ip_dest = dest_splitted[0]
    port_dest = dest_splitted[1]
    rtts = []

    proxy_message = build_proxy_msg(counts, ip_dest, port_dest)
    socket.send(proxy_message.encode())

    # Expect a pong response that indicate that the server could connect with destination server
    if verbose:
        print("Expecting pong response to confirm connection with destination server")

    pong = recv_msg(socket)

    if not pong.startswith(PONG):
        print("Error: destination server not found")
        socket.close()
        exit(1)

    if verbose:
        print("connection with destination server confirm")

    for seq in range(1, counts + 1):
        try:
            if verbose:
                print("recieving RTT message")
            msg = decode_rtt_message(recv_msg(socket))

            if msg[1] is not seq:
                print_packet_loss_message(seq, quiet)
                continue

            rtt_response = float(msg[2])
            rtts.append(rtt_response)
            print_info_message(seq, rtt_response, quiet)

        except Exception:
            print_packet_loss_message(seq, quiet)
            time.sleep(1)


    return rtts
