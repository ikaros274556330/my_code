"""__author__=吴佩隆"""
# 1.continue

"""
continue是循环体中的关键字
当执行循环体的时候，如果遇到continue，结束当次循环，直接进入下一次
"""

for x in range(4):
    print('hello')
    if x % 2 == 0:
        continue
    print('Hi')

# 2.break

"""
break是循环体中的关键字
当执行循环体的时候，如果遇到break，整个循环直接结束
"""

print('=======================')
for x in range(4):
    print('===')
    break
    print('+++')

# 功能:不断输入数字直到输入为0，求出所有奇数的和
sum1 = 0
while True:
    value = int(input('请输入数字:'))

    if value == 0:
        break

    if value % 2 == 0:
        continue
    sum1 += value

print(sum1)

# 3.else

"""
1)完整的for循环
for 变量 in 序列:
    循环体
else:
    代码段
    
2)完整的while循环
while 条件:
    循环体
else:
    代码段

else中的代码段:当循环自然结束的时候就执行，如果是break强制打断则不执行

else的意义:可以通过判断else中的代码有没有执行来判断有没有遇到break
"""

print('======================')

for x in range(4):
    print(x)
    if x == 2:
        break
else:
    print('else')