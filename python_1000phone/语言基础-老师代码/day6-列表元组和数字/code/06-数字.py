"""__author__=余婷"""
import math     # 数学模块 - 提供数学相关方法和数据
import cmath    # 和复数相关的数学模块

# python中和数字相关的类型: 整型(int)、浮点型(float)、布尔(bool)、复数(complex)
# 1.整型(int)  - 所有整数对应的类型(python2.x整型除了int还有long)；支持2进制、8进制和16进制的表示方式
# int(数据)  -  将指定的数据转换成整数;
#              1）所有的浮点数和布尔都可以转换成整型
#              2）字符串, 字符串去掉引号后本身是一个整数
print(int(12.5))     # 12
print(int(-12.5))    # -12
print(int(True), int(False))   # 1 0
# print(int('abc'))    # ValueError: invalid literal for int() with base 10: 'abc'
# print(int('123bn'))    # ValueError: invalid literal for int() with base 10: '123bn'
# print(int('12.5'))     # ValueError: invalid literal for int() with base 10: '12.5'
print(int('12'))     # 12
print(int('-20'))    # -20

# 2.浮点型(float)  -  所有带小数点的数对应的类型; 支持科学计数法: 3e4 == 3*10**4
# float(数据)  - 将指定的数据转换成浮点数
#               1）所有的整数和布尔都可以转化成浮点
#               2）字符串去掉引号后本身就是一个数字
print(3e4)
# 0.00001
print(1e-5 + 1)
# 6.7  ~ 6.69999999999999998
# 6.1  ~ 6.10000000000000002
print(float(100))       # 100.0
print(float('123'))     # 123.0
print(float('13.5'))    # 13.5
print(float('2e3'))     # 2000.0


# 3.布尔(bool)  -  只有True和False; True本质就是1，False本质就是0
# bool(数据)   -  将指定数据转换成布尔值；
#                不管什么类型的数据都能转换成布尔, 所有为零为空的值会转换成False,其他都是True
print(True == 1)    # True
print(True + 1)     # 2
print(False + 10)   # 10
print(False * 3)    # 0
print(bool(0), bool(0.0), bool(''), bool([]), bool(()), bool(None))   # False False False False False False
print(bool(' '))   # True
list1 = []
if list1:
    print('list1不为空')

if not list1:
    print('list1为空')

num = 13
if num & 1:
    print('奇数')

if num & 1 == 0:
    print('偶数')


# 4.复数(complex)  -  由实部和虚部组成的数就是复数, 实部+虚部j; python直接支持复数运算
# 注意: 如果虚部是1，这个1不能省
c1 = 10 + 2j
c2 = 5 - 3j
print(c1 + c2)    # 15 - 1j
print(c1 - c2)    # 5 + 5j
print(c1 * c2)    # 56-20j


# 5.数学模块
# 求绝对值
print(math.fabs(-20))    # 20.0
print(abs(-12))     # 12
print(abs(-12.5))   # 12.5








