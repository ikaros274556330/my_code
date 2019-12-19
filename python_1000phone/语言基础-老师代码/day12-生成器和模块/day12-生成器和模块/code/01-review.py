"""__author__=余婷"""
"""
1.函数就是变量: 声明函数就是声明类型是function的变量，函数名是变量名
（普通变量能做的事情函数都可以做）

2.实参高阶函数：一个函数的参数是函数
系统实参高阶函数的使用: 列表.sort()、sorted()、max()、min()
参数key赋值: 1)函数  2)有一个参数->代表序列中的每个元素  3)需要一个返回值 -> 比较大小标准

3.返回值高阶函数：一个函数的返回值是函数
4.装饰器: 给函数添加功能
装饰器 = 实参高阶函数+返回值高阶函数+糖语法
无参的装饰器:
def 装饰器名(fn):
    def 添加功能的函数(*args, **kwargs):
        # 保留原函数的功能
        re = fn(*args, **kwargs)
        实现添加新功能的代码
        return re
    return  添加功能的函数
    
使用无参装饰器:  声明函数前加 - @装饰器名

有参装饰器:
def 装饰器名(装饰器参数列表):
    def test1(fn):
        def test2(*args, **kwargs):
            # 保留原函数的功能
            re = fn(*args, **kwargs)
            实现添加新功能的代码
            return re
        return  test2
    return test1

"""


# 0.装饰器
def add_value(fn):
    def test(*args, **kwargs):
        re = fn(*args, **kwargs)
        if type(re) == int or type(re) == float:
            return re+100
        return re
    return test


def new_add_value(char, value):
    def test1(fn):
        def test2(*args, **kwargs):
            re = fn(*args, **kwargs)
            if isinstance(re, int) or isinstance(re, float):
                if char == '-':
                    return re - value
                else:
                    return re + value
            else:
                return re
        return test2
    return test1


@new_add_value('-', 10)
def yt_sum(x, y):
    return x + y


print(yt_sum(10, 20))
# print(yt_sum('abc', '123'))


# 1.函数作为变量
def func1(x, y):
    print(x, y)
    return 100


list1 = [func1, func1(10, 20)]
list1[0](100, 200)
print(list1[1]*3)


# 2.实参高阶函数
# test2是实参高阶函数
def func2(fn, m, n):
    return fn(m) * n


def test(x: int):
    return x+30


print(func2(test, 10, 3))


def func(x):
    # return x % 10
    sum1 = 0
    for num in str(x):
        sum1 += int(num)
    return sum1


print(max([124, 36, 82], key=func))


# 3.返回值高阶函数
def func3():
    def func4(x):
        return x*2

    return func4


print(func3()(100))


# func5是闭包
def func5():
    a = 100

    def func6(x):
        print(a+x)   # 200

    return func6


t = func5()
print(t(100))   # None
