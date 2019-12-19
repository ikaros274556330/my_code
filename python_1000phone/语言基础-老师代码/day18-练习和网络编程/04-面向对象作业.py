"""__author__=余婷"""


# 1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD属性，并且重新实现方法覆盖加速、减速的方法
class Auto:
    def __init__(self, tyre=4, color='白色', weight=2, speed=0):
        self.tyre = tyre
        self.color = color
        self.weight = weight
        self.speed = speed

    def add_speed(self):
        self.speed += 2
        if self.speed >= 180:
            self.speed = 180

    def sub_speed(self):
        self.speed -= 2
        if self.speed < 0:
            self.speed = 0

    def stop(self):
        self.speed = 0


class AirConditioner:
    def __init__(self, breed='格力', power=1, type='冷暖'):
        self.breed = breed
        self.power = power
        self.type = type


class CD:
    def __init__(self, breed='索尼', color='黑色', price=1000):
        self.breed = breed
        self.color = color
        self.price = price


class CarAuto(Auto):
    def __init__(self, tyre=4, color='白色', weight=2, speed=0):
        super().__init__(tyre, color, weight, speed)
        self.air_conditioner = AirConditioner()
        self.cd = CD()

    def add_speed(self):
        self.speed += 4
        if self.speed >= 240:
            self.speed = 240

    def sub_speed(self):
        self.speed -= 4
        if self.speed <= 0:
            self.speed = 0


# 2.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
class Person:
    count = 0

    def __init__(self):
        if self.__class__ == Person:
            Person.count += 1


class Student(Person):
    pass


stu = Student()
print(Person.count)
p1 = Person()
p2 = Person()
print(Person.count)


# 3.创建一个动物类，拥有属性：性别、年龄、颜色、类型 ，
# 要求打印这个类的对象的时候以'/XXX的对象: 性别-? 年龄-? 颜色-? 类型-?/' 的形式来打印
class Animal:
    def __init__(self, gender='雌', color='黑色', age=2, type='爬行'):
        self.gender = gender
        self.color = color
        self.age = age
        self.type = type

    def __repr__(self):
        return '/{}的对象: 性别-{} 年龄-{} 颜色-{} 类型-{}/'.format(self.__class__.__name__, self.gender, self.age, self.color, self.type)


a1 = Animal()
print(a1)


# 4.写一个圆类， 拥有属性半径、面积和周长；要求获取面积和周长的时候的时候可以根据半径的值把对应的值取到。但是给面积和周长赋值的时候，程序直接崩溃，并且提示改属性不能赋值
class ReadOnlyError(Exception):
    def __str__(self):
        return '改属性不能赋值'


class Circle:
    pi = 3.1415926

    def __init__(self, radius):
        self.radius = radius
        self._area = 0
        self._perimeter = 0

    @property
    def area(self):
        return Circle.pi * self.radius * self.radius

    @property
    def perimeter(self):
        return 2 * Circle.pi * self.radius

    @perimeter.setter
    def perimeter(self, value):
        raise ReadOnlyError

    @area.setter
    def area(self, value):
        raise ReadOnlyError


c1 = Circle(10)
print(c1.area, c1.perimeter)
# c1.area = 100   # __main__.ReadOnlyError: 改属性不能赋值













