"""__author__=吴佩隆"""

# 1.类中的方法
"""
类中的方法有三种:对象方法、类方法、静态方法

1)对象方法
a.怎么声明:直接声明在类中的函数
b.怎么调用:通过对象来调用
c.特点:自带一个参数self;self在调用的时候不用传参，指向当前对象
        self -> 当前对象

d.什么时候用:如果实现函数的功能需要用到对象属性，这个函数就声名成对象方法

2)类方法
a.怎么声明:在函数声明前加@classmethod
b.怎么调用:通过类来调用
c.特点:自带参数cls, cls调用时不用传参，系统会自动将当前类传给cls
            cls -> 当前类(当前类能做的事情cls都可以做)
d.什么时候用:实现函数的功能不需要对象属性的前提下，需要类的时候用类方法

2)静态方法
a.怎么声明:在函数声明前加@staticmethod
b.怎么调用:通过类来调用
c.特点:没有自带的参数
d.什么时候用:实现函数的功能不需要对象属性的前提下，也不需要类的时候用静态方法
"""


class Student:
    num = 100

    def __init__(self, name, tel, age=18):
        self.name = name
        self.age = age
        self.tel = tel

    # study是对象方法
    def study(self):
        print('%s在学习' % self.name)

    @classmethod
    def func1(cls):
        print('cls:', cls)
        print('类方法func1')

        # cls可以创建对象
        stu2 = cls('小花', 112, 20)
        print('stu2:', stu2)
        print(cls.num)

    @staticmethod
    def fun2():
        print('静态方法fun2')


stu = Student('小明', '110')
stu.study()

print('Student:', Student)
Student.func1()
Student.fun2()


class Math:
    pi = 3.141592653

    @classmethod
    def circle_area(cls, r):
        return cls.pi * r ** 2

    @staticmethod
    def sum(num1, num2):
        return num1 + num2


class Keng:
    num = 100

    def func1(self):
        print('坑中的对象方法')

    @classmethod
    def func2(cls):
        print('坑中的类方法')

    @staticmethod
    def func3():
        print('坑中的静态方法')


# 注意:类中的所有方法都可以通过对象或者类调用
# 类调用对象方法
Keng.func1(1)  # 用类调用对象方法self会失去意义
k = Keng()
k.func2()       # 用对象调用类方法多此一举，cls还是当前类
k.func3()       # 同上
