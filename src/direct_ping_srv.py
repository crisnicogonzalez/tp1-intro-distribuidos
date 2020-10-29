from payload_builder import build_ping_msg, build_pong_msg
from constants import STOP, PING, MSG_SIZE

def direct_ping_srv(conn):

    print("Direct ping request recieved")

    ping = build_ping_msg()
    pong = build_pong_msg()

    while not ping.startswith(STOP):
        try:
            # send "pong" message
            conn.send(pong.encode())

            # recieve "ping" message
            ping = conn.recv(MSG_SIZE).decode()

        except:
            break

    print("direct ping finished")
