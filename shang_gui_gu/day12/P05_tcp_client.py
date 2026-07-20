"""
tcp协议通信演示-客户端
"""
import socket

# 创建 TCP 套接字：AF_INET 表示使用 IPv4，SOCK_STREAM 表示使用 TCP（面向连接的字节流）协议
tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 向服务端发起连接请求（三次握手），连接成功后才能收发数据
# 127.0.0.1 为本机回环地址，8888 需与服务端监听端口一致
tcp_socket.connect(('127.0.0.1', 8888))

while True:
    # 获取用户输入并编码为字节后发送
    # TCP 与 UDP 不同：send 只需传数据，无需每次指定目标地址（连接建立时已确定）
    tcp_socket.send(input('想对服务端说什么？').encode('utf-8'))
    # 阻塞等待服务端回复，最多接收 1024 字节
    recv_data = tcp_socket.recv(1024)
    # 将服务端返回的字节数据按 utf-8 解码为字符串后打印
    print(recv_data.decode('utf-8'))

# 关闭套接字，触发四次挥手断开连接（因上方为死循环，此行实际不会执行）
tcp_socket.close()
