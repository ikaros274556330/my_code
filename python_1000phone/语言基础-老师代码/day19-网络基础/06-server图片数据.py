"""__author__=余婷"""
from socket import socket

server = socket()
server.bind(('10.7.156.58', 8086))
server.listen(512)
while True:
    connection, address = server.accept()
    # 发送图片
    with open('海贼王/aa.wav', 'rb') as f:
        data = f.read()
    # 先发送整个图片的总长度  100 -> '100'
    length = len(data)
    connection.send(str(length).encode())
    # 再发送图片数据
    connection.send(data)

