"""__author__=余婷"""

# 1.变量的作用域 - 变量可以使用的范围
# 2.全局变量和局部变量
"""
1)全局变量
没有声明在函数中或者类中的变量都是全局变量；
全局变量从声明开始到文件结束任何地方都可以使用

2)局部变量
声明在函数中的变量就是局部变量;
从声明开始到函数结束可以使用(形参是声明在函数中的变量)
"""
# 1)==============全局变量===============
# a是全局变量
a = 10
# b是全局变量
for b in range(4):
    # c是全局变量
    c = 100
    pass


print('在外部：', a, c)
print('外部b:', b)

for x in range(3):
    print('循环中:', a, b, c)


def func1():
    print('在函数中:', a, b, c)


func1()


print('2)======================局部变量=====================')


# aa和bb都是局部变量
def func2(aa):
    bb = 200
    print('函数内部:', aa, bb)

    def func3():
        cc = 300
        print('函数中函数:', aa, bb)
    func3()
    # print('函数内部:', cc)  # NameError: name 'cc' is not defined

func2(100)

# print('函数外部:', aa)   # NameError: name 'aa' is not defined
# print('函数外部:', bb)   # NameError: name 'bb' is not defined

# 3.global和nonlocal
"""
global和nonlocal这两个关键字只能在函数体中使用

1）global
使用方法: 在函数中给变量赋值前加: global 变量名
作用: 在函数中声明全局变量

2)nonlocal
使用方法: 在函数中给变量赋值前加: nonlocal 变量名
作用: 在局部的局部中修改局部变量的值
"""
print('3)======================global的使用=====================')
# 全局变量a1
a1 = 100
b1 = 100


def func4():

    global c1
    # 声明一个局部变量a1
    a1 = 200

    # 声明b1是全局变量
    global b1
    b1 = 200   # 修改全局变量的值

    c1 = 300

    # global d1 = 200   # 错误!

    # 使用的局部变量a1; 使用的是全局变量b1
    print('函数中:', a1, b1)


func4()
# 使用的是全局变量a1, b1
print('函数外部:', a1, b1, c1)


print('4)======================nonlocal的使用=====================')


def func5():
    a2 = 100

    def func6():
        nonlocal a2
        a2 = 200

        # 这儿的a3必须上层函数中已经声明过才行
        # nonlocal a3
        # a3 = 400

        print('函数的函数中:', a2)
        return a2

    func6()
    print('函数中:', a2)
    # print('a3')    # SyntaxError: no binding for nonlocal 'a3' found


func5()






