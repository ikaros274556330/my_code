"""__author__=余婷"""

# 循环结构: for循环和while循环

# 1.for循环
"""
1)语法:
for 变量名 in 序列:
    循环体
    
2)说明:
for     -     关键字,固定写法
变量名   -     和声明变量时的要求一样
in      -     关键字，固定写法
序列     -     容器型数据；字符串、列表、字典、元组、集合、迭代器、生成器、range
:       -      固定写法  
循环体   -     和for保持一个缩进的一条或者多条语句；需要重复执行的语句

3)执行过程:
让变量去序列中取值，一个一个的取，取完为止；每取一个值，执行一次循环体
(for循环可以通过控制序列中元素的个数来控制循环的次数)
"""

for x in 'abc12':
    print('x=:', x)
    print('+++++')
    print('======')
"""
x = 'a';  print('x=:',x); print('+++++'); print('======')
x = 'b';  print('x=:',x); print('+++++'); print('======')
x = 'c';  print('x=:',x); print('+++++'); print('======')
x = '1';  print('x=:',x); print('+++++'); print('======')
x = '2';  print('x=:',x); print('+++++'); print('======')
"""

# 2.range函数  -  为了让for更加方便的控制次数
"""
1）range(N)  -  产生0 ~ N-1的数字序列
例如: range(4) -> 0,1,2,3

2）range(M,N)  -  产生M ~ N-1的数字序列
例如: range(3, 10)  -> 3,4,5,6,7,8,9

3）range(M,N,step)  -  从M开始每隔step产生下一个数字，到N前一个数为止
例如: range(0, 10, 2)   ->  0, 2, 4, 6, 8

作用: 1.产生指定的数字序列  2.控制循环次数
"""
for x in range(4):
    print(x)

print('===============')
for x in range(3, 10):
    print(x)

print('===============')
for x in range(0, 10, 2):
    print(x)

# 注意: 如果for中变量取出来的值在循环体中无用，这个变量可以直接用_来命名
for _ in range(100):
    print('+++++++')

# 练习1: 打印0~100中所有能被3整除的数
# 方法一:
for x in range(101):
    if x % 3 == 0:
        print(x)

# 方法二:
print('===============')
for x in range(0, 101, 3):
    print(x)

# 练习2：统计1~100中能4整除并且个位数是2的数字的个数
print('================')
count = 0
for x in range(1, 101):
    if x % 4 == 0 and x % 10 == 2:
        # print(x)
        count += 1
print('个数:', count)


# 练习3: 计算1+2+3+...+100
sum1 = 0   # 保存最后的和
for x in range(1, 101):
    sum1 += x
print('和:', sum1)

"""
sum1 = 0
x = 1;  sum1 += x -> sum1 = sum1 + x -> sum1 = 0 + 1 = 1
x = 2;  sum1 += x -> sum1 = sum1 + x -> sum1 = 1 + 2
x = 3;  sum1 += x -> sum1 = sum1 + x -> sum1 = 1 + 2 + 3
x = 4;  sum1 += x -> sum1 = sum1 + x -> sum1 = 1 + 2 + 3 + 4
...
print('和:', sum1)
"""











