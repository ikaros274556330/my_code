"""__author__=余婷"""
from random import randint


# 1.while循环
"""
1)语法:
while 条件语句:
    循环体

2)说明
while    -     关键字；固定写法
条件语句  -     任何有结果的表达式；数据、已经声明过的变量、运算符表达式(不能是赋值语句)等
:        -     固定写法
循环体    -     和while保持一个缩进的一条或者多条语句;(需要重复指定的语句)

3)执行过程:
先判断条件语句是否True,如果为True就执行循环体；执行完循环体再判断条件语句是否为True,
为True又执行循环体，以此类推，直到条件语句的结果是False循环就结束
"""
num = 0
while num < 5:
    print('=====')
    num += 1


# 2.for循环和while的选择
"""
1)什么时候使用for循环
a.循环次数确定的时候
b.遍历序列

2)什么时候使用while循环
a.死循环
b.循环次数不确定的时候
"""
# 不断输入数字，直到输入的值是0为止
value = 1
while value != '0':
    value = input('请输入数字:')

# 练习: 猜数字游戏
# 游戏开始的时候随机产生一个100以内数字，不断输入数字，直到输入的数字和产生的数字一致，游戏就结束;
# 在没有猜对的时候，给出'大了'或者'小了'的提示
number = randint(0, 100)    # 产生0~100的随机数，并且保存在number
value = -1
while value != number:
    value = int(input('请输入一个数:'))
    if value < number:
        print('小了')
    elif value > number:
        print('大了')

print('游戏结束!', number, value)
