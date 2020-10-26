import argparse
import socket
from constants import PING, REVERSE, STOP, PROXY, MSG_SIZE
from reverse_ping_srv import reverse_ping_srv
from direct_ping_srv import direct_ping_srv
from proxy_ping_srv import proxy_ping_srv
from payload_builder import decode_message


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-H", "--host", default="127.0.0.1")
    parser.add_argument("-P", "--port", type=int, default="8080")

    return parser.parse_args()


def main():
    args = parse_arguments()
    address = (args.host, args.port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    print("server up!!!")

    while True:
        conn, addr = sock.accept()
        if not conn:
            break

        print("Accepted connection from {}".format(addr))

        connection_is_alive = True

        while connection_is_alive:

            msj = str(conn.recv(MSG_SIZE).decode())

            msj_decoded = decode_message(msj)

            if msj_decoded[0] == PING:
                direct_ping_srv(conn)

            elif msj_decoded[0] == REVERSE:
                reverse_ping_srv(conn, int(msj_decoded[1]))

            elif msj_decoded[0] == PROXY:
                proxy_ping_srv(conn, int(msj_decoded[1]), msj_decoded[2], int(msj_decoded[3]))

            else:
                connection_is_alive = False

        print("Connection with client finished")

    sock.close()


if __name__ == "__main__":
    main()
