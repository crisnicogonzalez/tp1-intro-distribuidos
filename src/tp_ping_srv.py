import argparse
import socket
from constants import CHUNK_SIZE, PING, REVERSE, STOP
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

        connection_is_alive = True

        while connection_is_alive:

            msj = str(conn.recv(CHUNK_SIZE).decode())

            splited_msg = msj.split("-")

            option = splited_msg[0]

            # Reverse case
            # Proxy case
            if len(splited_msg) == 2:
                counts = int(splited_msg[1])

                if option == REVERSE:
                    reverse_ping_srv(conn, addr, counts)
            else:
                # ping case
                # stop case
                if option == PING:
                    direct_ping_srv(conn)

                elif option == STOP:
                    connection_is_alive = False


        print("Connection with client finished")

    sock.close()


if __name__ == "__main__":
    main()
