"""__author__=吴佩隆"""

# 内置类属性 - 声明类的时候系统提供的属性


class Dog:
    """狗类！"""
    num = 100

    # 约束对象属性
    # __slots__ = ('name', 'age', 'gender', 'height', 'weight')

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

# 1. 类.__name__    -    获取类的名字

print(Dog)
print(Dog.__name__)


# 2. 对象.__class__  -  获取对象对应的类(和type(对象)功能一样)
print(type(dog1))
print(dog1.__class__)


# 3. 类.__doc__    -    获取类的说明文档
print(Dog.__doc__)


# 4. __dict__

# 类.__dict__    -    获取类中所有字段和字段对应的值，以字典的形式返回
print(Dog.__dict__)


# 5.(掌握!) 对象.__dict__  -  获取对象所有的属性和对应的值，以字典形式返回
print(dog1.__dict__)

# 6.__slots__  -  用来约束当前类最多能够拥有的对象属性

# 注意 __dict__和__slots__只能存在一个，不可兼得

# 7.类.__module__  -  获取当前这个类实在哪个模块中声明的,返回模块名
print(Dog.__module__)
print(int.__module__)


# 8. 类.__bases__    -    获取当前类的父类

# object是python的基类
print(Dog.__bases__)






