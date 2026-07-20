"""
socket 网络通信
"""
import socket

tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

