"""__author__=吴佩隆"""

# 1.变量的作用域 - 变量可以使用的范围

# 2.全局变量和局部变量
"""
1)全局变量
没有声明在函数中或者类中的变量都是全局变量
全局变量从声明开始到文件结束任何地方都可以使用

2)局部变量
声明在函数中的变量就是局部变量
从声明开始到函数结束(形参是声明在函数中的变量)
"""
print('===============全局变量=====================')
# a是全局变量
a = 10

# b也是全局变量
for b in range(4):
    # c也是全局变量
    c = 100
    pass

print(b)


def fun1():
    print('函数中:', a, b, c)


fun1()


print('===============局部变量=====================')

# aa和bb都是局部变量
def func2(aa):
    bb = 200
    print('外函数', aa, bb)

    def func3():
        cc = 300
        print('内函数', aa, bb)

    func3()
    # print('外函数',cc) NameError: name 'cc' is not defined


func2(100)
# print(aa)  #NameError: name 'aa' is not defined

print('===============global=====================')
# 3.global和nonlocal
"""
global和nonlocal这两个关键字只能在函数体中使用

1)global
在函数中给变量赋值前加:global 变量名
作用:在函数中声明全局变量
如果外部没有事先声明,可以直接在函数内部用global 变量声明
函数销毁后外部依然可用

2)nonlocal
使用方法:在函数中给变量赋值前加:nonlocal 变量名
作用:在内函数中修改局部变量的值,就如同函数作用域中的global

"""
# 全局变量a1
a1 = 100
b1 = 100


def func4():
    # 声明一个局部变量a1
    a1 = 200

    # 声明b1是全局变量
    global b1
    b1 = 300    # 修改全局变量的值
    # 使用的局部变量a1,使用全局变量b1

    global c1   # 外部没有声明依然可以直接声明
    c1 = 500

    print('函数内', a1, b1, c1)


func4()
# 使用的是全局变量a1
print('函数外', a1, b1, c1)


print('===============nonlocal================')


def func5():
    a2 = 100
    b1 = 100

    def func6():
        a2 = 200
        nonlocal b1
        # nonlocal c1   外函数没有不能直接声明,跟global不一样
        # c1 = 100       只能修改,不能建立
        b1 = 200
        print('函数的函数中:', a2, b1)

    func6()
    print('函数中', a2, b1)


func5()
