import argparse
import socket
from constants import CHUNK_SIZE, PING, REVERSE
from reverse_ping_srv import reverse_ping_srv
from direct_ping_srv import direct_ping_srv
from proxy_ping_srv import proxy_ping_srv


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

        msj = str(conn.recv(CHUNK_SIZE).decode())

        option, counts = msj.split("-")

        if option == PING:
            direct_ping_srv(conn, addr, counts)

        elif option == REVERSE:
            reverse_ping_srv(conn, addr, counts)

        # elif option == PROXY:
        #    proxy_ping_srv(conn,addr,counts)

    sock.close()


if __name__ == "__main__":
    main()
