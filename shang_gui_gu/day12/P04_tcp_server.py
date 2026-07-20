"""
tcp协议通信演示-服务端
"""
import socket

# 创建 TCP 套接字：AF_INET 表示使用 IPv4，SOCK_STREAM 表示使用 TCP（面向连接的字节流）协议
tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 绑定本机地址和端口，0.0.0.0 表示监听所有网卡，8888 为服务端口
tcp_socket.bind(('0.0.0.0', 8888))

# 开启监听，将套接字设为被动模式；参数 5 为等待连接队列的最大长度（半连接/未 accept 的连接数）
tcp_socket.listen(5)

# 阻塞等待客户端连接，一旦有连接建立就返回
# client_socket 是与该客户端通信的新套接字，client_info 为客户端地址元组 (ip, port)
client_socket, client_info = tcp_socket.accept()

while True:
    # 通过客户端套接字接收数据，最多接收 1024 字节（TCP 是字节流，需注意粘包/半包问题）
    recv_data = client_socket.recv(1024)
    # 将字节数据按 utf-8 解码为字符串后打印，并显示客户端的 IP 和端口
    print(f"接收到客户端{client_info[0]}:{client_info[1]}消息：{recv_data.decode('utf-8')}")
    # 向该客户端回复消息，需先将字符串编码为字节
    client_socket.send('你好，消息又收到了~'.encode('utf-8'))

# 关闭与客户端通信的套接字（因上方为死循环，以下两行实际不会执行）
client_socket.close()
# 关闭监听套接字，释放端口
tcp_socket.close()

