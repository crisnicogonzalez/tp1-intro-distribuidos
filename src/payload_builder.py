from constants import MSG_SIZE, COUNT_SIZE, PING, PONG, REVERSE, PROXY, IP_SIZE, PORT_SIZE, STOP, RTT, RTT_SIZE


def fill_with_x(initial_payload):
    miss = MSG_SIZE - len(initial_payload)
    return initial_payload + miss * "X"


def fill_with_zero(initial_payload):
    miss = COUNT_SIZE - len(str(initial_payload))
    return miss * "X" + str(initial_payload)


def fill_ip(ip):
    miss = IP_SIZE - len(ip)
    return miss * "X" + ip


def fill_rtt(rtt):
    miss = RTT_SIZE - len(rtt)
    return miss * "X" + rtt


def fill_port(port):
    miss = PORT_SIZE - len(str(port))
    return miss * "X" + str(port)


def build_ping_msg(seq):
    return fill_with_x(PING + fill_with_zero(seq))


def build_pong_msg(seq):
    return fill_with_x(PONG + fill_with_zero(seq))


def build_reverse_msg(counts):
    return fill_with_x(REVERSE + fill_with_zero(counts))


def build_proxy_msg(counts, ip, port):
    return fill_with_x(PROXY + fill_with_zero(counts) + fill_ip(ip) + fill_port(port))


def build_stop_connection_msg():
    return fill_with_x(STOP)


def build_rtt_response_msg(seq, rtt):
    return fill_with_x(RTT + fill_with_zero(seq) + fill_rtt(rtt) )


def decode_proxy_message(msj):
    count = int(msj[1:11].replace('X', ''))
    ip_address = msj[11:27].replace('X', '')
    port = int(msj[27:].replace('X', ''))
    return [PROXY, count, ip_address, port]


def decode_reverse_message(msj):
    count = int(msj[1:11].replace('X', ''))
    return [REVERSE, count]


def decode_ping_message(msj):
    seq = int(msj[1:11].replace('X', ''))
    return [PING, seq]


def decode_pong_message(msj):
    seq = int(msj[1:11].replace('X', ''))
    return [PONG, seq]


def decode_rtt_message(msj):
    seq = int(msj[1:11].replace('X', ''))
    rtt = msj[11:21].replace('X', '')
    return [RTT, seq, rtt]


def decode_message(msj):
    if msj.startswith(PING):
        return decode_ping_message(msj)

    elif msj.startswith(PONG):
        return decode_pong_message(msj)

    elif msj.startswith(REVERSE):
        return decode_reverse_message(msj)

    elif msj.startswith(PROXY):
        return decode_proxy_message(msj)

    else:
        return [STOP]
