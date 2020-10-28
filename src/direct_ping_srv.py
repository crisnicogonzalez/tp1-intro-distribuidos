from payload_builder import build_ping_msg, build_pong_msg
from constants import STOP, PING, MSG_SIZE


def direct_ping_srv(conn):

    print("ping message received successfully")

    ping = build_ping_msg()
    pong = build_pong_msg()

    while not ping.startswith(STOP):

        if ping.startswith(PING):
            print("ping message received successfully")

            # send "pong" message
            print("sending pong response")
            conn.send(pong.encode())

        else:
            print("ping message received unsuccessfully")

        # recieve "ping" message
        ping = conn.recv(MSG_SIZE).decode()

    print("stop message received successfully")
    print("direct ping finished")
