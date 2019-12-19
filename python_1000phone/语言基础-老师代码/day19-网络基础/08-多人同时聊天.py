"""__author__=余婷"""
from socket import socket
from threading import Thread


class ConnectionThread(Thread):
    def __init__(self, connection: socket, address):
        super().__init__()
        self.connection = connection
        self.address = address

    def run(self):
        # 实现和一个客户端不断聊天的效果
        while True:
            re_message = (self.connection.recv(1024)).decode(encoding='utf-8')
            print('%s:%s'%(self.address[0], re_message))

            self.connection.send('我是余婷!'.encode())



server = socket()
server.bind(('10.7.156.58', 8086))
server.listen(512)
while True:
    print('监听....')
    connection, address = server.accept()
    t1 = ConnectionThread(connection, address)
    t1.start()





