"""
udp协议通信演示-服务端
"""
import socket

# 创建 UDP 套接字：AF_INET 表示使用 IPv4，SOCK_DGRAM 表示使用 UDP（数据报）协议
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 绑定本机地址和端口，0.0.0.0 表示监听所有网卡，8888 为服务端口
udp_socket.bind(('0.0.0.0', 8888))

while True:
    # 阻塞等待接收数据，最多接收 1024 字节
    # 返回值：recv_data 为收到的字节数据，client_info 为发送方地址元组 (ip, port)
    recv_data, client_info = udp_socket.recvfrom(1024)
    # 将字节数据按 utf-8 解码为字符串后打印，并显示发送方的 IP 和端口
    print(f"接收到来自{client_info[0]}:{client_info[1]}的数据，{recv_data.decode('utf-8')}")
    # 向发送方回复消息，需先将字符串编码为字节，第二个参数指定接收方地址
    udp_socket.sendto('你好，消息已收到'.encode('utf-8'), client_info)

# 关闭套接字，释放资源（因上方为死循环，此行实际不会执行）
udp_socket.close()
