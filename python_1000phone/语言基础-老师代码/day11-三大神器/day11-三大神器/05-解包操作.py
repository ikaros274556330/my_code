"""__author__=余婷"""

# 1.解包: 在容器型数据类型前加*或者**可以容器进行解包
# 注意: **只能放在字典的前面
# 1)*将列表和元祖解包
list1 = [10, 20, 30]
print(*list1)   # list1 == [10, 20, 30]  -> *list1 == 10, 20, 30
print(10, 20, 30)


def func1(x, y, z):
    print('x:{}, y:{}, z:{}'.format(x, y, z))


func1(10, 20, 30)
func1(*list1)

list1 = [10, 20, 30, 40]
# func1(*list1)  # func1(10, 20, 30, 40)


# 练习: 写一个函数可以对多个数据进行不同的运算
def yt_sum(*nums):
    # nums = ((9, 90, 89, 67, 8),)
    # nums = (9, 90, 89, 67, 8)
    sum1 = 0
    for x in nums:
        sum1 += x
    return sum1


def yt_sub(*nums):
    sum1 = nums[0]
    for x in nums[1:]:
        sum1 -= x
    return sum1


yt_sub(10, 2, 3)


def operation(char, *nums):
    # char='+', nums = (9, 90, 89, 67, 8)
    if char == '+':
        # yt_sum((9, 90, 89, 67, 8))
        # return yt_sum(nums)

        # yt_sum(9, 90, 89, 67, 8)
        return yt_sum(*nums)
    elif char == '-':
        return yt_sub(*nums)


print(operation('-', 28, 90, 78))
# operation('-', 28, 90, 78, 10)
print(operation('+', 9, 90, 89, 67, 8))

# 2) **是将字典解包
dict1 = {'x': 100, 'y': 200}
print(dict1)   # dict1 == {'x': 100, 'y': 200}  **dict1 == x=100,y=200; *dict1==x,y
# print(**dict1)   # print(x=100, y=200)

dict2 = {'end': '\n', 'sep': '+'}
print(10, 20, **dict2)    # print(10, 20, end='=', sep='+')


def func2(x, y):
    print(x, y)


func2(x=100, y=200)
func2(**dict1)    # func2(x=100,y=200)
