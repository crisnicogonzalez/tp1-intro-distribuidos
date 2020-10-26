from constants import MSG_SIZE, COUNT_SIZE, PING, PONG, REVERSE, PROXY, IP_SIZE, PORT_SIZE, STOP


def fill_with_x(initial_payload):
    miss = MSG_SIZE - len(initial_payload)
    return initial_payload + miss * "X"


def fill_with_zero(initial_payload):
    miss = COUNT_SIZE - len(str(initial_payload))
    return miss * "X" + str(initial_payload)


def fill_ip(ip):
    miss = IP_SIZE - len(ip)
    return miss * "X" + ip


def fill_port(port):
    miss = PORT_SIZE - len(str(port))
    return miss * "X" + str(port)


def build_ping_msg():
    return fill_with_x(PING)


def build_pong_msg():
    return fill_with_x(PONG)


def build_reverse_msg(counts):
    return fill_with_x(REVERSE + fill_with_zero(counts))


def build_proxy_msg(counts, ip, port):
    return fill_with_x(PROXY + fill_with_zero(counts) + fill_ip(ip) + fill_port(port))


def build_stop_connection_msg():
    return fill_with_x(STOP)


def decode_proxy_message(msj):
    count = int(msj[1:11].replace('X', ''))
    ip_address = msj[11:27].replace('X', '')
    port = int(msj[27:].replace('X', ''))
    return [PROXY, count, ip_address, port]


def decode_reverse_message(msj):
    count = int(msj[1:11].replace('X', ''))
    return [REVERSE, count]


def decode_message(msj):
    if msj.startswith(PING):
        return [PING]

    elif msj.startswith(PONG):
        return [PONG]

    elif msj.startswith(REVERSE):
        return decode_reverse_message(msj)

    elif msj.startswith(PROXY):
        return decode_proxy_message(msj)

    else:
        return [STOP]

