"""__author__=余婷"""

# 1.注释
# 代码中不参与编译执行的文字（不影响程序功能的文字）就叫注释; 专门用来对代码进行注解和说明的
# python中单行注释就是在一行文字前加#
# python中的多行注释是： """注释"""或者'''注释'''
"""
多行注释1
多行注释2
多行注释3
....
"""

# 2.语句(一行一行的代码)
# 一条语句占一行，一条语句结束后可以不写分号
# 如果一行中需要写多条语句，语句之间必须加分号
print('hello world')
print('你好')
print('hello world'); print('你好')

# 3.缩进
# python中一条语句的开头不能随便加缩进(tab)或者空格； 如果需要缩进的时候必须加缩进
print('python')
if 100 > 10:
    print('100大于10')


# 4.标识符
# 标识符是专门用来给变量、函数或者类等命名的
# 标识符的要求: 由字母、数字或者_组成；数字不能开头! (理论其实汉字、日语、韩语等也可以作为标识符；但是实际不要这样做)
abc = 10
abc123 = 10
abc_123 = 10
abc_abc = 10
# abc+abc = 10     # SyntaxError: can't assign to operator
# 123abc = 10      # SyntaxError: invalid syntax
_abc = 10

# 5.关键字
# 在python中有特殊功能或者特殊意义的标识符就是关键字，又叫保留字(总共33个)
"""
'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
'try', 'while', 'with', 'yield'
"""
import keyword
print(len(keyword.kwlist))
print(keyword.kwlist)

# 6.常用数据
# 1) 数字数据: 用来表达大小的数据就是数字数据，在程序中直接写;
#             例如: 100, 18, 12.5, -0.12, 2e3(科学计数法), 2+5j(复数)
print(1j*1j)

# 2) 文本数据: 文本信息对应的数据，在程序中需要用单引号或者双引号引起来；
#             例如: 'hello' ，'成都市'， '千锋教育', '15300022838'
print(100)
print('我是余婷')

# 3）布尔数据: 用True表示真/肯定, 用False表示假/否定, 程序中只有True和False两个值
print(True)


# 7.常见的数据类型  -  通过不同的数据类型对数据进行分类
# 整型(int)  - 包含所有的整数
# 浮点型(float)  - 包含所有的小数
# 字符串(str)   -  文本数据对应的数据类型
# 布尔类型(bool)  -  True和False对应的数据类型
# 其他： 列表(list)、字典(dict)、元组(tuple)、集合(set)、字节(bytes)、迭代器(iter)、生成器、函数(function)等

# type(数据)  -  获取数据对应的类型
print(type(True))

# 8.输入和输出函数
# 1)输出函数: print
# print(数据)  -  在控制台中打印指定数据
print(10)
print('abc')

# print(表达式)  - 打印表达式的结果
print(10+20)

# print(表达式1, 表达式2, 表达式3,...)  - 在一行同时打印多个表达式的结果
print('你好', 123, '1+2', 1+2)

# a.定制换行
# 默认情况下，一个print中的内容会在一行打印。
print('hello world', end=';')
print('你好世界!')

# b.定制分隔
# 默认情况下，一个print打印多个内容的时候，多个内容之间用空格隔开
print(1, 2, 3, 4, sep='+')

# 2）输入函数: input
# 变量 = input(输入提示信息)   - 用变量去获取从控制台输入的内容；不管输入的内容是什么，类型都是字符串
age = input('请输入年龄:')
print('age的值是', age, type(age))






