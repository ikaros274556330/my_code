"""__author__=吴佩隆"""
"""
1.函数就是变量:声明函数就是声明类型是function的变量
（普通变量能做的事情函数都可以做）
 
2.实参高阶函数：一个函数的参数是函数
系统实参高阶函数的使用：列表.sort()、sorted()、max()、min()
参数key赋值:1)函数 2)有一个参数 -> 代表序列中的每个元素 3)需要一个返回值

3.返回值高阶函数：一个函数的返回值是函数

4.装饰器：给函数添加功能
装饰器 = 实参高阶函数+返回值高阶函数+糖语法
无参装饰器：
def 装饰器名(fn):
    def 添加功能的函数(*args, **kwargs):
        # 保留原函数的功能
        re = fn(*args, **kwargs)
        实现添加功能的代码
        return 返回值
    return 添加功能的函数名


有参装饰器:
def 装饰器名字(装饰器参数列表):
    def test1(fn):
        def test2(*args, **kwargs):
            # 原函数功能
            re = (*args, **kwargs)
            实现添加功能的代码
            return re
        return test2
    return test1
"""


