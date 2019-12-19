"""__author__=余婷"""
from socket import socket

# 1.创建套接字对象
server = socket()
# 2.绑定ip和端口
server.bind(('10.7.156.58', 8081))
# 3.准备监听
server.listen(512)
# 4.让服务一直运行
while True:
    print('开始监听...')
    # 1.接受请求
    connection, address = server.accept()

    # 2.持续交流
    while True:
        # 接收消息
        re_data = connection.recv(1024)
        re_message = re_data.decode(encoding='utf-8')
        print('%s:%s'% (address[0], re_message))
        if re_message == '拜拜' or re_message == 'ByeBye':
            connection.close()
            break

        # 发送消息
        message = input('server:')
        connection.send(message.encode())
        if message == '拜拜' or message == 'ByeBye':
            connection.close()
            break




