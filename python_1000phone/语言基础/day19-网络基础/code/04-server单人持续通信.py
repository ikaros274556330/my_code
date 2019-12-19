"""__author__=吴佩隆"""

from socket import socket

server = socket()

server.bind(('10.7.156.50', 6060))

server.listen(512)

while True:
    print('开始监听...')

    connection, address = server.accept()

    while True:
        re_data = connection.recv(1024)
        re_message = re_data.decode(encoding='utf-8')
        print('client:', re_message)
        if re_message == '拜拜' or re_message == '88':
            connection.close()

        message = input('server:')
        connection.send(message.encode())
        if re_message == '拜拜' or re_message == '88':
            connection.close()
            break

