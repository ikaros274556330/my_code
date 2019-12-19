"""__author__=余婷"""
from random import randint


# 2.声明⼀个人的类和狗的类:
# 狗的属性:名字、颜色、年龄
# 狗的方法:叫唤
# 人的属性:名字、年龄、狗
# 人的方法:遛狗
# a.创建⼈的对象小明，让他拥有一条狗⼤黄，然后让⼩明去遛⼤黄
class Dog:
    """狗类"""
    def __init__(self, name: str, color='黄色', age=1):
        self.name = name
        self.color = color
        self.age = age

    def shout(self):
        print('%s在嗷嗷叫' % self.name)


class Person:
    def __init__(self, name:str, age=18, dog=None):
        self.name = name
        self.age = age
        self.dog = dog

    def walk_with_dog(self):
        if self.dog:
            print('%s牵着%s散步' % (self.name, self.dog.name))
        else:
            print('没有狗，遛自己！')


p1 = Person('小明')
p1.dog = Dog('大黄')
p1.walk_with_dog()


# 3.声明⼀一个圆类，自己确定有哪些属性和方法
# 属性:半径、圆心、圆周率
# 方法:求周长、求面积、求圆心距、是否内切、是否外切
class Point:
    """点类"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        """
        求当前点到另外一个点的距离
        :param other: 另外一个点对象
        :return: 两个点之间的距离
        """
        # self=c1.center=Point(0, 0); other=c2.center=Point(200, 0)
        a = self.x - other.x
        b = self.y - other.y
        return (a**2 + b**2)**0.5


class Circle:
    """圆类"""
    pi = 3.1415926

    def __init__(self, radius: float, center: Point):
        self.radius = radius
        self.center = center

    def perimeter(self):
        """周长"""
        return 2 * Circle.pi * self.radius

    def area(self):
        """面积"""
        return Circle.pi * self.radius * self.radius

    def circles_center_distance(self, other):
        """
        求两个圆的圆心距
        :param other: 另外一个圆
        :return: 圆心距
        """
        # self = c1; other=c2
        # return Point(0, 0).distance(Point(200, 0))
        return self.center.distance(other.center)

    @staticmethod
    def circles_center_distance2(circle1, circle2):
        pass


c1 = Circle(100, Point(0, 0))
c2 = Circle(60, Point(200, 0))

c1.circles_center_distance(c2)


class Line:
    """线段类"""
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        return self.start_point.distance(self.end_point)


class Line1:
    def __init__(self, start=(0, 0), end=(0,0)):
        self.start = start
        self.end = end


l1 = Line(Point(100, 0), Point(0, 0))
print(l1.start_point.x, l1.start_point.y)


l2 = Line1((100, 0), (0, 0))
print(l2.start[0], l2.start[1])


# 4.创建一个学生类:
# 属性:姓名，年龄，学号
# 方法:答到，展示学生信息
# 创建⼀个班级类:
# 属性:学⽣，班级名
# 方法:添加学生，删除学生，点名, 求班上学生的平均年龄
class Student:

    def __init__(self, name, age=18, study_id='001'):
        self.name = name
        self.age = age
        self.study_id = study_id
        self.is_in_classroom = randint(0, 1)

    def respond(self):
        if self.is_in_classroom:
            print('%s，到!' % self.name)

    def show(self):
        print('姓名:{}, 年龄:{}, 学号:{}'.format(self.name, self.age, self.study_id))


class Class:
    def __init__(self, name):
        self.students = []
        self.name = name

    def add_student(self):
        """添加学生"""
        name = input('姓名:')
        age = input('年龄:')
        study_id = input('学号:')
        new_stu = Student(name, int(age), study_id)
        self.students.append(new_stu)

    def del_student(self):
        """删除学生"""
        study_id = input('请输入需要删除的学生的学号:')
        for stu in self.students[:]:
            if stu.study_id == study_id:
                self.students.remove(stu)
                break
        else:
            print('没有该学生!')

    def call_the_roll(self):
        """点名"""
        for stu in self.students:
            print(stu.name)
            stu.respond()

    def average_age(self):
        """平均年龄"""
        count = len(self.students)
        sum = 0
        for stu in self.students:
            sum += stu.age
        print('平均年龄:%.1f' % (sum / count))

    # 让班级所有的学生按年龄从小到大排序
    def sort_age(self):
        self.students.sort(key=lambda item: item.age)

    def show_all_student(self):
        for stu in self.students:
            stu.show()


# stu1 = Student('小明', 20)
# stu2 = Student('小花', 18)
# print(stu1 > stu2)
class1 = Class('py1906')

print('=========添加完学生==============')
for _ in range(5):
    class1.add_student()
class1.show_all_student()

print('=========学生排序===============')
class1.sort_age()
class1.show_all_student()

print('==========点名=================')
class1.call_the_roll()

print('==========平均年龄=================')
class1.average_age()

print('==========删除学生=================')
class1.del_student()
class1.show_all_student()

