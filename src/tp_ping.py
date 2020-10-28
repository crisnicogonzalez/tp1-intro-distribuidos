import argparse
import statistics
import time
from constants import STOP
from reverse_ping import reverse_ping
from direct_ping import direct_ping
from proxy_ping import proxy_ping
from socket_client import send_msg
from socket_client import create_socket


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

    parser.add_argument("-d", "--dest", help="destination  IP  address", metavar='ADDR:PORT', default="127.0.0.2:8081")

    return parser.parse_args()


def show_statistics(measures, total_time, count):
    print("")
    print("--- 127.0.0.1 ping statistics ---")
    print("{} packets transmitted, {} received, {}% packet loss, time {} ms".format(count, len(measures), (1 - len(measures)/count)*100, total_time))
    print("rtt min / avg / max / mdev = {:.3f}/{:.3f}/{:.3f}/{:.3f} ms".format(min(measures), statistics.mean(measures), max(measures), statistics.stdev(measures)))


def get_ping_type(args):
    if args.reverse:
        return "Reverse Ping"
    elif args.proxy:
        return "Proxy Ping"
    elif args.ping:
        return "Direct Ping"


def get_client_address(args, soc):
    if args.reverse or args.proxy:
        return "{}".format(args.server)
    else:
        return "{}:{}".format(soc.getsockname()[0], soc.getsockname()[1])


def get_server_address(args, soc):
    if args.reverse:
        return "{}:{}".format(soc.getsockname()[0], soc.getsockname()[1])
    elif args.proxy:
        return "{}".format(args.dest)
    elif args.ping:
        return "{}".format(args.server)


def show_initial_messages(args):
    print("TP-PING v0.1")
    print("Operation: {}".format(get_ping_type(args)))


def show_address_messages(args, soc):
    print("Server Address: {}".format(get_server_address(args, soc)))
    print("Client Address: {}".format(get_client_address(args, soc)))


def exec_protocol(args, soc, count):
    if args.reverse:
        return reverse_ping(soc, count, args.quiet)

    elif args.proxy:
        return proxy_ping(soc, count, args.dest, args.quiet)

    elif args.ping:
        return direct_ping(soc, count, args.quiet)


def main():
    start = time.time()
    args = parse_arguments()

    splited_ip = args.server.split(":")
    soc = create_socket(splited_ip[0], int(splited_ip[1]))

    show_initial_messages(args)
    show_address_messages(args, soc)
    count = args.count

    measures = exec_protocol(args, soc, count)
    send_msg(soc, STOP)

    end = time.time()
    diff = end - start
    total = int(diff * 1000)

    show_statistics(measures, total, count)


if __name__ == "__main__":
    main()
