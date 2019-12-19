"""__author__=吴佩隆"""
# 1. if-elif-else结构

"""
1)语法:
if 条件1:
    代码1
elif 条件2:
    代码2
elif 条件3:
    代码3
...
else:
    代码N
    
2)执行过程:
判断1是否为True,如果是则执行1,整个if-elif-else结构结束:
如果1为False,判断2,依次类推
如果所有elif都不成立,执行else
"""

# 根据年龄范围打印:少年(~14)、青年(14~25)、壮年(26~35)、中年(36~50)、老年(50~)
age = 26
if age < 14:
    print('少年')
elif age <= 25:    # 因为上级条件没执行，所以可以省略上级条件
    print('青年')
elif age <= 35:
    print('壮年')
elif age <= 50:
    print('中年')
elif age > 50:
    print('老年')

# 2. if嵌套

"""
if结构中可以再出现其他if语句
"""

# 判断一个数是否为偶数,并且再判断这个数是否是4的倍数;并打印结论
num = 13
if num & 1 == 0:
    print('偶数')
    if num % 4 == 0:
        print('4的倍数')
else:
    print('奇数')
    if num % 10 == 3:
        print('个位数是3')
