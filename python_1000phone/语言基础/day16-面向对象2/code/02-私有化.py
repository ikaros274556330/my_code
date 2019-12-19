"""__author__=吴佩隆"""

# 1.访问权限:
"""
公开的(public):类的里面、类的外面都能用，也能被继承
保护的(protect):类里面能使用，也可被继承
私有的(private):只有类里面能使用，不能被继承
"""

# 2.python中类的内容的访问权限
"""
严格来说,python类中的内容只有公开的;私有化是假的私有化
"""

# 3.怎么私有化
"""
在方法名前或属性名前加__
"""


class Person:
    num = 61
    __num2 = 100

    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def func1(self):
        print('%s今年%d岁' % (self.name,self.age))

    @staticmethod
    def func2():
        print('我是静态方法1')

    @classmethod
    def func3(cls):
        print(cls.num)
        print(cls.__num2)


print('==========默认公开的属性和方法里外都可使用=====')
print(Person.num)

p1 = Person('小明')
print(p1.name, p1.age)

p1.func1()

Person.func2()


print('=========私有的属性和方法=========')
print(Person._Person__num2)
