"""__author__=吴佩隆"""

from threading import Thread
from socket import socket
from random import choice


class Ext(Thread):
    def __init__(self, ip, ext_phone: socket, word):
        super().__init__()
        self.word = word
        self.ext_phone = ext_phone
        self.ip = ip

    def run(self):
        while True:
            data = self.ext_phone.recv(1024)
            message = data.decode('utf-8')
            self.word.append(message)
            print('%s客户:%s' % (self.ip, message))
            self.ext_phone.send(choice(self.word).encode())


def bind_address_listen(host, ip: str, port: int):
    host.bind((ip, port))
    host.listen(101)
    return host


def main():
    word_list = []
    host = socket()
    host = bind_address_listen(host, '10.7.156.50', 8080)
    while True:
        ext_phone, address = host.accept()
        print('接到电话')
        new_thread = Ext(address[0], ext_phone, word_list)
        new_thread.start()


main()
