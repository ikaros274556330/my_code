"""__author__=余婷"""

# 1.类中的属性  -  就是类中保存数据的变量
"""
类中的属性分为2种：字段、对象属性
"""

# 2.字段
"""
1）怎么声明: 直接声明在类里面函数外面的变量就是字段
2）怎么使用: 通过类使用； 以'类.字段'的形式去使用
3）什么时候用：不会因为对象不同而不一样的属性就声明成对象属性
"""

# 3.对象属性
"""
1）怎么声明：声明在__init__方法中；以'self.属性名=值'的形式来声明

2）怎么使用: 通过对象来使用； 以'对象.属性'的形式来使用

3）什么时候用: 会因为对象不同而不一样的属性就声明成对象属性
"""


class Person:
    # a就是字段
    a = 10

    # name和age就是对象属性
    def __init__(self):
        self.name = '小明'
        self.age = 18


# print(a)    # NameError: name 'a' is not defined
print(Person.a)

p1 = Person()
print(p1.name, p1.age)

p2 = Person()
print(p2.name, p2.age)
p2.name = '小花'


class Student:
    def __init__(self, n, s=0):
        self.name = n
        self.age = 18
        self.score = s


stu1 = Student('小明')
print(stu1.name, stu1.age, stu1.score)

stu2 = Student('小花', 60)
print(stu2.name, stu2.age, stu2.score)


# 声明一个狗类，拥有属性：品种、名字、颜色、年龄、性别； 功能: 吃(xxx吃xxx)
class Dog:
    def __init__(self, name, bread='土狗', color='黄色', age=1, gender='公狗'):
        self.breed = bread
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def eat(self, food: str):
        # self=dog1; food='肉'
        print('%s在吃%s' % (self.name, food))   # self.name->dog1.name


dog1 = Dog('大黄')
dog2 = Dog('财财', color='黑色')

dog1.eat('肉')
dog2.eat('骨头')






