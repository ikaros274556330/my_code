"""__author__=余婷"""
# import socket
from socket import socket, AF_INET, AF_INET6, SOCK_STREAM, SOCK_DGRAM

# 1.socket编程
"""
socket又叫套接字
socket编程其实就是用代码来实现进行网络通信的两个端；套接字就是实现通信的两个程序
实现通信的两个端分为服务器和客户端两种

python通过socket模块来提供socket编程相关的类和方法；其中socket类就是套接字对应的类
"""
# 2.服务器端的实现
# 1)创建套接字对象(买电话机)
"""
socket(family=AF_INET, type=SOCK_STREAM)

family - 设置ip类型; AF_INET对应的是ipv4; AF_INET6对应的是ipv6
type - 设置传输类型;  SOCK_STREAM对应的是TCP协议; SOCK_DGRAM对应的是UDP协议
"""
server = socket()

# 2)绑定IP和端口(插电话线)
"""
bind((ip地址, 端口))

ip地址: 找到互联网中唯一的一台计算机; 赋值ip地址对应的字符串
端口: 区分同一台计算机中不同的服务(程序); 赋整数,值的范围是0~65535, 其中0~1024属于著名，不能随便用。
     同一时间同一个端口只能对应一个服务
"""
server.bind(('10.7.156.58', 12342))

# 3)开始监听（等电话）
server.listen(512)


# 4)保证服务器一直运行
while True:
    print('开始监听...')
    # 5)接收客户端的请求(接电话)，返回为这个客户端创建的独立的套接字对象(分机)和客户端的地址
    # 当程序运行到这句代码的时候会停下来，直到有请求为止
    connection, address = server.accept()
    print(connection, type(connection))
    print(address)
    print('============')

    # 6)接收消息(听别人说话)
    # recv(一次性能够接收的数据的大小)   - 返回接收到的数据, 数据类型是二进制
    recv_data = connection.recv(1024)
    print(recv_data.decode(encoding='utf-8'))

    # 7)发送消息(说话给别人听)
    # send(需要发送的数据)
    # with open('test.html', 'r', encoding='utf-8') as f:
        #     message = f.read()
        # connection.send(('HTTP/1.1 200 OK\r\n\r\n'+message).encode())
    message = input('(server)请输入:')
    connection.send(message.encode())

    # 8）关闭连接(挂电话)
    connection.close()





