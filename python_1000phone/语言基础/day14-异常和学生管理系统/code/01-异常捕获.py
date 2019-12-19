"""__author__=吴佩隆"""

# 1异常：程序在运行过程中报错就叫异常；ValueError、IndexError等
# 当程序出现异常的时候程序直接结束，不会执行后续代码

# print(int('abc'))   #ValueError: invalid literal for int() with base 10:
# print([1,2][10])    #IndexError: list index out of range

# 2.异常捕获:让程序出现异常的时候不崩溃，程序可以继续执行
"""
1)什么时候需要捕获异常：明知道某个位置可能会出现异常，但程序员没办法控制的时候
2)怎么捕获异常

语法一: 捕获任意可以捕获的异常

try:
    代码块1    (需要捕获异常的代码)
except:
    代码块2    (出现异常后对异常进行的处理)

执行过程:先尝试执行1，1报异常执行2。
        如果代码1中没有出现异常，直接执行后面


语法二: 捕获指定的一种异常
try:
    代码1:
except 异常类型:
    代码2
finally:
    代码块3
    
执行过程:先尝试执行1，1出异常，检查异常类型与except后类型是否一致
一致执行代码2，不一致程序崩溃

语法三: 捕获多种异常，对不同进行相同处理
try:
    代码块1
except (异常类型1，异常类型2....)
    代码块2
finally:
    代码块3

语法四:捕获多种，分开处理
try:
    代码块1
except 异常类型1:
    代码块11
except 异常类型2:
    代码块22
except 异常类型3:
    代码块33
finally:
    代码块3

"""

# 3.关键字finally
"""
所有异常捕获结构的最后都可以添加一个finally
try中代码出现任何情况finally后都会执行
"""

try:
    print([1, 2][10])
except IndexError:
    print('报错')

print('==========语法2============')


try:
    print(int('abc'))
    print([1, 2][10])
except (ValueError, IndexError) as c:
    print(c)

print('===========finally============')

try:
    print({'name': '张三', 'age': 18}['Alice'])

except KeyError:
    print('出错')

finally:
    print('遗言！~')

# raise ValueError  主动抛出异常
