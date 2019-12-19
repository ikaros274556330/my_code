"""__author:吴佩隆"""
import itchat
import time

# 1.登录
def wx_login():
    print('登录成功')

def wx_exit():
    print('退出登录')

# itchat.auto_login(hotReload=是否自动登录)
itchat.auto_login(hotReload=True,loginCallback=wx_login,exitCallback=wx_exit)

# 2.退出登录
# itchat.logout()

# 3.获取好友信息 - 返回所有好友的列表
all_friends = itchat.get_friends()
# print(all_friends)
# for friend in all_friends:
#     print(friend)
#
# 4.发送消息
# 发文字消息:itchat.send(消息,目标)
for friend in all_friends:
#      1）给指定好友'XX'发送消息
#      if friend['NickName'] == 'XX':
#        发送消息
#          itchat.send('hello!',)
#     2）给所有好友发送消息
#     itchat.send('最近好吗？(开发测试勿回)',friend['UserNmae'])
#     if friend['NickName'] == 'XX':
#         while True:
#             itchat.send('测试',friend['UserName'])
#             time.sleep(2)


#   4)发送图片
    if friend['NickName'] == 'XX':
        itchat.send('@img@图片地址',friend['UserName'])

# 5接受消息
# 1）注册指定类型的消息
# @itchat.msg_register(消息类型，消息来源1，消息来源2，...)
@itchat.msg_register(itchat.content.TEXT,isFriendChat=True, isGroupChat=True,isMpChat=True)
def get_text_message(msg):
    print('接收到消息',msg)

@itchat.msg_register(itchat.content.PICTURE,isFriendChat=True, isGroupChat=True,isMpChat=True)
def get_image_message(msg):
    print('接收到图片',msg)
    # 下载消息中的文件
    msg.download('./msgFiles/'+msg['FileName'])
    # itchat.send('请发视频',msg['FromUserName'])
# 让微信保持运行
itchat.run()