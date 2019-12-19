"""__author__=余婷"""

# 1.什么是函数
"""
1)函数的定义
函数就是对实现某一特定功能的代码的封装

2)函数的分类
系统函数 - 系统(语言系统)已经声明好，程序员可以直接使用的函数(别人造好的机器). 例如:print、input、hex、bin、oct、chr、ord...
自定义函数 - 开发者自己声明的函数(自己造机器).
"""
# 2.函数的声明(定义函数) - 造机器
"""
1)语法:
def 函数名(参数列表):
    函数说明文档
    函数体 

2)说明
def   -   关键字;固定写法
函数名  -  和变量的要求一样（机器名）
():     -  固定写法
参数列表 -  这儿的参数又叫形参; 以'参数名1,参数名2,参数名3,...'的形式存在, 参数名其实就是变量名
           作用: 将函数外面的数据传到函数里面
函数说明文档  -  本质就是一段注释; 必须在第一行有效当代码的前面, 需要使用三个双引号引起来（机器的说明书）
函数体  -   和def保持一个缩进的一条或者多条语句；实现函数功能代码
    
3)初学者声明函数的步骤
a.确定函数的功能
b.根据函数的功能确定函数名
c.确定参数(形参), 看实现函数的功能需不需要额外的数据, 需要几个就设置几个形参
d.实现函数的功能
e.写说明文档


注意: 声明函数的时候不会执行函数!!（重要!）
"""


# 1).声明一个函数，打印两个数的和
def yt_sum(num1, num2):
    """
    （函数功能说明区）求两个数的和
    :param num1: 提供第一个数；数字
    :param num2: 提供第二个数；数字
    :return: (返回值)
    """
    # num1=10; num2=20
    print(num1 + num2)    # print(10+20)  print(30)


# 2).声明一个函数，求N!
def factorial(n):
    """
    求N的阶乘
    :param n: 数字N的值
    :return: None
    """
    # n=5; n=10
    sum1 = 1
    for x in range(1, n+1):
        sum1 *= x
    print('%d的阶乘是:%d' % (n, sum1))


# 3.函数的调用(使用机器)
"""
1)语法:
函数(实参列表)

2)说明
函数  -  已经声明的函数
()    -  固定写法
实参列表  -  多个数据用逗号隔开; 需要传递到函数中使用的具体的数据, 用来形参赋值的

3)函数的调用过程(非常重要)
a.回到函数声明的位置
b.传参 - 用实参给形参赋值(必须保证每个形参都有值)
c.执行函数体
d.确定返回值
e.回到函数调用的位置，接着往后执行
"""
yt_sum(10, 20)
factorial(5)
factorial(10)










