from constants import CHUNK_SIZE
from constants import PING
from constants import PONG
from constants import STOP


def direct_ping_srv(conn):

    print("ping message received successfully")

    ping = PING

    while ping != STOP:

        if (ping == PING):
            print("ping message received successfully")
            msj = PONG

            # send "pong" message
            print("sending pong response")
            conn.send(msj.encode())

        else:
            print("ping message received unsuccessfully")

        # recieve "ping" message
        ping = conn.recv(CHUNK_SIZE).decode()

    print("stop message received successfully")
