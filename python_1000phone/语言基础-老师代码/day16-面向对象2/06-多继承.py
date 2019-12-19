"""__author__=余婷"""


class Animal:
    num = 100

    def __init__(self, age=0, gender='雄'):
        self.age = age
        self.gender = gender

    def a_func1(self):
        print('动物的对象方法')

    def message(self):
        print('this is Animal')


class Fly:
    flag = '飞行'

    def __init__(self, height=1000, time=3):
        self.height = height
        self.time = time

    @classmethod
    def f_func1(cls):
        print('飞行的类方法')

    def message(self):
        print('this is Fly')


class Bird(Animal, Fly):
    pass


class A1:
    def message(self):
        super(Bird, Bird()).message()


b1 = Bird()

# 字段都可以继承
print(Bird.num, Bird.flag)

# 方法都可以继承
b1.a_func1()
Bird.f_func1()

# 对象属性只能继承第一个父类的
print(b1.age, b1.gender)
# print(b1.height, b1.time)   # AttributeError: 'Bird' object has no attribute 'height'

b1.message()

A1().message()


print('===============================================')

class A:
    def message(self):
        print('this is A')


class B:
    def message(self):
        print('this is B')


class C(A, B):
    def message(self):
        super().message()
        print('this is C')


# this is A
# this is C
C().message()

print('=================================================')
# 查看继承顺序: 先画出和需要的类相关联的所有的父类的继承关系，然后从左往右看没有子类的类

class A:
    def message(self):
        print('this is A')


class B(A):
    def message(self):
        super().message()
        print('this is B')


class C(A):
    def message(self):
        super().message()
        print('this is C')


class D(B, C):
    def message(self):
        super().message()
        print('this is D')

class E(C):
    def message(self):
        super().message()
        print('this is E')

class F(D, E):
    def message(self):
        super().message()
        print('this is F')

class G(F):
    def message(self):
        super().message()
        print('this is G')

D().message()
"""
'this is A'
'this is B'
'this is D'
"""
print(D.__mro__)
print('=========================================')
F().message()

print('==================================================')
class A:
    def message(self):
        print('this is A')

class B:
    def message(self):
        super().message()
        print('this is B')


class C(B, A):
    def message(self):
        super().message()
        print('this is C')

class D(B):
    def message(self):
        super().message()
        print('this is D')

class E(C):
    def message(self):
        super().message()
        print('this is E')

class F(D, E):
    def message(self):
        super().message()
        print('this is F')


class K(F):
    def message(self):
        super().message()
        print('this is K')


F().message()
print(F.__mro__)
