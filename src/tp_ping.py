import argparse
import socket
from constants import CHUNK_SIZE
from reverse_ping import reverse_ping
from direct_ping import direct_ping
from proxy_ping import proxy_ping


def parse_arguments():

    parser = argparse.ArgumentParser(description='TP1 - Introducción Distribuidos 75.43 - Client')

    parser.allow_abbrev = False

    verbose_group = parser.add_mutually_exclusive_group()
    verbose_group.add_argument("-v", "--verbose", action="store_true", help="increase  output  verbosity", default=False)
    verbose_group.add_argument("-q", "--quiet", action="store_true", help="decrease  output  verbosity", default=False)

    parser.add_argument("-s", "--server", default="127.0.0.1:8080", help="server  IP  address", metavar='ADDR')
    parser.add_argument("-c", "--count", type=int, default=10, help="stop  after <count > replies")

    ping_type_group = parser.add_mutually_exclusive_group()
    ping_type_group.add_argument("-p", "--ping", action="store_true", help="direct  ping", default=True)
    ping_type_group.add_argument("-r", "--reverse", action="store_true", help="reverse  ping", default=False)
    ping_type_group.add_argument("-x", "--proxy", action="store_true", help="proxy  ping", default=False)

    parser.add_argument("-d", "--dest", help="destination  IP  address", metavar='ADDR:PORT', default=None)

    return parser.parse_args()


def create_socket(host, port):
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    return sock


def main():
    args = parse_arguments()
    splited_ip = args.server.split(":")
    soc = create_socket(splited_ip[0], int(splited_ip[1]))
    count = args.count
    if args.reverse:
        reverse_ping(soc, count)

    elif args.ping:
        direct_ping(soc, count)

    elif args.proxy:
        proxy_ping(soc, count)

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
