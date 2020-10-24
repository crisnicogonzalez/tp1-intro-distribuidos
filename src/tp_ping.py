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
    server_address = (args.host, args.port)

    msg = "PING"

    print("Sending {} bytes from {}".format(4, msg))

    # Create socket and connect to server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    sock.send(msg.encode())

    # Recv amount of data received by the server
    num_bytes = sock.recv(CHUNK_SIZE)

    print("Server received {} bytes".format(num_bytes.decode()))

    sock.close()


if __name__ == "__main__":
    main()
