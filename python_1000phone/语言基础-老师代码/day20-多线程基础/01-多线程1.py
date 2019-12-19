"""__author__=余婷"""
from datetime import datetime
import time
from threading import *

flag = ''
print(flag)

"""
一个进程中默认有且只有一个线程，这个线程叫主线程。默认情况所有的代码都是在主线程中执行
进程中主线程以外的线程都叫子线程

1.怎么让进程拥有子线程
在进程中创建threading模块中Thread类的对象或Thread类的子类对象.

2.程序(进程)的结束
只有进程中有的线程都结束了进程才会结束
线程怎么结束: 线程中任务执行完成，线程才会被销毁
"""


def download(film_name: str):
    print('%s开始下载:%s' % (film_name, datetime.now()))
    for _ in range(5):
        time.sleep(1)
        # 不断下载数据
        if flag:
            return
    print('%s下载结束: %s' % (film_name, datetime.now()))


# download('暮光之城')
# download('两只老虎')
# download('海上钢琴师')

# 1.创建线程对象 - 子线程
"""
线程对象 = Thread(target=函数, args=元组)
 
说明: target  -  函数，需要在子线程中执行的任务(会在子线程中调用)
      args  -   target对应的函数在调用的时候传的参数
    
"""
t1 = Thread(target=download, args=('暮光之城',))

t2 = Thread(target=download, args=('两只老虎',))
t3 = Thread(target=download, args=('海上钢琴师',))

# 2.让子线程执行子线程中的任务
# 线程对象.start()   -  在子线程中调用target对用的函数，并且将args中的元素作为参数
t1.start()

# 删除线程的引用不会让线程销毁
# del t1
t2.start()
t3.start()


# exit()
# print('===================')

# 获取当前正在运行的线程的数量
# print(active_count())
#
# # 获取当前正在运行的所有的线程对象
# for x in enumerate():
#     print(x)

while True:
    flag = input('是否结束:')
    print(flag)
    break


