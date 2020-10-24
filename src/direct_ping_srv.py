from constants import CHUNK_SIZE
from constants import PING
from constants import PONG
from constants import STOP

def direct_ping_srv(conn):

    while True:

        print("waiting for ping message...")

        # recieve "ping" message
        ping = conn.recv(CHUNK_SIZE).decode()

        print(ping)

        if ( ping == PING ):
            print("ping message received successfully")
            msj = PONG

            # send "pong" message
            print("sending pong response")
            conn.send(msj.encode())

        elif (ping == STOP):
            print("stop message received successfully")
            break
        else:
            print("ping message received unsuccessfully")