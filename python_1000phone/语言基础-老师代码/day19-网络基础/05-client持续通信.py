"""__author__=余婷"""
from socket import socket

# 1.创建套接字对象
client = socket()
# 2.建立连接
client.connect(('10.7.156.58', 8086))
# 3.持续交流
while True:
    # 1.发送消息
    message = input('client:')
    client.send(message.encode())
    if message == '拜拜' or message == 'ByeBye':
        client.close()
        break

    # 2.接收消息
    re_message = client.recv(1024).decode(encoding='utf-8')
    print('server:', re_message)
    if re_message == '拜拜' or re_message == 'ByeBye':
        client.close()
        break

