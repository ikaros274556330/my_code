"""__author__=吴佩隆"""

"""
1.声明⼀个电脑类: 属性:品牌、颜⾊、内存⼤小 方法:打游戏、写代码、看视频  

a.创建电脑类的对象，然后通过对象点的⽅方式获取、修改、添加和删除它的属性  

b.通过attr相关⽅方法去获取、修改、添加和删除它的属性  

"""

# class Computer:
#
#     def __init__(self, brand, color, memory):
#         self.brand = brand
#         self.color = color
#         self.memory = memory
#
#     def play_game(self):
#         print('%s的电脑内存小于%s打游戏是真的卡' % (self.brand,self.memory))
#
#     def code(self, program):
#         print('%s天下第一!' % program)
#
#     def video(self):
#         print('Bilibili~[]~(￣▽￣)~*')
#
#
# pc1 = Computer('华硕','黑色','4G')
# pc1.play_game()
# pc1.code('python')
# pc1.video()
#
# print(pc1.color)
# pc1.color = '白色'
# setattr(pc1,'memory','8G')
# print(pc1.memory)


"""
2.声明⼀个人的类和狗的类:  

狗的属性:名字、颜色、年龄   

狗的⽅法:叫唤     

人的属性:名字、年龄、狗   

人的⽅法:遛狗    

a.创建⼈的对象小明，让他拥有一条狗大黄，然后让⼩明去遛大⻩
"""


# class Dog:
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age
#
#     def wang(self):
#         print('汪~~')
#
#
# class Person:
#     def __init__(self, name, age, dog):
#         self.name = name
#         self.age = age
#         self.dog = dog
#
#     def walk_dog(self):
#         print('%s牵着%s在公园里遛弯！~~' % (self.name, self.dog.name))
#
#
# dog1 = Dog('大黄', '黄色', '5')
# person1 = Person('小明', 18, dog1)
#
# person1.walk_dog()

"""
3.声明⼀一个圆类，自己确定有哪些属性和方法
"""

# class Circle:
#
#     pi = 3.141592653
#
#     @classmethod
#     def area(cls, r):
#         return cls.pi*r**2
#
#     @classmethod
#     def perimeter(cls, r):
#         return cls.pi*r*2
#
#
# print(Circle.area(5))
# print(Circle.perimeter(5))

"""
4.创建⼀一个学⽣生类:  

属性:姓名，年龄，学号   

方法:答到，展示学⽣生信息  

创建⼀一个班级类:   

属性:学⽣生，班级名   

方法:添加学⽣生，删除学生，点名, 求班上学生的平均年龄

"""
