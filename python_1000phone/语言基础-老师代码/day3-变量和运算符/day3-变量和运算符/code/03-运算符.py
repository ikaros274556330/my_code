"""__author__=余婷"""

# python支持的运算符: 数学运算符、比较运算符、逻辑运算符、赋值运算; 位运算
print('===================数学运算符======================')
# 1.数学运算符: +、-、*、/、%、//、**
# 1）+、-、*、/ 和小学数学中的加(+)、减(-)、乘(×)、除(÷)的功能一模一样
print(1+1)
print(20-10)
print(20 * 10)
print(5/2)

# 2) %  - 求余数(取余/取模)
print(5 % 2)
print(10 % 4)

# 应用1： 判断整数的奇偶性 - 判断这个数对2取余的结果是否是0
print(20 % 2)
print(23 % 2)

# 应用2：是否整除 - 判断余数是否为0
# 应用3：取低位数，例如，获取一个整数个位数 - 数字%10
num = 123
print(num % 10)    # 3
print(num % 100)   # 23

# 3) //  - 整除(商只取整数部分)
# 注意: 负数整除除不尽的时候向下整！！！ -5 // 2 == -3
print(5//2)   # 2
print(3.9 // 3)   # 1.0

# 应用: 取高位
print(num // 100)   # 1

# 4) **  - 幂运算；x ** y -- 求x的y次方
print(2 ** 3)
print(16 ** (1/2))
print(8 ** (1/3))

result = 3 ** 4
print(result)

print('=====================比较运算符=========================')
# 2.比较运算符: >、<、==、!= 、>=、<=
"""
注意: 所有的比较运算的运算结果都是布尔值
"""
# 1) >, <, >=, <= 和数学中的>、<、≥、≤是一样的
print(10 > 20)    # False
print(10 < 20)    # True
print(30 >= 20)   # True
print(30 >= 30)   # True

# 2) == - 判断两个值是否相等, !=  - 判断两个值是否不相等
print(10 == 10)    # True
print(10 != 10)    # False

# 3) python可以像数学一样用比较运算符连写的方式表示范围(C/Java/JS等不可以)
age = 30
print(18 < age < 28)

print('=====================逻辑运算符=========================')
# 3.逻辑运算符: and(与)、or(或)、not(非)
# 逻辑运算符的运算对象和结果一般都是布尔值
# 1)and
"""
运算规则: 两个都是True结果才是True，只要有一个是False结果就是False
True and  True  -> True
True and  False  -> False
False and  True  -> False
False and  False  -> False
使用场景: 需要多个条件同时满足的时候，就用and; 相当于生活中的并且
"""
gpa = 4.5
score = 98

# 获取奖学金的条件: 绩点不低于4并且操评分高于95
print('是否能够获取奖学金:', gpa >= 4 and score > 95)

# 练习: 判断一个数是否能够同时被3和7整除
num = 21
print('是否能够同时被3和7整除:', num % 3 == 0 and num % 7 == 0)
print('是否能够同时被3和7整除:', num % 21 == 0)

# 2) or
"""
运算规则: 两个都是False结果才是False, 只要有一个是True结果就是True
True or True  -> True
True or False  -> True
False or True  -> True
False or False  -> False
使用场景: 需要多个条件中有一个条件满足就行，就使用or；相当于生活中的or
"""
gpa = 4.5
score = 98
# 获取奖学金的条件: 绩点不低于4或者操评分高于95
print('是否获取奖学金:', gpa >= 4 or score > 95)

# 3) not
"""
运算规则: True变False， False变True
not True  -> False
not False -> True
使用场景: 对某一个条件进行否定
"""
num = 21
# 一个数不能同时被3和7整除的条件
print('不能同时被3和7整除:', not (num % 3 == 0 and num % 7 == 0))
print((num % 3 != 0 and num % 7 != 0) or (num % 3 == 0 and num % 7 != 0) or (num % 7 == 0 and num % 3 != 0))

# 4) 短路操作
"""
and的短路操作: 条件1 and 条件2  -> and前面的那个条件如果结果是False，那么后面的条件语句不会执行，结果直接是False
or的短路操作: 条件1 or 条件2  -> or前面的那个条件如果结果是True,那么后面的条件语句不会执行，结果直接是True
"""


def func1():
    print('函数被执行了')
    return True


False and func1()
True or func1()


# 4.赋值运算符: =, +=, -=, *=, /=, %=, //=, **=
"""
所有的赋值运算符的左边必须是变量; 组合赋值运算符的左边除了是变量，这个变量还必须是已经声明过的
"""
# 1) 变量 = 值   -> 将右边的值赋给左边的变量
a = 10
b = 10 * 2
c = a
d = a + b
a = 100

# 2)组合赋值运算符
# 变量 += 值  ->  变量 = 变量 + 值
# aa += 10    # NameError: name 'aa' is not defined
bb = 100
bb += 10      # bb = bb + 10; bb = 100 + 10; bb = 110
print(bb)

bb -= 20      # bb = bb - 20; bb = 110 - 20; bb = 90
print(bb)

bb *= 4/2     # bb *= 2.0; bb = bb * 2.0; bb = 90 * 2.0; bb = 180.0
print(bb)

bb %= 2       # bb = bb % 2; bb = 180 % 2; bb = 0
print(bb)

# 5.运算顺序
"""
运算符优先级:
数学运算符 > 比较运算符 > 逻辑运算符 > 赋值运算符(最低)
数学运算符的优先级和数学一样: ** > *,/,//,% > +,-
如果有括号，先算括号里面的
"""














