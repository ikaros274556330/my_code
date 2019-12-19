"""__author__=余婷"""
from socket import socket

client = socket()
client.connect(('10.7.156.58', 8086))

# 接收图片长度
total_length = int(client.recv(1024).decode())
print('第一次:', total_length)


sum_length = 0   # 保存接收到的图片的总长度
sum_data = bytes()   # 保存接收到的图片的总数据


# 接收图片
while True:
    # 方法一: 接收一点儿写一点儿
    # re_data = client.recv(1024)
    # length = len(re_data)
    # sum_length += length
    # print('当前接收的数据的长度:', length)
    # with open('client/test.jpeg', 'ab') as f:
    #     f.write(re_data)
    #
    # if sum_length == total_length:
    #     break

    re_data = client.recv(1024)
    sum_data += re_data
    if len(sum_data) == total_length:
        with open('client/test1.wav', 'wb') as f:
            f.write(sum_data)
        break





