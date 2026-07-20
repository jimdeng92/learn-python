"""
udp协议通信演示-客户端
"""

import socket

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    udp_socket.sendto(input('对服务器说：').encode('utf-8'), ('127.0.0.1', 8888))
    server_data, server_info = udp_socket.recvfrom(1024)
    print(f"接收到服务器发送的数据：{server_data.decode('utf-8')}")

udp_socket.close()
