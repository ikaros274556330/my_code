"""__author__=余婷"""
from copy import copy, deepcopy


class Dog:
    def __init__(self, name, color='黄色'):
        self.name = name
        self.color = color

    def __repr__(self):
        return '<%s __id: %s>' % (str(self.__dict__)[1:-1], id(self))


class Person:
    def __init__(self, name, age=10, gender='男', dog=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.dog = dog

    # 这个函数会在打印当前类的对象的时候自动调用; 函数的返回值就是打印的结果
    # 返回值是字符串
    def __repr__(self):
        return '<%s __id: %s>' % (str(self.__dict__)[1:-1], id(self))


# 1.直接赋值
# 用一个变量直接给另外一个变量赋值的时候赋的地址；赋值后两个变量保存的是同一个数据的地址
print('直接赋值')
p1 = Person('小明', dog=Dog('大黄'))
p2 = p1    # 赋值后p1和p2指向是同一个Person对象
print('p1:', p1)
print('p2:', p2)
p1.gender = '女'
p1.dog.color = '白色'
print('p1:', p1)
print('p2:', p2)


# 2.浅拷贝
# 复制原数据产生一个新的数据(值和原数据一样，地址不同)，然后将新的数据的地址返回; 如果有子对象，子对象不会复制
print('=============浅拷贝==============')
p1 = Person('小明', dog=Dog('大黄'))
p2 = copy(p1)
print(p1)
print(p2)
p1.gender = '女'
p1.dog.color = '白色'
print('p1:', p1)
print('p2:', p2)

# 3.深拷贝
# 复制原数据产生一个新的数据(值和原数据一样，地址不同)，然后将新的数据的地址返回; 如果有子对象，子对象也会复制
print('=============深拷贝===========')
p1 = Person('小花', dog=Dog('大黄'))
p2 = deepcopy(p1)
print('p1:', p1)
print('p2:', p2)
p1.gender = '女'
p1.dog.color = '白色'
print('p1:', p1)
print('p2:', p2)






