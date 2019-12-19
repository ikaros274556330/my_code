"""__author__=吴佩隆"""
from socket import socket

# 1.客户端套接字
# 1)创建套接字对象(买座机电话)
client = socket()

# 2)连接服务器(拨号)
client.connect(('10.7.156.50', 12345))

# 3)发送消息
client.send('你好,服务器!'.encode())

# 4)接收消息
re_data = client.recv(1024)
print(re_data.decode(encoding='utf-8'))

# 5)关闭连接
client.close()