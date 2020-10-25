from socket_client import send_ping
from constants import PONG

def direct_ping(socket, counts):

    # return list of rtts
    rtts = []

    for seq in range(1, counts + 1):
        response = send_ping(socket)
        if response[0]:
            rtts.append(response[0])
            print("{} bytes  from  157.92.49.38:  seq={} time ={} ms".format(len(PONG),seq,response[1]))

        else:
            print("Error: packet incomplete, seq = {}".format(seq))

    return rtts