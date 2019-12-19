"""__author__=吴佩隆"""
"""
1.
建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等属性，
并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。 
再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD属性，
并且重新实现方法覆盖加速、减速的方法
"""

# class Auto:
#     tire = 4
#
#     def __init__(self, color, weight, speed):
#         self.color = color
#         self.weight = weight
#         self.speed = speed
#
#     def add_speed(self):
#         print('加速1')
#
#     @classmethod
#     def sub_speed(self):
#         print('减速1')
#
#     @staticmethod
#     def stop():
#         print('停车！1')
#
#
# class CarAuto(Auto):
#     kt = '空调'
#     cd = 'cd'
#
#     def add_speed(self):
#         print('加速2')
#
#     @classmethod
#     def sub_speed(cls):
#         print('减速2')
#
#
# car = CarAuto('黑色', 1400, 240)
#
# print(car.color, car.weight, car.speed)
# print(CarAuto.kt, CarAuto.cd)
#
# car.add_speed()
# CarAuto.sub_speed()

"""
2.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
"""

# class Person:
#     all_number = 0
#
#     def __init__(self):
#         Person.all_number += 1
#
#     def __del__(self):
#         Person.all_number -= 1
#
#     @classmethod
#     def show_num(cls):
#         print('目前被创造的对象个数:{}'.format(Person.all_number))
#
#
# Person.show_num()
#
# all_person_list = []                 # 对象列表
# for i in range(50):                  # 建造50个对象
#     all_person_list.append(Person())
#
# Person.show_num()
#
# for i in range(15):                  # 删除15个对象
#     all_person_list.pop()
#
# Person.show_num()

"""
3.创建一个动物类，拥有属性：性别、年龄、颜色、类型 ，

要求打印这个类的对象的时候以
'/XXX的对象: 性别-? 年龄-? 颜色-? 类型-?/' 的形式来打印
"""


class Animal:
    def __init__(self,sex,age,color,kind):
        self.sex = sex
        self.age = age
        self.color = color
        self.kind = kind

    def show(self):
        print('{}的对象:性别-{} 年龄-{} 颜色-{} 类型-{}'.format(self.__class__.__name__,self.sex,self.age,self.color,self.kind))


a = Animal('公',3,'黑色','狗')

a.show()

"""
4.写一个圆类， 拥有属性半径、面积和周长；
要求获取面积和周长的时候的时候可以根据半径的值把对应的值取到。
但是给面积和周长赋值的时候，程序直接崩溃，并且提示改属性不能赋值
"""

# class Circle:
#     pi = 3.141592653
#
#     def __init__(self,r):
#         self.r = r
#         self._area = 0
#         self._perimeter = 0
#
#     @property
#     def area(self):
#         return Circle.pi * self.r ** 2
#
#     @area.setter
#     def area(self, value):
#         raise ValueError
#
#     @property
#     def perimeter(self):
#         return Circle.pi * self.r * 2
#
#     @perimeter.setter
#     def perimeter(self, value):
#         raise ValueError
#
#
# a = Circle(5)
# print(a.area)
# print(a.perimeter)
#
# # a.area = 100
# # a.perimeter = 100

"""
5.写一个扑克类， 
要求拥有发牌和洗牌的功能(具体的属性和其他功能自己根据实际情况发挥)
"""
# from random import *
#
#
# class Poker:
#
#     def __init__(self):
#         self.card_list = [i + str(j) for i in ['红桃', '黑桃', '方块', '梅花'] for j in range(2, 11)] + \
#         [i + j for i in ['红桃', '黑桃', '方块', '梅花'] for j in ['A', 'J', 'Q', 'K']]
#
#     def shuffle_card(self):
#         shuffle(self.card_list)
#
#     def get_card(self):
#         new_card = iter(self.card_list)
#         num = input('你想发几张牌:')
#         for _ in range(int(num)):
#             print(next(new_card))
#
#
# a = Poker()        # 生成牌对象
# a.shuffle_card()   # 打乱牌序
# a.get_card()       # 发牌


"""
6.(尝试)写一个类，其功能是：
1.解析指定的歌词文件的内容 
2.按时间显示歌词 提示：歌词文件的内容一般是按下面的格式进行存储的。
歌词前面对应的是时间，在对应的时间点可以显示对应的歌词
[00:00.20]蓝莲花   
[00:00.80]没有什么能够阻挡   
[00:06.53]你对自由地向往   
[00:11.59]天马行空的生涯  
[00:16.53]你的心了无牵挂   
[02:11.27][01:50.22][00:21.95]穿过幽暗地岁月   
[02:16.51][01:55.46][00:26.83]也曾感到彷徨   
[02:21.81][02:00.60][00:32.30]当你低头地瞬间  
[02:26.79][02:05.72][00:37.16]才发觉脚下的路   
[02:32.17][00:42.69]心中那自由地世界  
[02:37.20][00:47.58]如此的清澈高远   
[02:42.32][00:52.72]盛开着永不凋零   
[02:47.83][00:57.47]蓝莲花  
"""

