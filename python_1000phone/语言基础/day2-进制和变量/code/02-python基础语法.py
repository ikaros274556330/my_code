"""__author__=吴佩隆"""
import keyword
# 1.注释
# 代码中不参与编译执行的文字就叫注释（专门用来对代码注解说明的）
# python中的单行注释就是在文字前加#
# python中的多行注释加"""注释""",或者'''注释'''
"""
多行注释1
多行注释2
多行注释3
...
"""

# 2.语句(一行一行的代码)
# 一条语句占一行,一条语句结束可以不写分号
# 如果一行中需要多条语句,语句间必须加分号

print('hello world')
print('hello world');print('你好,world')

# 3.缩进
# python中一条语句的开头不能随便加缩进（tab）或者 空格，需要时必须加

# 4.标识符
# 标识符是专门用来给变量、函数或者类命名的
# 要求:由字母、数字或者_（下划线）组成;数字不能开头(其实汉字、日语、韩语也可以做标识符;实际上不要这样做)

# 5.关键字
# python中有特殊功能或者特殊意义的标识符就是关键字，又叫保留字
"""
'False', 'None', 'True', 'and', 'as', 
'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 
 'except', 'finally', 'for', 'from', 'global', 
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
 'not', 'or', 'pass', 'raise'-抛出异常, 'return', 'try', 
 'while', 'with', 'yield-生成器'
"""
print(keyword.kwlist)

# 6.常用数据
# 1）数字数据:用来表示大小的数据，直接写就行2e3 = 2*10**3(科学记数法)，2+5j(复数)
# 2）文本数据:文本信息对应的数据，在程序中需要用单引号或者双引号引起来
# 例如:'hello','成都','门牌号','电话号码'
# 3）布尔数据:True-表示真/肯定,用False表示假/否定d，程序中只有True和False两个值

# 7.常见的数据类型 - 通过不同的数据类型对数据进行分类
# 整型(int) - 所有整数
# 浮点型(float) - 所有小数
# 字符串(str) - 文本数据对应的数据类型
# 布尔类型(bool) - True和False对应的数据类型
# 其他:列表(list)、字典(dict)、元组(tuple)、集合(set)、字节(bytes)、迭代器(iter)、生成器、函数(fuction)
# type(数据) - 获取数据对应的类型

# 8.输入和输出函数
# 1)输出函数:print
# print(数据) - 在控制台中打印指定数据
# print(表达式) - 打印表达式的结果
# print(表达式1,表达式2,...) - 一行同时打印多个表达式的结果

# a.定制换行
# 默认情况,一个print中的内容会在一行打印。
print('hello world',end='')

# b.定制分割
# 默认情况下，一个print打印多个内容的时候，多个内容之间用空格隔开
print(1,2,3,4,5,6,sep='+')

# 2)输入函数:input
# 变量 = input(输入提示信息) - 用变量去获取从控制台输入的内容;不管输入的内容是什么，类型都是字符串
age = input('请输入年龄:')
print(age)
