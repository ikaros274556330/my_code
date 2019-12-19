"""__author__=吴佩隆"""

# 1.根据实参的传值方式将实参分为:位置参数、关键字参数
"""
1)位置参数 - 直接让实参的值和形参一一对应
2)关键字参数 - 调用函数的时候以'形参1=值1,形参2=值2...'的形式传参
3)位置参数和关键字混用 - 位置参数必须在关键字参数前面
"""


def func1(a, b, c):
    print('a:{},b:{},c:{}'.format(a, b, c))


func1(10, 20, 30)

func1(a=100, b=200, c=300)
func1(c=100, a=200, b=300)

func1(10, c=100, b=200)

print('=========================================')
# 2.参数默认值(形参)
"""
声明函数的时候，可以通过'参数名=值'的形式给参数默认值;
有默认值的参数在调用的时候可以不传参
关键参数的使用场景:想要前面有默认值的参数直接给后面参数赋值的时候，必须使用关键字参数
注意:有默认值的参数必须放在没有默认值参数的后面
"""


def func2(a, b, c=30):
    print('a:{},b:{},c:{}'.format(a, b, c))


func2(10, 20, 10)


def fun3(a, b=2, c=3):
    print('a:{},b:{},c:{}'.format(a, b, c))

print('======================================')
# 3.参数类型说明
"""
1)给参数赋默认值
2)形参:类型名
3)返回值类型说明 -> 类型

根据参数提示赋值
"""


def func4(z: list, y: str, x=10) -> str:
    """

    :param z:
    :param y: 字符串
    :param x: int
    :return:
    """
    print(z, y, x)


func4([1, 2], 'a', 3)
print('================================================')
# 4.不定长参数
"""
声明函数的时候，参数个数不确定（不定长参数）

1)声明函数的时候在参数名前加*,这个参数就会变成一个元组，元组中的元素就是对应的多个实参
注意：a.调用的时候只能使用位置参数
     b.不定长参数后面如果有其他的定长参数，那么他后面的其他参数必须使用关键字参数
     
2)声明函数的时候在参数名前加**，这个参数就会变成字典,字典中的元素->关键字：实参值
注意：a.调用的时候只能使用关键字参数
     b.*和**同时使用时这个函数参数个数不确定，可以同时使用位置参数和关键字参数传参，写的时候*必须在**前
"""

# 写一个函数，求多个数的和


def sum1(*x):
    all_num = 0
    for i in x:
        all_num += i
    print(all_num)


sum1(1, 2, 3)


def func5(name, *scores, sex):
    print(name, scores, sex)


def func6(**x):
    print(x)


func5('雷军', sex=2)
func5('雷军', 12, 45, 65, 78, sex=1)

func6(x=100)
func6(a=100, b=200)

print('===============================')


def func7(*args, **kwargs):
    print(args, kwargs)


func7()
func7(1, 2)
func7(a=10, b=20)
func7(12, a=10)
