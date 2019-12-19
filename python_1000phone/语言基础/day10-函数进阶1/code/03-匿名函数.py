"""__author__=吴佩隆"""

# 1.什么是匿名函数 - 没有名字的函数
"""
匿名函数还是函数,普通函数中除了声明的语法以外其他语法基本都适用于匿名函数
1)声明匿名函数
lambda 参数列表:返回值

2)说明:
lambda - 关键字,固定写法

相当于:
def (参数列表):
    return 返回值
    

参数列表 - 形参:参数名1,参数名2,...
:   -   固定写法
返回值 - 相当于普通函数中函数体的return语句
"""

# 用匿名函数实现求两个数的和
func1 = lambda x, y: x + y

# 匿名函数的调用和普通函数没有区别
print(func1(10, 20))
print(func1(x=3, y=5))

func2 = lambda a=1, b=2, c=3: print(a, b, c)

func2()
func2(b=10)

func3 = lambda *nums: sum(nums)
print(func3(10, 20, 30))
print(func3(1, 2, 3, 4))

# 注意:不支持类型说明

# 练习:写一个匿名函数判断指定的年是否是闰年

r_year = lambda x: (x % 4 == 0 and x % 100 != 0) or x % 400 == 0
print(r_year(2002))