"""__author__=余婷"""


# 1.变量可以作为函数的返回值
def yt_sum(x, y):
    # x=10, y=20
    t = x+y   # t = 10+20 = 30
    return t  # return 30


print(yt_sum(10, 20))


# 函数作为函数的返回值  -  返回值高阶函数
# func1就是一个返回值高阶函数
def func1():
    def func2():
        print('函数2')

    return func2


print(func1())
func1()()   # func2()
print('=============')
print(func1()())    # func2()  -> None


# 2.闭包 - 函数1中声明了一个函数2，并且在函数2中使用了函数1的数据，那么这个函数1就是一个闭包
# 闭包的特点: 闭包函数中的数据不会因为函数调用结束而销毁
def func3():
    a = 10
    print(id(a))

    def func4():
        print(a)
        print(id(a))

    return func4


t = func3()
t()   # 10

# 面试题1：
list1 = []
for i in range(5):
    list1.append(lambda x: x*i)

# list1 = [lambda x: x*i, lambda x: x*i, lambda x: x*i, lambda x: x*i, lambda x: x*i]
# i = 4
print(list1[1](2), list1[2](2), list1[3](2))


# def func10():
#     print(yyy + 100)


# 面试题2: 函数参数默认值
def func2(seq=[]):
    # seq = []
    seq.append(10)   # [10]
    return seq


print(func2())  # [10]
print(func2())  # [10, 10]

# 练习: 写出打印结果
list3 = [1, 2]


def func3(seq=list3):
    # seq=seq
    seq.append(10)
    return seq


func3()
# list3 = [100, 200]
list3.append(100)
print(func3())
