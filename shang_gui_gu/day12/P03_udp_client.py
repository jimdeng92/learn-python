"""
udp协议通信演示-客户端
"""

import socket

# 创建 UDP 套接字：AF_INET 表示使用 IPv4，SOCK_DGRAM 表示使用 UDP（数据报）协议
# 客户端无需 bind，发送数据时系统会自动分配临时端口
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    # 获取用户输入并编码为字节后发送，第二个参数为服务端地址 (ip, port)
    # 127.0.0.1 为本机回环地址，8888 需与服务端监听端口一致
    udp_socket.sendto(input('对服务器说：').encode('utf-8'), ('127.0.0.1', 8888))
    # 阻塞等待服务端回复，最多接收 1024 字节
    # 返回值：server_data 为收到的字节数据，server_info 为服务端地址元组
    server_data, server_info = udp_socket.recvfrom(1024)
    # 将服务端返回的字节数据按 utf-8 解码为字符串后打印
    print(f"接收到服务器发送的数据：{server_data.decode('utf-8')}")

# 关闭套接字，释放资源（因上方为死循环，此行实际不会执行）
udp_socket.close()
