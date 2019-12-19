"""__author__=余婷"""

# 1.什么是匿名函数 - 没有名字的函数
"""
匿名函数还是函数，普通函数中除了声明的语法以外其他语法基本都适用于匿名函数
1)声明匿名函数
函数名 = lambda 参数列表:返回值

相当于:
def 函数名(参数列表):
    return 返回值

2)说明:
lambda - 关键字，固定写法
参数列表 - 形参: 参数名1,参数名2,...
:      -  固定写法
返回值  -  相当于普通函数中函数体中的return语句
"""
# 用匿名函数实现求两个数的和
func1 = lambda num1, num2: num1+num2

# lambda x: print('abc')
# 匿名函数的调用和普通函数没有区别
print(func1(10, 20))
print(func1(num1=100, num2=200))


# 参数默认值
func2 = lambda a=1, b=2, c=3: print(a, b, c)

# def func2(a, b, c):
#     return print(a, b, c)

print(func2())
func2(b=20)


# 不定长参数
func3 = lambda *nums: sum(nums)
print(func3(10, 20, 30))
print(func3(1, 2, 3, 4))


# 注意：不支持类型说明
# func4 = lambda a: int, b: a*b

# 练习: 写一个匿名函数判断指定的年是否是闰年
leap_year = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(leap_year(2018))
print(leap_year(2000))



