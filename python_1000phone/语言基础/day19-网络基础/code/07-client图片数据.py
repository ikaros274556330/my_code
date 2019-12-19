"""__author__=吴佩隆"""
from socket import socket

client = socket()
client.connect(('10.7.156.50', 6067))

# while True:
#     re_data = client.recv(1024)
#     length = len(re_data)
#     with open('./re_image/test.png','ab') as f:
#         f.write(re_data)
#
#     if length < 1024:
#         break

total_length = int(client.recv(1024).decode(encoding='utf-8'))
sum_length = 0

# 方法1:接收一点写一点~
while True:
    re_data = client.recv(1024)
    length = len(re_data)
    sum_length += length
    with open('./re_image/test.png','ab') as f:
        f.write(re_data)

    if sum_length == total_length:
        break


