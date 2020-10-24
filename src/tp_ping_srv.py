import argparse
import socket
from constants import CHUNK_SIZE


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

        bytes_received = 0
        data = str(conn.recv(CHUNK_SIZE).decode())
        bytes_received += len(data)

        print("Received msg {}".format(data))

        # Send number of bytes received
        conn.send(str(bytes_received).encode())

    sock.close()


if __name__ == "__main__":
    main()
