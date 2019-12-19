"""__author__=余婷"""

# 1.根据实参的传值方式将实参分为: 位置参数、关键字参数
"""
1）位置参数 - 直接让实参的值和形参一一对应
2）关键字参数 - 调用函数的时候以'形参名1=值1,形参名2=值2,...'的形式传参
3) 位置参数和关键字参数混用 - 混用的时候必须保证位置参数在关键字参数的前面, 同时保证每个参数都有值
"""


def func1(a, b, c):
    # a=10, b=20,c=30
    print('a:{},b:{},c:{}'.format(a, b, c))


# 位置参数
func1(10, 20, 30)   # a:10,b:20,c:30

# 关键参数
func1(a=100, b=200, c=300)  # a:100,b:200,c:300
func1(c=33, a=11, b=22)     # a:11,b:22,c:33

# 混用
func1(100, c=300, b=200)    # a:100,b:200,c:300

# func1(b=22,a=11, 33)    # SyntaxError: positional argument follows keyword argument
# func1(10, 20, b=30)     # TypeError: func1() got multiple values for argument 'b'


print('===================参数默认值=================')
# 2. 参数默认值(形参)
"""
声明函数的时候，可以通过'参数名=值'的形式给参数默认值; 有默认值的参数在调用的时候可以不传参

关键参数的使用场景: 想要跳过前面有默认值的参数直接给后面参数赋值的时候，必须使用关键字参数
注意: 有默认值的参数必须放在没有默认值参数的后面
"""


# 给所有的参数赋默认值
def func2(a=1, b=2, c=3):
    # a=10, b=20
    print('a:{},b:{},c:{}'.format(a, b, c))


func2()
func2(10)
func2(10, 20)
func2(b=200)


def func3(a, b, c=3):
    print('a:{},b:{},c:{}'.format(a, b, c))


# 3. 参数类型说明
"""
1)给参数赋默认值
2)形参: 类型名  
3)返回值类型说明 -> 类型
"""


def func4(z: list, y: str, x=10) -> str:
    """
    功能; x -> int  z是列表
    :param x:
    :return:
    """
    # z.append(10)
    print(z)


# func4('abc', 100)

# 4.不定长参数
"""
声明函数的时候，参数个数不确定（不定长参数）

1)声明函数的时候在参数名前加*, 这个参数就会变成一个元祖，元祖中的元素就是对应的多个实参  
注意: a.调用的时候只能使用位置参数
     b.不定长参数后面如果有其他的定长参数，那么它后面的其他参数必须使用关键字参数传参

2)声明函数的时候在参数名前加**, 这个参数就会变成字典，字典中的元素-> 关键字:实参值
注意: a.调用的时候只能使用关键字参数
     b. *和**同时使用时这个函数参数个数不确定，只能可以同时使用位置参数和关键参数；写的时候*要在**的前面

"""

print('=================加*===================')


# 写一个函数，求多个数的和
def yt_sum(*x):
    sum1 = 0
    for num in x:
        sum1 += num
    print(sum1)


yt_sum()
yt_sum(10)
yt_sum(10, 20)
yt_sum(1, 2, 3)
yt_sum(1, 23, 4, 5, 6, 7, 8)


def func5(name, *scores, gender):
    print(name, scores, gender)


# gender必须使用关键字参数
func5('余婷', gender='男')
func5('余婷', 29, 90, 89, 78, gender='女')

print('===================加**=================')


def func6(**x):
    print(x)


func6(x=100)
func6(a=1, b=2)
func6(a=10, b=3, x=20, y=100)

print('=================同时使用*和**==================')


def func7(*args, **kwargs):
    print(args)
    print(kwargs)


func7()
func7(1, 2)
func7(a=10, b=20, c=30)
func7(12, a=10)