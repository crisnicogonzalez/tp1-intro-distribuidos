from socket_client import create_socket
from payload_builder import build_stop_connection_msg, build_pong_msg
from direct_ping import direct_ping
from constants import PONG

def proxy_ping_srv(conn, count, ip_proxy, port_proxy):

    try:
        proxy_conn = create_socket(ip_proxy, port_proxy)

    except:
        print("Error: Server not found. Proxy ping finished")
        return

    response = build_pong_msg()
    conn.send(response.encode())

    for seq in range(1, count + 1):
        rtt = direct_ping(proxy_conn, 1)
        msj = str(rtt[0])
        conn.send(msj.encode())

    msj = build_stop_connection_msg()
    proxy_conn.send(msj.encode())
    proxy_conn.close()

    print("proxy ping finished")
