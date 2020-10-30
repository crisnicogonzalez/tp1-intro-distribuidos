from socket_client import create_socket
from payload_builder import build_stop_connection_msg, build_pong_msg , build_rtt_response_msg
from direct_ping import direct_ping


def proxy_ping_srv(conn, count, ip_proxy, port_proxy, verbose):

    try:
        proxy_conn = create_socket(ip_proxy, port_proxy)

    except Exception:
        print("Error: Server not found. Proxy ping finished")
        return

    if verbose:
        print("proxy ping request received counts -> {}".format(count))

    response = build_pong_msg(0)
    conn.send(response.encode())

    for seq in range(1, count + 1):
        rtt = direct_ping(proxy_conn, 1, True, verbose)

        if len(rtt) == 0:
            continue
        msj = build_rtt_response_msg(seq, str(rtt[0]))
        conn.send(msj.encode())


    msj = build_stop_connection_msg()
    proxy_conn.send(msj.encode())
    proxy_conn.close()

    if verbose:
        print("proxy ping finished")
