"""__author__=余婷"""


# 1.为函数写一个装饰器，在函数执行之后输出 after
def print_after(fn):
    def test(*args, **kwargs):
        re = fn(*args, **kwargs)
        print('after')
        return re
    return test


# 2.实现tag装饰器
def tag(fn):
    def test(*args, **kwargs):
        re = fn(*args, **kwargs)
        return '<p>'+str(re)+'</p>'
    return test


@tag
def func1(x):
    return x


print(func1(120))


# 4.写一个装饰器@tag要求满足如下功能(需要使用带参的装饰器，自己先自学挣扎一下):
def tag(name):
    def test1(fn):
        def test2(*args, **kwargs):
            re = fn(*args, **kwargs)
            return '<{0}>{1}</{0}>'.format(name, re)
        return test2
    return test1


@tag(name='h1')
def func1(x):
    return x


print(func1('你好!'))