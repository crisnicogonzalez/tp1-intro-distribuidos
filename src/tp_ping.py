import argparse
import socket
from constants import CHUNK_SIZE
from reverse_ping import reverse_ping
from direct_ping import direct_ping
from proxy_ping import proxy_ping

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-H", "--host", default="127.0.0.1")
    parser.add_argument("-P", "--port", type=int, default="8080")
    parser.add_argument("-r", "--reverse", help="reverse ping", action="store_true")
    parser.add_argument("-p", "--ping", help="direct ping", action="store_true")
    parser.add_argument("-x", "--proxy", help="proxy pin", action="store_true")

    return parser.parse_args()


def create_socket(host, port):
    # server_address = (host, port)
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(server_address)
    # return sock
    return None


def main():
    args = parse_arguments()
    soc = create_socket(args.host, args.port)

    if args.reverse:
        reverse_ping(soc)

    elif args.ping:
        direct_ping(soc)

    elif args.proxy:
        proxy_ping(soc)

    # msg = "PING"
    #
    # print("Sending {} bytes from {}".format(4, msg))
    #
    # # Create socket and connect to server
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(server_address)
    #
    # sock.send(msg.encode())
    #
    # # Recv amount of data received by the server
    # num_bytes = sock.recv(CHUNK_SIZE)
    #
    # print("Server received {} bytes".format(num_bytes.decode()))
    #
    # sock.close()


if __name__ == "__main__":
    main()
