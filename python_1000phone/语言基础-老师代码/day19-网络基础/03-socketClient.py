"""__author__=余婷"""
from socket import socket

# 1.客户端套接字
# 1)创建套接字对象(买电话)
client = socket()

# 2)连接服务器(拨号)
client.connect(('10.7.156.58', 12342))

# 3)发送消息
client.send('服务器你好吗？'.encode())

# 4)接收消息
re_data = client.recv(1024)
print(re_data.decode(encoding='utf-8'))

# 5)关闭连接
client.close()
