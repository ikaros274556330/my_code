"""__author__=吴佩隆"""

from random import randint
# 1.while循环

"""
1)语法:
while 条件:
    循环体
    
2)说明
while   -   关键字；固定写法
条件语句  -   任何有结果的表达式都可以；数据、已经声明过的变量、运算表达式(赋值语句除外)
:       -   固定写法
循环体   -   和while保持一个缩进的一条或者多条语句；(需要重复执行的语句)

3)执行过程:
先判断条件语句是否为True，为True就执行循环体，然后再判断条件是否为True...依次类推，
直到条件为False循环结束
"""
num = 0
while num < 5:
    print('====')
    num += 1

# 2.for循环和while的选择

"""
1)什么时候用for循环
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

# 练习:猜数字游戏
# 游戏开始的时候随机产生一个100以内的数字，直到猜对结束
# 没猜对给出相应提示

number = randint(0, 100)

answer = -1

while answer != number:
    answer = int(input('请输入你的答案:'))
    if answer > number:
        print('大了')
    elif answer < number:
        print('小了')
    elif answer == number:
        print('对了，答案就是', number)


