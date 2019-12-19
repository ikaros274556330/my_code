"""__author__=余婷"""

# 1.读程序
# 1）
numbers = 1
for i in range(0, 20):
    numbers *= 2
print(numbers)

"""
numbers = 1
i = 0 ~ 19, 循环20次
i = 0:  numbers *= 2 -> numbers = numbers * 2 = 1 * 2 = 2 = 2^1 
i = 1:  numbers *= 2 -> numbers = numbers * 2 = 2 * 2 = 4 = 2^2
i = 2:  numbers *= 2 -> numbers = numbers * 2 = 4 * 2 = 8 = 2^3
...
i = 19: numbers *= 2 -> numbers = numbers * 2 = 2^20

结论: 计算2的20次方
"""
# 2）
summation = 0
num = 1
while num <= 100:
    if (num % 3 == 0 or num % 7 == 0) and num % 21 != 0:
        summation += 1
    num += 1
print(summation)
# print(num)

"""
num = (1, 2, 3, 4, ..., 99, 100), 101
总结: 统计1~100中能被3或者7整除但是不能同时被3和7整除的数的个数
"""

# 1.求1到100之间所有数的和、平均值
# 方法一:
sum1 = 0
count = 0
for num in range(1, 101):
    sum1 += num
    count += 1
print('和:', sum1, '平均值:', sum1 / count)

# 方法二:
num = 1  # 计算数字
sum1 = 0  # 和
count = 0  # 个数
while num <= 100:
    sum1 += num  # 求和
    count += 1  # 统计个数
    num += 1  # 控制num取一下数字
print('和:', sum1, '平均值:', sum1 / count)

# 2.计算1-100之间能3整除的数的和
# 方法1：
sum1 = 0
for num in range(3, 101, 3):
    sum1 += num
print('第2题和:', sum1)

# 方法:
num = 0
sum1 = 0
while num <= 100:
    sum1 += num
    num += 3
print('第2题和:', sum1)

# 3. 计算1-100之间不能被7整除的数的和
# 方法一:
sum1 = 0
for num in range(100, 0, -1):
    if num % 7 != 0:
        sum1 += num
print('第3题和:', sum1)

# 方法二:
num = 100
sum1 = 0
while num >= 1:
    if num % 7 != 0:
        sum1 += num
    num -= 1
print('第3题和:', sum1)

# 控制while循环产生数字序列
"""
产生的数字范围是M ~ N (M < N), step是步长(正)
# 方法一: 升序
num = M
while num <= N:
    每次循环要做的事情
    num += step

# 方法二: 降序
num = N
while N >= M:
    每次循环要做的事情
    num -= step
"""
# 1. 求斐波那契数列中第n个数的值：1，1，2，3，5，8，13，21，34....
# 规律: 前两个数是1，从第三个数开始，每个是它前两个数的和
n = 3
pre_1 = 1
pre_2 = 1
if n == 1 or n == 2:
    print('当前数是: 1')
else:
    for _ in range(n - 3):
        # python写法:
        pre_1, pre_2 = pre_2, pre_1 + pre_2
        # java/c的写法
        # t = pre_1
        # pre_1 = pre_2
        # pre_2 = t + pre_2

    print('当前数是:', pre_1 + pre_2)

# 补充: 交换两个变量的值
# python写法:
a = 10
b = 20
a, b = b, a  # a, b = 20, 10
print(a, b)

# java/c写法
a = 10
b = 20
t = a
a = b
b = t
print(a, b)

# 2. 判断101-200之间有多少个素数，并输出所有素数
# 素数就是质数: 除了1和这个数本身，不能再被其他数整除。这样数就是质数

# 方法一:
count = 0
# 取出101~200之间的所有的数
for num in range(101, 200, 2):
    # 判断num取出来的这个数是不是素数: 判断2~num-1之间有没有数能去整除的
    for x in range(2, int(num**0.5+1)):
        if num % x == 0:
            # print(num, '不是素数')
            break
    else:
        # print(num, '是素数')
        count += 1
print('101-200之间素数的个数:', count)

# 方法二:
for num in range(101, 200, 2):
    flag = True  # 假设当前取出来的这个数是素数
    for x in range(2, int(num**0.5+1)):
        if num % x == 0:
            flag = False
            break

    if flag == True:
        print(num, '是素数!')


# 3.打印出所有的⽔仙花数,所谓⽔仙花数是指⼀个三位数，其各位数字⽴⽅和等于该数本身。例如：153是
# ⼀个⽔仙花数,因为153 = 1^3 + 5^3 + 3^3
for num in range(100, 1000):
    ge = num % 10
    shi = num // 10 % 10   # shi = num % 100 // 10
    bai = num // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == num:
        print(num, '是水仙花数')


# 4.有⼀分数序列：2/1,3/2,5/3,8/5,13/8,21/13...求出这个数列的第20个分数
# 分子: 前一个分数的分子+前一个分数的分母
# 分母: 前一个分数的分子
n = 4
fen_zi = 2
fen_mu = 1
for _ in range(n-1):
    fen_zi, fen_mu = fen_zi + fen_mu, fen_zi
print('当前分数:', fen_zi, '/', fen_mu)

# 5.给⼀一个正整数，要求:1、求它是几位数 2.逆序打印出各位数字
# 123 -> 123 // 10 -> 12 // 10 -> 1 // 10 -> 0
# 7236 -> 7236 // 10 -> 723 // 10 -> 72 // 10 -> 7 // 10 -> 0
num = 345
count = 0
while True:
    # 倒序取出每一位
    print(num % 10, end='')

    num //= 10
    # 统计位数
    count += 1
    if num == 0:
        break
print()
print(count, '位数')








