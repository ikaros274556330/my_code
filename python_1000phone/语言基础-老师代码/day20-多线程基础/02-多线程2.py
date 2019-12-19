"""__author__=余婷"""
from threading import *
from datetime import datetime
import time


class DownloadThread(Thread):

    def __init__(self, film_name):
        super().__init__()
        self.film_name = film_name

    # 这个run方法是会在子线程中自动调用的方法，要求除了self以外不能有其他参数
    def run(self) -> None:
        print('%s开始下载：%s' % (self.film_name, datetime.now()))
        time.sleep(5)
        print('%s结束下载：%s' % (self.film_name, datetime.now()))


t1 = DownloadThread('卧虎藏龙')
t2 = DownloadThread('让子弹飞')
t3 = DownloadThread('五十度灰')

# 在子线程中执行下载操作
t1.start()
t2.start()
t3.start()

# 在主线程中执行下载操作
# t1.run()
# t2.run()
# t3.run()





