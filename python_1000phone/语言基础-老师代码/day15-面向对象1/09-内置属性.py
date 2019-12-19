"""__author__=余婷"""

# 内置类属性 - 声明类的时候系统提供的属性


class Dog:
    """狗类！"""
    num = 100

    # __slots__是用来约束当前类最多能够拥有的对象属性
    __slots__ = ('name', 'age', 'gender', 'height', 'weight', '__dict__')

    def __init__(self, name, age=3, gender='公狗'):
        self.name = name
        self.age = age
        self.gender = gender

    def func1(self):
        print('对象方法', self.name)

    @classmethod
    def func2(cls):
        print('类方法')

    @staticmethod
    def func3():
        print('静态方法')


dog1 = Dog('大黄')

# 1. 类.__name__   -  获取类的名字
print(Dog)
print(Dog.__name__)

# 2. 对象.__class__  - 获取对象对应的类(和type(对象)功能一样)
print(type(dog1))
print(dog1.__class__)

# 3. 类.__doc__   - 获取类的说明文档
print(Dog.__doc__)
print(int.__doc__)

# 4.__dict__
# 类.__dict__   -   获取类中所有的字段和字段对应的值，以字典的形式返回
print(Dog.__dict__)

# (掌握！) 对象.__dict__  -  获取对象所有的属性和对应的值，以字典的形式返回
# 注意: 如果设置了__slots__,对象的__dict__就不能用
print(dog1.__dict__)

dog1.height = 180
# dog1.nema = '财财'


# 5.类.__module__   -  获取当前这个类是哪个模块中声明的，返回的是模块名
print(Dog.__module__)
print(int.__module__)


# 6.类.__bases__   -  获取当前类的所有的父类
# object是python的基类
print(Dog.__bases__)
print(Dog.__base__)

