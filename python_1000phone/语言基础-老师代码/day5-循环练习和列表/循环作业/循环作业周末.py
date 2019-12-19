"""__author__=余婷"""

# 1.一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆朗玛峰的高度（8848.13米）？
# 循环次数不确定，使用while循环; 每次对折后的高度是原来厚度的2倍
count = 0  # 保存次数
height = 0.08
while True:
    height *= 2
    count += 1
    if height >= 8848.13:
        break
print('对折%d次' % count)

# 3. 将一个正整数分解质因数。例如:输入90,打印出90=2x3x3x5。
factor = 2  # 保存因数
num = 90
print(num, '=', end='')
while num != 1:
    while num % factor == 0:
        num //= factor
        if num != 1:
            print(factor, '+', end='')
        else:
            print(factor)
            break
    factor += 1


# 4. 输入两个正整数m和n，求其最大公约数和最小公倍数。 程序分析：利用辗除法。
m = 90
n = 35
# 先保证m中保存两个数中较小的那个数
if m > n:
    m, n = n, m

# 求最大公约数
if n % m == 0:
    print('m和n的最大公约数为:', m)
else:
    for num in range(m-1, 1, -1):
        if m % num == 0 and n % num == 0:
            print('m和n的最大公约数为:', num)
            break
    else:
        print('m和n的最大公约数为:', 1)


# 5. 一个数如果恰好等于它的因子之和，这个数就称为 "完数 "。例如6=1＋2＋3.  编程 找出1000以内的所有完数
