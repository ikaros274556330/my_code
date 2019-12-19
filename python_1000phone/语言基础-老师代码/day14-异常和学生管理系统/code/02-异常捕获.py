"""__author__=余婷"""

# 1.异常： 程序在运行过程中报的错误就叫异常；ValueError、IndexError叫异常类型名
# 当程序出现异常的时候程序直接结束，不会继续执行后续的代码
# print(int('abc'))   # ValueError: invalid literal for int() with base 10: 'abc'
# print([1, 2][10])   # IndexError: list index out of range
# print('=========')

# 2.异常捕获: 让程序出现异常的时候不崩溃，程序可以继续执行
"""
1)什么时候需要捕获异常: 明知道某个位置可能会出现异常，但是程序员又没有办法控制的时候
2)怎么捕获异常

语法一: 捕获任意可以捕获的异常
try:
    代码块1(需要捕获异常的代码)
except:
    代码块2(出现异常后对异常进行的处理)
finally:
    代码块3
其他语法
    
执行过程: 先执行代码块1，如果出现异常，程序不崩溃，马上执行代码块2；执行完代码块2再执行其他语句。
         如果代码块1中没有出现异常，不执行代码块2，直接执行后面的其他语句
         
语法二: 捕获指定的一种异常
try:
    代码块1
except 异常类型:
    代码块2
finally:
    代码块3
    
执行过程: 先执行代码块1，如果代码块1出现异常，检测异常类型和except后面的异常类型是否一致；
         如果一致，程序不崩溃，直接执行代码块2；如果不一致，程序直接崩溃。
         如果没有出现异常，不执行代码块2，直接执行后面的其他语句


语法三: 捕获多种异常，对不同进行相同的处理
try:
    代码块1
except (异常类型1, 异常类型2,...):
    代码块2
finally:
    代码块3
    
    
语法四: 捕获多种异常，对不同进行不同的处理
try:
    代码块1
except 异常类型1：
    代码块11
except 异常类型2:
    代码块22
except 异常类型3:
    代码块33
...
finally:
    代码块3
"""
# 3.关键字finally
"""
所有的异常捕获结构的最后可以添加一个finally
finally后面的代码块，不管try中的代码出现任何情况都会执行：
1）代码块1没有异常finally会执行
2）代码块1中有异常，异常被捕获finally会执行
3）代码块1中有异常，异常没有被捕获finally会执行
"""


# age = int(input('请输入年龄:'))
# # print('年龄:', age)

print('============语法1=============')
try:
    print(int('abc'))
    print([1, 2][10])
    print('++++++++')
except:
    print('出现了异常!')

print('=========')

print('===============语法2================')
try:
    print(int('abc'))
    print([1, 2][10])
    print('++++++++')
except ValueError:
    print('下标越界!')

print('语法2结束')

# raise ValueError

print('=============finally=============')
# try:
#     print('++++')
#     print({'name': '张三', 'age': 18}['gender'])
#     print('hello'[100])
#     print(max([10, 'abc', True]))
# except IndexError:
#     print('出现异常')
# finally:
#     print('写遗书！')
