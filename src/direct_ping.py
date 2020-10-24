from constants import CHUNK_SIZE
from constants import PING
from constants import PONG
from constants import STOP
from datetime import datetime

def direct_ping(socket, counts):

    # return list of rtts
    rtts = []

    msj = PING

    for seq in range(1, counts + 1):

        try:
            # send message "ping"
            rtt_begin = datetime.now()
            socket.send(msj.encode())

            # recieve message "pong"
            pong = socket.recv(CHUNK_SIZE).decode()
            rtt_end = datetime.now()
            print(pong)
        except:
            print("Error: connection terminate")

        if ( pong == PONG ):
            rtt = (rtt_end - rtt_begin).total_seconds() / 1000
            rtts.append(rtt)
            print("{} bytes  from  157.92.49.38:  seq={} time ={} ms".format(len(pong),seq,rtt))

        else:
            print("{} bytes  from  157.92.49.38:  seq={} packet incomplete".format(len(pong),seq))

    # send message to indicate server to stop recieving pings
    msj = STOP
    socket.send(msj.encode())

    return rtts