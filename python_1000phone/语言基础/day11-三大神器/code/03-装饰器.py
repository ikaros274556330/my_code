"""__author__==吴佩隆"""

import time


# 1.什么是装饰器
"""
装饰器本质是一个函数 = 返回值高阶函数 + 实参高阶函数 + 糖语法
装饰器是python的三大神器之一:装饰器,迭代器,生成器
作用:给已经写好的函数添加功能
"""

# 给函数添加一个功能:统计函数的执行时间


# 方法一:在每个需要添加功能的函数中加入相应的代码
def sum_w(x, y):
    start = time.time()  # 获取当前时间
    sum1 = x+y
    print(sum1)
    end = time.time()
    print('函数执行时间:%fs' % (end - start))


sum_w(100, 200)


def factorial(n):
    start = time.time()

    num1 = 1
    for num in range(1, n+1):
        num1 *= num
    print('%d的阶乘是:%d' % (n, num1))
    end = time.time()
    print('执行时间是:%fs' % (end-start))


factorial(5)


# 方法二:

# 注意:这个add_time只能给没有参数的函数添加统计时间的功能
def add_time(fn):
    # fn = func1
    start = time.time()
    fn()
    end = time.time()
    print('函数执行的时间:%fs' % (end - start))


def add_time2(fn, *args, **kwargs):
    start = time.time()
    fn(*args, **kwargs)

    end = time.time()
    print('函数执行的时间:%fs' % (end - start))


def func1():
    print('===========')
    print('-----------')


def func2():
    print('你好世界')
    print('你好python')


def func3(x, y):
    print('%d+%d=%d' % (x, y, x+y))


add_time(func1)
add_time(func2)
add_time2(func1)

# func3(10, 20)
add_time2(func3, 10, 20)


# 2.装饰器
print('===========================================')
"""
无参装饰器
def 函数名1(参数1):
    def 函数名2(*args, **kwargs):
        参数1()
        新功能对应的代码段
    return 函数名2
    
说明:
函数名1 - 装饰器的名字 - 一般根据需要添加的功能命名
参数1 - 需要添加功能的函数,一般命名fn
函数名2 - 随便命名, 可以用test
"""


def add_time3(fn):
    def test(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print('函数执行的时间:%fs' % (end - start))

    return test


@add_time3
def func5():
    print('你好吗')


func5()


# 练习:给所有返回值是整数的函数添加功能;返回值以16进制形式的数据返回

def hex_1(fn):
    def test(*args, **kwargs):
        a = fn(*args, **kwargs)
        if isinstance(a, int):
            return hex(a)
        return a

    return test


@hex_1
def t_sum(x, y):
    return x+y


print(t_sum(10, 20))