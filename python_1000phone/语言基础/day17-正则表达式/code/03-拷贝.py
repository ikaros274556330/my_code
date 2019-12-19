"""__author__=吴佩隆"""

from copy import copy, deepcopy

# 1.直接赋值
"""
用一个变量直接给另一个变量赋值的时候的地址;
赋值后两个变量保存的是同一个数据的地址
"""


class Dog:
    def __init__(self,name,color='黄色'):
        self.name = name
        self.color = color

    def __repr__(self):
        return '<%s>' % str(self.__dict__)[1:-1]


class Person:
    def __init__(self, name, age=10, gender='男',dog=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = dog

    # 这个函数会在打印当前类的对象时候自动调用，返回值就是打印结果
    # 返回值是字符串
    def __repr__(self):
        return '<%s>' % str(self.__dict__)[1:-1]


# 1.直接赋值
p1 = Person('小明')
p2 = p1
p1.gender = '女'
print(p2.gender)  # 女


# 2.浅拷贝
"""
复制原数据产生一个新的数据(值和原数据一样，地址不同)，
然后将新的数据的地址返回
如果有子对象，子对象不会复制
"""
p1 = Person('小明')
p2 = copy(p1)

print(p1)
print(p2)

# 3.深拷贝
"""
复制原数据产生一个新的数据(值和原数据一样，地址不同)，
然后将新的数据的地址返回
如果有子对象，子对象也会复制
"""
print('===========================')
dog1 = Dog('旺财')

p1 = Person('小花',dog=dog1)
p2 = deepcopy(p1)
p2.dog.name = '二黑'
p2.dog.color = '黑色'

print('p1', p1, p1.dog.name)
print('p2', p2, p2.dog.name)

