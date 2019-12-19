# itchat使用教程  

itchat是一个开源的微信个人号接口，使用python调用微信从未如此简单。使用不到三十行的代码，你就可以完成一个能够处理所有信息的微信机器人。

首先，在终端安装一下itchat:

```python
pip install itchat
```

##1.登录

1. login()  - 每次运行程序都需要扫二维码
2. login(hotReload==True)  - 下次登录不用再扫二维码
3. auto_login(loginCallback=登录成功回调函数, exitCallback=退出登录回调函数)



## 2.退出登录

1. logout()    - 强制退出登录



## 3.获取好友信息

1. get_friends(update=True)



## 4.发送消息  

send(msg=消息内容, toUserName=用户名)

1) msg的值会因为消息类型不同而不同：

文本消息 - 引号中直接写要发送的文字内容

发送文件 - @fil@文件路径

发送图片 - @img@图片路径

发送视频 - @vid@视频路径

2)toUserName:  发送对象，如果不填就发送给自己

## 5.接收消息

想要自动接收消息，需要先对不同类型的消息进行注册，如果没有注册，对应类型的消息将不会被接收.

注册的方式如下:

```python
@itchat.msg_register(消息类型,isFriendChat=True, isGroupChat=True,isMpChat=True)

def 函数名(msg):
	#接收到对应的消息会自动执行的代码段
    #msg.download(msg['FileName'])   #这个同样是下载文件的方式
    #msg['Text'](msg['FileName'])      #下载文件

```

1）消息类型:

| 参数 | 类型 | Text键值           |
| ---- | ---- | ------------------ |
| TEXT | 文本 | 文本内容(文字消息) |
|MAP|地图|位置文本(位置分享)|
|CARD|名片|推荐人字典(推荐人的名片)|
|SHARING|分享|分享名称(分享的音乐或者文章等)|
|RECORDING|语音|下载方法|
|ATTACHMENT|附件|下载方法|
|VIDEO|小视频|下载方法|
|FRIENDS|好友邀请|添加好友所需参数|
|SYSTEM|系统消息|更新内容的用户或群聊的UserName组成的列表|
|NOTE|通知|通知文本(消息撤回等)|
|PICTURE|图片/表情|下载方法|




