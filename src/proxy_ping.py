from payload_builder import build_proxy_msg, decode_rtt_message
from socket_client import recv_msg, print_info_message, print_packet_loss_message
import time


def proxy_ping(socket, counts, dest, quiet):

    dest_splitted = dest.split(":")
    ip_dest = dest_splitted[0]
    port_dest = dest_splitted[1]
    rtts = []

    proxy_message = build_proxy_msg(counts, ip_dest, port_dest)
    socket.send(proxy_message.encode())

    # Expect a pong response that indicate that the server could connect with destination server
    try:
        pong = recv_msg(socket)

    except:
        print("Error: destination server not found")
        socket.close()
        exit(1)

    for seq in range(1, counts + 1):
        try:
            msg = decode_rtt_message(recv_msg(socket))

            if msg[1] is not seq:
                print_packet_loss_message(seq, quiet)
                continue

            rtt_response = float(msg[2])
            rtts.append(rtt_response)
            print_info_message(seq, rtt_response, quiet)

        except Exception as e:
            print_packet_loss_message(seq, quiet)
            time.sleep(1)


    return rtts
