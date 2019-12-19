"""__author__=余婷"""

# 1.函数作为变量
"""
python中声明函数就是声明一个类型是function的变量，函数名就是变量名
普通变量能做的事情函数都可以做
"""


# 1.声明函数就是声明变量，函数名就是变量名
def func1():
    print('函数1')
    return 100


print(type(func1))
a = 100
print(type(a))

func2 = lambda x: x*2
"""
def func2(x):
    return x*2
"""
print(type(func2))


# 2.普通变量能做的函数都可以做
# 1)一个变量可以给另外一个变量赋值
a = 100
b = a
print(b, b+10)


def func3():
    print('函数3')
    return 200


b2 = func3
print(type(b2), b2())

# 2)修改变量的值
a = 'abc'
print(a, a[1:])

func3 = [10, 20]
# func3()   # TypeError: 'list' object is not callable
func3.append(100)
print(func3)

# 3)变量作为序列元素
a = 10
list1 = [a, 100, 'abc']
print(list1)


def func4():
    print('函数4')
    return 400

list2 = [func4, func4(), 10]
print(list2)
print(list2[0]())    # func4()


# 4)变量作为函数的参数
def func5(x):
    print('函数5:', x)


a = 100
func5(a)
func5(func4)


print('===================实参高阶函数==================')


def func4():
    print('函数4')
    return 400


# 1.将函数作为函数的参数  -  实参高阶函数
def func6(x):
    # x = func4
    y = x()  # func4()
    # print('y:', y)
    return y


# func6(a)   # TypeError: 'int' object is not callable
re = func6(func4)
print(re)


# 2.系统的实参高阶函数
# 列表.sort()、sorted()、max()、min()都是实参高阶函数, 因为这四个函数中都有一个参数key，要求是一个函数
nums = [10, 89, 78, 7]
nums.sort(reverse=True)
print(nums)

# 1）排序方法: 参数key要求是一个函数，作用是用来定制排序的规则(默认按元素的大小从小到大或者从大到小排序)
"""
参数key的要求:
a.key是一个函数
b.函数中有且只有一个参数, 这个参数指向的是序列中的每个元素
c.函数需要一个返回值，这个返回值就是排序的时候比较大小的对象
"""
# 练习: 将nums中的元素按个位数从小到大排序
nums = [100, 39, 51, 62, 58]
# nums = [100, 51, 62, 58, 39]


# def func_key(item):
#     return item % 10
# func_key = lambda item: item % 10

nums.sort(key=lambda item: item % 10)
print(nums)


# 练习2：将学生按成绩从大到小排序
students = [
    {'name': '小明', 'age': 18, 'score': 90},
    {'name': '小花', 'age': 23, 'score': 78},
    {'name': '王五', 'age': 17, 'score': 65},
    {'name': '李四', 'age': 30, 'score': 89}
]
# def func1(item):
#     return item['score']
students.sort(reverse=True, key=lambda item: item['score'])
print(students)

# 练习3: 按学生年龄和分数的和从小到排序
students.sort(key=lambda item: item['age'] + item['score'])
print(students)

# 2) max、min默认是直接比较序列元素的大小求出最大值和最小值
nums = [17, 89, 100, 78, 23]
max1 = max(nums)
print(max1)

# 求nums中个位数最大的元素
max2 = max(nums, key=lambda item: item % 10)
print(max2)


students = [
    {'name': '小明', 'age': 18, 'score': 90},
    {'name': '小花', 'age': 23, 'score': 78},
    {'name': '王五', 'age': 17, 'score': 65},
    {'name': '李四', 'age': 30, 'score': 89}
]
print(max(students, key=lambda item: item['score']))


# 3)max函数的原理(了解)
def yt_max(seq, key=None):
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


# max1 = max(nums)
# print(max1)
# max([nums], key=)

max1 = max((10, 9, 8, 67), key=lambda item: item % 10)
print(max1)

max2 = yt_max((10, 12, 8, 67, 29), key=lambda item: item % 10)
print(max2)





