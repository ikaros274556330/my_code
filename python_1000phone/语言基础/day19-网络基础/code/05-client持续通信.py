"""__author__=吴佩隆"""

from socket import socket

client = socket()

client.connect(('10.7.156.50', 8080))

while True:
    message = input('client:')
    client.send(message.encode())
    if message == '拜拜' or message == '88':
        client.close()
        break

    re_message = client.recv(1024).decode(encoding='utf-8')
    print('server:', re_message)
    if message == '拜拜' or message == '88':
        client.close()
        break


# client = socket()
# client.connect(('10.7.156.50', 6666))
# while True:
#
#     client.send('test~~~~~~~~~~~'.encode())
#
#     data = client.recv(1024)
#     print(data.decode(encoding='utf8'))




















