"""__author__=吴佩隆"""
from datetime import datetime
import time
from threading import Thread

"""
一个进程中默认有且只有一个线程，叫主线程
默认情况所有代码都是在主线程中执行

进程中主线程以外的线程都叫子线程

1.怎么让进程拥有子线程
在进程中创建threading模块中的Thread类的对象或Thread类的子类对象

2.程序(进程)的结束
只有进程中有的线程都结束了进程才会结束
"""


def download(film_name: str):
    print('%s开始下载:%s' % (film_name, datetime.now()))
    time.sleep(5)
    print('%s下载结束:%s' % (film_name, datetime.now()))


# download('《三体一:地球往事》')
# download('《三体二:黑暗森林》')
# download('《三体三:死神永生》')

# 1.创建线程对象 - 子线程
"""
线程对象 = Thread(target=需要在子线程中调用的函数，args=元组)

说明:target - 需要在子线程中执行的任务
    args - target对应的函数在调用的时候传的参数
"""

t1 = Thread(target=download, args=('《三体一:地球往事》',))
t2 = Thread(target=download, args=('《三体二:黑暗森林》',))
t3 = Thread(target=download, args=('《三体三:死神永生》',))

# 2.让子线程执行子线程中的任务
# 线程对象.start() - 在子线程中调用target对应的函数，并且将args中的元素作为参数
# 线程开始之后只有自然死亡或者异常两种情况能终止

t1.start()
t2.start()
t3.start()
