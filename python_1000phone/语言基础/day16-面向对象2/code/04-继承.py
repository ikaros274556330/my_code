"""__author__=吴佩隆"""

# 1.什么是继承
"""
继承是让子类直接拥有父类的属性和方法
子类 - 继承者(儿子)
父类 - 被继承者(爸爸),又叫超类
"""

# 2.怎么继承
"""
语法:
class 类名(父类1,父类2,...):
    类的说明文档
    类的内容
"""

# 3继承那些东西
"""
父类所有的属性和方法
"""


class Person:
    num = 61

    def __init__(self):
        self.name = '小明'
        self.age = 18

    @staticmethod
    def func1():
        print('静态方法')


class Student(Person):
    pass


# 子类直接使用父类的属性和方法
print(Student.num)
Student.func1()

# 4.子类中添加属性和方法
"""
1)添加方法和字段
在子类中直接声明新的字段和方法
注意:如果添加的字段名和方法名和父类的字段方法同名，
子类中的字段和方法会覆盖父类的字段和方法  -  重写

2)添加对象属性
在自己的init方法中添加新的属性
并且需要通过super()去调用父类的__init__方法继承父类的对象属性
"""

# 5.super的应用
"""
可以在类中任何一个对象方法或者类方法中去通过super()调用父类的对象方法或类方法

super(类1,类1对象).方法() -> 调用类1父类中的方法
super().方法()  <==>  super(当前类,当前类的对象)

super(type,obj) -> 要求obj必须是type的对象或者是type的子类对象
"""


class Animal:
    num = 100

    def __init__(self):
        self.age = 10
        self.gender = '雌'

    def a_func1(self):
        print('动物的对象方法1')

    @staticmethod
    def fun1():
        print('动物中的静态方法！')

    def func2(self):
        print('动物中的对象方法2')

    @classmethod
    def func4(cls):
        print('动物中的类方法')


class Cat(Animal):
    voice = '喵~'

    def __init__(self):
        super().__init__()  # 调用当前类的父类的__init__方法
        self.color = '白色'
        self.breed = '机器猫'

    @classmethod
    def c_func1(cls):
        print('猫的类方法')

    @staticmethod
    def fun1():  # 静态方法不能直接使用super()方法
        print('猫中的静态方法')

    def func3(self):
        super().func2()
        print('猫中的对象方法3')

    @classmethod
    def fun5(cls):
        super().func4()
        print('猫中的类方法')


cat1 = Cat()
print(Cat.num, Cat.voice)  # 100 喵~
cat1.a_func1()  # 动物的对象方法1
Cat.c_func1()  # 猫的类方法

print('========================')

Cat.fun1()  # 猫中的静态方法
Animal.fun1()  # 动物中的静态方法！

print('===============================')

cat1 = Cat()
print(cat1.age, cat1.gender)  # 10 雌
print(cat1.color, cat1.breed)  # 白色 机器猫

print('==================================')

cat1.func3()  # 动物中的对象方法2
# 猫中的对象方法3


print('=========================')
Cat.fun5()  # 动物中的类方法
# 猫中的类方法

print('==============================================')


class A:
    def func(self):
        print('this is A')


class B(A):
    def func(self):
        print('this is B')


class C(B):
    def func(self):
        # super().func()
        # super(C,self).func()
        super(B, B()).func()
        print('this is C')


obj = C()
obj.func()  # this is B
# this is C
