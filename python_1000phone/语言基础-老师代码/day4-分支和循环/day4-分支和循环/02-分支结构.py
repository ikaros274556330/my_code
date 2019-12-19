"""__author__=余婷"""

# 1. if-elif-else结构
"""
1)语法:
if 条件语句1:
    代码段1
elif 条件语句2:
    代码段2
elif 条件语句3:
    代码段3
...
else:
    代码段N
其他语句

2) 执行过程:
先判断条件语句1是否为True,为True就执行代码段1，然后整个if-elif-else结构结束；
如果为False,就判断条件语句2是否为True, 为True就执行代码段2，然后整个if-elif-else结构结束；
如果是False,就判断条件语句3是否为True, 为True就执行代码段3，然后整个if-elif-else结构结束；
以此类推
如果所有的条件语句都不成立，执行else后面的代码段
"""

# 根据年龄范围打印: 少年(14以下)、青年(14~25)、壮年(26~35)、中年(36 ~ 50)、老年(50以上)
age = 30

if age < 14:
    print('少年')
elif age <= 25:
    print('青年')
elif age <= 35:
    print('壮年')
elif age <= 50:
    print('中年')
else:
    print('老年')


# 2.if嵌套
"""
if结构中的代码块中可以再出现其他的if语句
"""
# 判断一个数是否是偶数，并且再判断这个数是否是4的倍数；并打印出结论
num = 13

# 方法一:
if num & 1 == 0:
    print('偶数')
else:
    print('奇数')

if num % 4 == 0:
    print('是4的倍数!')

# 方法二:
print('====================')
if num & 1 == 0:
    print('偶数')
    if num % 4 == 0:
        print('是4的倍数!')
        print('++++')
else:
    print('奇数')
    if num % 10 == 3:
        print('个位数是3')


# if age < 14:
#     print('少年')
#
# if 14 <= age <= 25:
#     print('青年')
#
# if 25 < age <= 35:
#     print('壮年')

