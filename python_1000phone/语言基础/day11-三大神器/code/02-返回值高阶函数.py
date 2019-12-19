"""__author__==吴佩隆"""


# 1.变量可以作为函数的返回值
def sum1(x, y):
    t = x + y
    return t


print(sum1(10, 20))


print('================================')
# 函数作为函数的返回值 - 返回值高阶函数
# func1就是一个返回值高阶函数


def func1():

    def func2():
        print('函数2')

    return func2


print(func1())
func1()()
print(func1()())
print('================================')

# 2.闭包 - 函数1中声明了一个函数2，并且在函数2中使用了函数1的数据，那么这个函数1就是一个闭包
# 闭包的特点:闭包函数中的数据不会因为函数调用结束而销毁


def func3():
    a = 10

    def func4():
        print(a)

    return func4


t = func3()
t()

print('========================')
# 面试题1:
list1 = []
for i in range(5):
    list1.append(lambda x: x*i)  # 声明函数不会执行函数体,所以list1中五个函数都是一样的
# i = 4
print(list1[1](2), list1[2](2), list1[3](2))


# 面试题2
def func2(seq=[]):
    seq.append(10)
    return seq


print(func2())
print(func2())

# 练习:写出打印列表

list3 = [1, 2]


def func3(seq=list3):
    seq.append(10)
    return seq


func3()
list3.append(100)
print(func3())

