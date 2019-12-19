"""__author__=吴佩隆"""

# 循环结构:for循环和while循环

# 1.for循环

"""
1)for 变量 in 序列:
    循环体

2)说明:
for     -       关键字，固定写法
变量名   -       和声明变量时的要求一样
in      -       关键字，固定写法
序列     -       容器型数据:字符串、列表、字典、元组、集合、迭代器、生成器、range
:       -       固定写法
循环体   -       和for保持一个缩进的一条或者多条语句;需要重复执行的语句

3)执行过程:
让变量取序列中取值，一个一个取，取完为止;每取一个值，执行一次循环体
(for循环通过控制序列中元素个数来控制循环次数)
"""

for x in 'abc12':
    print(x)
    print('hello')

# 2.range函数 - 为了让for更加方便的控制次数

"""
range(N) - 产生0~N-1的数字序列
range(M,N) - 产生M~N-1的数字序列
range(M,N,step) - 产生M~N-1,间隔step的数字学列
作用:1.产生指定的数字序列
    2.控制循环次数
如果只是为了控制循环次数，不需要变量的时候可以用_命名

"""

for x in range(4):
    print(x)

print('-----------------')

for x in range(3,10):
    print(x)

print('-----------------')

for x in range(0,10,2):
    print(x)

print('-----------------')

# 练习1:统计0~100中能被3整除的个数

# 方法一:
num_1 = 0
for i in range(101):
    if i % 3 == 0:
        num_1 += 1
        print(i)
print(num_1)

print('-----------------')
# 方法二:
for i in range(0,101,3):
    print(i)

print('-----------------')
# 练习2:统计1~100中能被4整除的并且个位数是2的数字的个数

num_2 = 0

for i in range(1, 101):
    if i % 4 == 0 and i % 10 == 2:
        print(i)
        num_2 += 1
print(num_2)

# 练习3:计算1+2+3+.....+100
print('-----------------')
num_3 = 0
for i in range(1,101):
    num_3 += i
print(num_3)


