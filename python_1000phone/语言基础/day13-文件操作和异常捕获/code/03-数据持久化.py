"""__author__=吴佩隆"""

# 1.数据持久化
"""
1)需要持久化的数据要保存到文件中
2)需要数据的时候不是在程序中直接给初始值,从本地文件中读取数据
3)如果数据发生改变，要将最新的数据更新到文件中
"""

# 练习：在程序中用一个变量来记录当前程序启动的次数
# count

# 需要数据的时候读取数据
with open('../files/count.txt', 'r') as f:
    count = f.read()
    print(count)

count = int(count) + 1

# 数据发生改变后更新文件
with open('../files/count.txt', 'w') as f:
    f.write(str(count))


# 2.文件域
"""
打开指定文件,在文件作用域结束后会自动关闭文件
with open(文件路径,打开方式,编码方式) as 文件对象:
    文件作用域
    
"""

# 每次运行程序添加一个学生，要求之前添加的学生要一直存在
"""
张三
[张三]

李四
[张三,李四]

"""
stu_list = []

with open('../files/stu_list.txt','r') as f:
    while True:
        stu_list.append(f.readline())
        if not f.readline():
            break

print(stu_list)

stu = input('输入要添加的学生:')

stu_list.append(stu)
with open('../files/stu_list.txt','a') as f:
    for i in stu_list:
        f.write(i)

print('============================================')

# 3.容器字符串转换:eval - 要求本身是一个合法的容器型数据
str1 = '[1,2,3]'
str2 = "{'a':1,'b':2}"

print(eval(str1))
print(eval(str2))

print(eval('4*5'))

