"""__author__==吴佩隆"""

import time

"""
1.为函数写一个装饰器，在函数执行之后输出 after
"""


# def after(fn):
#     def test(*args, **kwargs):
#         fn(*args, **kwargs)
#         print('after')
#
#     return test
#
#
# @after
# def func1():
#     pass
#
#
# func1()


"""
2.为函数写一个装饰器，把函数的返回值 +100 然后再返回。
"""


# def add_100(fn):
#     def test(*args, **kwargs):
#         a = fn(*args, **kwargs)
#         return a + 100
#     return test
#
#
# @add_100
# def a_number():
#     return 100
#
#
# print(a_number())


"""
3.写一个装饰器@tag要求满足如下功能:
@tag
def render(text):
    # 执行其他操作
    return text

@tag
def render2():
    return 'abc'

print(render('Hello'))   # 打印出: <p>Hello</p>
print(render2())     # 打印出: <p>abc</p>
"""


# def tag(fn):
#     def test(*args, **kwargs):
#         text1 ='<p>' + fn(*args, **kwargs) + '<p/>'
#         return text1
#     return test
#
#
# @tag
# def render(text):
#     # 执行其他操作
#     return text
#
#
# @tag
# def render2():
#     return 'abc'
#
#
# print(render('Hello'))
# print(render2())


"""
4.写一个装饰器@tag要求满足如下功能(需要使用带参的装饰器，自己先自学正在一下):
@tag(name='p')
def render(text):
    # 执行其他操作
    return text

@tag(name='div')
def render2():
    return 'abc'

print(render('Hello'))   # 打印出: <p>Hello</p>
print(render2())     # 打印出: <div>abc</div>
"""


# def tag(name=None):
#     def test(fn):
#         def test1(*args, **kwargs):
#             text1 = ('<{}>' + fn(*args, **kwargs) + '<\{}>').format(name, name)
#             return text1
#         return test1
#     return test
#
#
# @tag(name='p')
# def render(text):
#     # 执行其他操作
#     return text
#
#
# @tag(name='div')
# def render2():
#     return 'abc'
#
#
# print(render('Hello'))
# print(render2())


"""
5.为函数写一个装饰器，根据参数不同做不同操作。
"""


def tag(flag='X'):
    def test1(fn):
        def test2(*args, **kwargs):
            if flag == 'X':
                return fn(*args, **kwargs)
            return fn(*args, **kwargs) + 100 if flag else fn(*args, **kwargs) - 100
        return test2
    return test1


@tag(flag=True)
def func1():
    return 500


@tag(flag=False)
def func2():
    return 500


@tag()
def func3():
    return 500


print(func1())
print(func2())
print(func3())


# start = time.time()
# a = [i for i in range(10000000)]
# b = []
# for i in a:
#     if i % 3 == 0:
#         b.append(i)
# end = time.time()
# print('用时%.4f' % (end-start))
