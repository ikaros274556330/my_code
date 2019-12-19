"""__author__=余婷"""
# 1.访问权限:
"""
公开的(public)：类的里面、类的外面都可以使用，也可以被继承
保护的(protect)：类的里面可以使用，类的外面不能使用，可以被继承
私有的(private)：类的里面可以用，类的外面不能使用也不能被继承
"""
# 2.python中类的内容的访问权限
"""
严格来说, python类中的内容只有公开的; 私有化是假的私有化
"""
# 3.怎么私有化
"""
在方法名前或者属性名前加__（但是名字后不能加__）
原理: 不是真的私有化，而是在__开头的属性名和方法名前加了'_类名'
"""


class Person:
    num = 61
    __num2 = 100

    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.gender = '男'
        self.__gender = '男'

    def func1(self):
        print('%s今年%d岁' % (self.name, self.age), self.__gender)
        self.__func11()

    def __func11(self):
        print('私有的对象方法')

    @staticmethod
    def func2():
        print('我是静态方法1')

    @staticmethod
    def __func22():
        print('我是静态方法1')

    @classmethod
    def func3(cls):
        print(cls.num)
        print(cls.__num2)


print('==========默认公开的属性和方法在类的外面都可以用========')
print(Person.num)

p1 = Person('小明')
print(p1.name, p1.age, p1.gender)

p1.func1()

Person.func2()

print('===============私有的属性和方法==========')
# print(Person.__num2)    # AttributeError: type object 'Person' has no attribute '__num2'
Person.func3()

# print(p1.__gender)  # AttributeError: 'Person' object has no attribute '__gender'
# p1.__func11()   # AttributeError: 'Person' object has no attribute '__func11'
# Person.__func22()   # AttributeError: type object 'Person' has no attribute '__func22'


print(p1.__dict__)
print(p1._Person__gender)
print(Person._Person__num2)