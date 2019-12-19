"""__author__=余婷"""
import time

# 1.什么是装饰器
"""
装饰器本质是一个函数 = 返回值高阶函数+实参高阶函数+糖语法
装饰器是python的三大神器之一: 装饰器、迭代器、生成器
作用: 给已经写好的函数添加新的功能
"""
# 给函数添加一个功能: 统计函数的执行时间


# ==========方法一: 在每个需要添加功能的函数中加入相应代码=========
def yt_sum(x, y):
    start = time.time()   # 获取当前时间
    sum1 = x + y
    print(sum1)
    end = time.time()
    print('函数执行时间: %fs' % (end - start))


yt_sum(100, 200)


def factorial(n):
    start = time.time()
    sum1 = 1
    for num in range(1, n+1):
        sum1 *= num
    print('%d的阶乘是:%d' % (n, sum1))

    end = time.time()
    print('函数执行时间: %fs' % (end - start))


factorial(5)


# ==============方法二:====================


# 注意: 这个add_time只能给没有参数的函数添加统计执行时间的功能
def add_time(fn):
    # fn=func1
    start = time.time()
    fn()  # func1()
    end = time.time()
    print('函数执行时间: %fs' % (end - start))


def add_time2(fn, *args, **kwargs):
    start = time.time()
    fn(*args, **kwargs)
    end = time.time()
    print('函数执行时间: %fs' % (end - start))


def func1():
    print('=======')
    print('+++++++')


def func2():
    print('你好世界!')
    print('你好python~')


def func3(x, y):
    print('%d+%d=%d' % (x, y, x+y))


add_time(func1)
add_time(func2)
add_time2(func1)

# func3(10, 20)
add_time2(func3, 10, 20)


# 2.装饰器
print('========================装饰器================')
"""
无参装饰器的函数:
def 函数名1(参数1):
    def 函数名2(*args, **kwargs):
        result = 参数1(*args, **kwargs)
        新功能对应的代码段
        return result
    return 函数名2
    
说明: 
函数名1  -  装饰器的名字;一般根据需要添加的功能命名
参数1 - 需要添加功能的函数， 一般命名为fn
函数名2  -  随便命名, 可以用test
"""


# 添加统计函数执行时间的装饰器对应的函数
def add_time3(fn):

    def test(*args, **kwargs):
        start = time.time()
        re = fn(*args, **kwargs)
        end = time.time()
        print('函数执行时间: %fs' % (end - start))
        return re

    return test


@add_time3
def func5():
    print('你好吗')


func5()


@add_time3
def sum3(x, y, z):
    print(x+y+z)


sum3(1, 2, 3)


# 练习: 给所有返回值是整数的函数添加功能: 返回值以16进制形式的数据返回
def add_hex(fn):
    def test(*args, **kwargs):
        re = fn(*args, **kwargs)
        # type(re) == int
        # 判断re是否是整型
        if isinstance(re, int):
            return hex(re)
        return re
    return test


@add_hex
def yt_sum(x, y):
    return x+y


print(yt_sum(10, 20))


@add_hex
def print_star():
    print('******')


print(print_star())