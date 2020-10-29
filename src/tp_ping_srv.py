import argparse
import socket
from constants import PING, REVERSE, PROXY, MSG_SIZE
from reverse_ping_srv import reverse_ping_srv
from direct_ping_srv import direct_ping_srv
from proxy_ping_srv import proxy_ping_srv
from payload_builder import decode_message


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-H", "--host", default="127.0.0.1")
    parser.add_argument("-P", "--port", type=int, default="8080")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase  output  verbosity", default=False)
    return parser.parse_args()


def main():
    args = parse_arguments()
    address = (args.host, args.port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    print("Server up!!!")

    verbose = args.verbose

    while True:
        if verbose:
            print("Wait connections")
        conn, addr = sock.accept()
        if not conn:
            break
        if verbose:
            print("Accepted connection from {}".format(addr))

        connection_is_alive = True

        while connection_is_alive:

            msj = str(conn.recv(MSG_SIZE).decode())

            msj_decoded = decode_message(msj)

            if msj_decoded[0] == PING:
                direct_ping_srv(conn, verbose)

            elif msj_decoded[0] == REVERSE:
                reverse_ping_srv(conn, int(msj_decoded[1]), verbose)

            elif msj_decoded[0] == PROXY:
                proxy_ping_srv(conn, int(msj_decoded[1]), msj_decoded[2], int(msj_decoded[3]), verbose)

            else:
                connection_is_alive = False

        print("Connection with client finished")

    sock.close()


if __name__ == "__main__":
    main()
