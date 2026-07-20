"""
udp协议通信演示-服务端
"""
import socket

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_socket.bind(('0.0.0.0', 8888))

while True:
    recv_data, client_info = udp_socket.recvfrom(1024)
    print(f"接收到来自{client_info[0]}:{client_info[1]}的数据，{recv_data.decode('utf-8')}")
    udp_socket.sendto('你好，消息已收到'.encode('utf-8'), client_info)

udp_socket.close()
