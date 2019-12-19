"""__author__==吴佩隆"""

# 1.函数作为变量
"""
python 中声明函数就是声明一个类型为function的变量，函数名就是变量名
普通变量能做的事情函数都可以做
"""


def fun1():
    print('函数1')
    return 100


print(type(fun1))

# 2.普通变量能做的事情函数都可以做
# 1）一个变量可以给另一个变量赋值
a = 100
b = a
print(b, b + 10)


def fun2():
    print('函数2')
    return 200


b2 = fun2
print(type(b2), b2())

# 2）修改变量的值

fun3 = 100
# fun3()      TypeError: 'int' object is not callable

# 3)变量作为序列元素
a = 10
list1 = [a, 100, 'abc']
print(list1)

list2 = [fun2, fun2(), 10]
print(list2[0]())


# 4)变量作为函数的参数
def func3(x):
    print('函数5：', x)


a = 100
func3(a)
func3(fun2)

print('===================================')


# 3.将函数作为函数的参数 - 实参高阶函数


def fun4(x):
    y = x()
    return y


re = fun4(fun2)
print(re)

# 2.系统的实参高阶函数
# 列表.sort()、sorted()、max()、min()都是实参高阶函数,因为这四个函数中都有一个参数key，要求是一个函数
nums = [10, 89, 78, 7]
nums.sort(reverse=True)
print(nums)

# 1）排序方法:参数key要求是一个函数,作用是用来定制排序规则(默认按元素的大小从小到大或从大到小)
"""
参数key的要求
a.key是一个函数
b.函数中有且只有一个参数，这个参数指向的是序列中的每个元素
c.函数需要一个返回值，这个返回值就是排序的时候比较大小的对象
"""
nums = [100, 39, 51, 62, 58]

# def func_key(item):
#     return item % 10


# nums.sort(key=func_key)
nums.sort(key=lambda x: x % 10)
print(nums)

students = [
    {'name': '小明', 'age': 18, 'score': 90},
    {'name': '小花', 'age': 23, 'score': 78},
    {'name': '小兰', 'age': 17, 'score': 65},
    {'name': '小红', 'age': 30, 'score': 89}
]

students.sort(reverse=True, key=lambda item: item['score'])
print(students)

students.sort(key=lambda item: item['score'] + item['age'])
print(students)

# 2）max、min直接比较元素的大小求出最大最小值
nums = [100, 39, 51, 62, 58]
max1 = max(nums)
print(max1)

max2 = max(nums, key=lambda i: i % 10)
print(max2)


# 3）max函数的原理


def max1(seq, key=None):
    t_seq = list(seq)
    t_max = t_seq[0]

    if not key:
        for item in t_seq[1:]:
            if item > t_max:
                t_max = item
    else:
        for item in t_seq[1:]:
            if key(item) > key(t_max):
                t_max = item
    return t_max


print(max((10, 9, 8, 67), key=lambda item: item % 10))
print(max1((10, 9, 8, 67), key=lambda item: item % 10))
