import time
from socket_client import send_ping
from constants import MSG_SIZE


def direct_ping(socket, counts):

    # return list of rtts
    rtts = []

    for seq in range(1, counts + 1):
        try:
            response = send_ping(socket)
            rtts.append(response)
            print("{} bytes from 127.0.0.1: seq={} time={:.3f} ms".format(str(MSG_SIZE), seq, response))
        except Exception as e:
            print("exception handled", e)
            print("Error: packet incomplete, seq={}".format(seq))
        time.sleep(1)

    return rtts
