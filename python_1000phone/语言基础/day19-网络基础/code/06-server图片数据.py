"""__author__=吴佩隆"""

from socket import socket

server = socket()

server.bind(('10.7.156.50', 6067))
server.listen(512)

while True:
    connection, address = server.accept()

    with open('./image/716428.png', 'rb') as f:
        data = f.read()

    # 发送总长度
    connection.send(str(len(data)).encode())
    # 图片数据
    connection.send(data)