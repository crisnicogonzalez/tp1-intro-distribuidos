import time
from socket_client import send_ping, print_info_message, print_packet_loss_message

def direct_ping(socket, counts, quiet):

    # return list of rtts
    rtts = []

    for seq in range(1, counts + 1):
        try:
            response = send_ping(socket)
            rtts.append(response)
            print_info_message(seq, response, quiet)

        except Exception as e:
            print_packet_loss_message(seq, e, quiet)

        time.sleep(1)

    return rtts
