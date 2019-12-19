"""__author__=余婷"""

# 循环嵌套: 外面的循环执行一次，里面的循环要执行完
for x in range(3):
    for y in range(4):
        print(x, y)
"""
x = 0: 
    y = 0: print(0, 0)
    y = 1: print(0, 1)
    y = 2: print(0, 2)
    y = 3: print(0, 3)
x = 1:
    y = 0: print(1, 0)
    y = 1: print(1, 1)
    y = 2: print(1, 2)
    y = 3: print(1, 3)
...

0 0
0 1
0 2
0 3
1 0
1 1
1 2
1 3
2 0
2 1
2 2
2 3
"""

# 计算1!+2!+3!+...+10!
# N! = 1*2*3*4*...*N

# 方法一:
sum1 = 0
# 将1~10取出来
for num in range(1, 11):
    # 计算取出来的数的阶层
    sum2 = 1
    for x in range(1, num+1):
        sum2 *= x
    # 将阶乘值加起来
    sum1 += sum2
    print(sum2)

print(sum1)

# 方法二:
sum1 = 0
sum2 = 1
for num in range(1, 11):
    sum2 *= num
    sum1 += sum2

print(sum1)
"""
sum1 = 0
sum2 = 1

num = 1: sum2 = sum2 * num = 1*1; sum1 += sum2 = sum1 + sum2 -> sum1 = 1
num = 2: sum2 = sum2 * num = 1*2; sum1 = 1 + 2!
num = 3: sum2 = sum2 * num = 1*2*3; sum1 = 1+2!+3!
...
num = 10: sum2 = 1*2*3*..*10; sum1 = 1+2!+3!+...+10!


"""