"""__author__=吴佩隆"""

from threading import *
from datetime import datetime
import time
from random import randint

# 1.join
"""
线程对象.join()
其他代码

这儿的其他代码会在线程对象执行结束后才执行
"""


def download(film_name: str):
    print('%s开始下载:%s' % (film_name, datetime.now()))
    time.sleep(randint(3, 7))
    print('%s下载结束:%s' % (film_name, datetime.now()))


t1 = Thread(target=download, args=('《三体一:地球往事》',))
t2 = Thread(target=download, args=('《三体二:黑暗森林》',))
t3 = Thread(target=download, args=('《三体三:死神永生》',))

# 需求1:所有电影下载结束后打印所有电影下载完成!
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
# print('所有电影下载结束')

# 要求三体1，2下载完成后才下载三体3

t1.start()
t2.start()

t1.join()
t2.join()

t3.start()