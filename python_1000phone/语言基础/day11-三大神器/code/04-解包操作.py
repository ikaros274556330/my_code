"""__author__==吴佩隆"""
# 1.解包:在容器型数据类型前加*或者**可以对容器进行解包
# 注意: **只能放在字典的前面
list1 = [10, 20, 30]
print(*list1)  # -> 10 20 30


def func1(x, y, z):
    print(x, y, z)


func1(*list1)


# 练习:写一个函数,可以对多个数据进行不同的运算
def sum_1(*nums):
    num1 = 0
    for x in nums:
        num1 += x
    return num1


def sub_1(*nums):
    num1 = nums[0]
    for x in nums[1:]:
        num1 -= x
    return num1


def operation(char, *nums):
    if char == '+':
        return sum_1(*nums)

    elif char == '-':
        return sub_1(*nums)


print(operation('-', 9, 90, 80, 7, 60))

# 2)**是将字典解包
dict1 = {'x': 100, 'y': 200}  # **dict1 == x==100,y==200;*dict=x,y
print(*dict1)
