"""__author__=余婷"""

# 1.数据持久化
"""
1）需要持久化的数据要保存在文件
2）需要数据的时候不是在程序中直接给初始值，而是从本地文件中读数据
3）如果这个数据的值发生改变，要将最新的数据更新到文件中
"""

# 练习： 在程序中用一个变量来记录当前程序启动的次数
# 需要数据的的时候读数据
f = open('files/num.txt', 'r', encoding='utf-8')
count = int(f.read())
print(count)
f.close()

# 数据发生改变后更新文件
count += 1
f = open('files/num.txt', 'w', encoding='utf-8')
f.write(str(count))
f.close()

# 2.文件域
"""
打开指定文件，在文件作用域结束后会自动关闭文件
with open(文件路径,打开方式,编码方式) as 文件对象:
    文件作用域
    
"""
with open('files/test.txt', 'r', encoding='utf-8') as f1:
    re = f1.read()
    print(re)

# print(f1.read())   # ValueError: I/O operation on closed file.


# 每次运行程序添加一个学生，要求之前添加的学生要一直存在
"""
张三
[张三]

李四
[张三, 李四]

小明
[张三, 李四, 小明]
"""
# with open('files/students.txt', 'r', encoding='utf-8') as f1:
#     students = f1.read()
#
# name = input('学生姓名:')
# if students == '[]':
#     # [张三]
#     students = '{}{}]'.format(students[:-1], name)
# else:
#     # [张三,李四]
#     students = '{},{}]'.format(students[:-1], name)
#
# print(students)
#
# with open('files/students.txt', 'w', encoding='utf-8') as f:
#     f.write(students)


# 3.容器字符串的转换: eval
# eval(字符串) - 将字符串转换成容器型数据类型的数据(要求字符串去掉引号后本身是合法的容器数据)
# 怎么将字符串: '[张三,李四,小明,tom]' 转换成列表: [张三,李四,小明,tom]
str1 = '[1, 2, 3]'
# 将列表字符从转换成列表
re1 = eval(str1)
print(re1, type(re1))
re1.append(100)
print(re1)   # [1, 2, 3, 100]

str2 = "{'a': 10, 'b': 20}"
# 将字典字符串转换成字典
re2 = eval(str2)
print(re2, type(re2))
print(re2['a'])

str3 = "[{'name': '小明', 'age': 18}, {'name': '小花', 'age': 19}, {'name': 'Lisa', 'age': 22}]"
re3 = eval(str3)
print(type(re3))
print(type(re3[0]))





