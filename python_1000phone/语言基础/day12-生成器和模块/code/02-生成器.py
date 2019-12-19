"""__author__=吴佩隆"""

# 1.什么是生成器
"""
生成器就是迭代器的一种;生成器作为容器他保存的不是数据,而是产生数据的算法
"""

# 2.怎么创建生成器
"""
调用带有yield关键字的函数,就可以得到一个生成器
函数中只要有yield不管能不能遇到,调用这个函数都不会执行函数体,并且得到的是一个生成器的对象
"""


def func1():
    print('=====')
    print('+++++')
    yield


re = func1()  # 这儿的re就是生成器
print(re)    # <generator object func1 at 0x000001AFEBEFA348>


# 3. 生成器怎么产生数据(怎么确定生成器中的元素)
"""
一个生成器能够产生多少个数据和那些数据,看执行完生成器关联的函数的函数体会遇到几次yield
能够遇到几次yield生成器就可以产生多少个数据,每次遇到yield,yield后面的数据就是对应的元素
"""


def func2():
    yield 10
    yield 100
    yield 1000


gen1 = func2()
for x in gen1:
    print('x', x)


print('==========================================================')
# 4.生成器产生数据的规律
"""
生成器怎么获取元素
获取第一个元素的时候从函数的第一条语句开始执行,执行到第一个yield为止,并且将yield后面的值作为
当前获取到的元素;获取下一个元素的时候接着上次结束的往后执行,直到遇到下一个yield为止,并且
将yield后面的值作为当前获取到的元素;以此类推
当从执行位置开始到函数结束没有遇到yield就会报错StopIteration
"""


def func2():
    print('=========')
    yield 1
    print('+++++++++')
    yield 10
    print('---------')
    yield 100


gen2 = func2()
print(next(gen2))
print(next(gen2))
print(next(gen2))

print('============================================')


def func3(n):
    for _ in range(n):
        yield 100


gen3 = func3(4)
next(gen3)
for x in gen3:
    print('x:', x)


# 写一个生成器,能够产生一班所有学生的学号,班级人数自己定;前缀自己定

def stu_id(num1, str1):
    length = len(str(num1))
    for i in range(1, num1+1):
        yield str1+str(i).zfill(length)


stu = stu_id(99, 'python')
for i in stu:
    print(i)