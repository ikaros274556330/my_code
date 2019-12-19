"""__author__=吴佩隆"""
import time
"""
时间戳:当前时间距离1970年1月1日0时0分0秒的时间差，单位是秒
"""

print(time.time())
# 获取当前时间的时间戳

time1 = time.time()

# localtime(时间戳) - 将时间戳转化为当地时间
time2 = time.localtime(time1)
print(time2)

'2019-11-26 14:15:00'

# 1.getter 和 setter
"""
1)什么时候用
如果希望在对象属性赋值前做点别的什么事情就给这个属性添加setter
如果希望在获取属性值之前做点别的什么事情就给这个属性添加getter

2)怎么用
getter
a.将需要添加getter的属性名前加_
b.声明函数:声明前加@property
            函数名必须是属性名不带_
            函数需要一个返回值,返回值就是获取属性得到的值
c.在外部使用属性的时候不带_


setter:
注意:如果想要给属性添加setter必须先添加getter
a.声明函数:声明前加@getter名.setter;
        函数名不带_的属性名;
        函数不需要返回值，但是需要一个参数，这个参数就是给属性赋的值

b.在外面给属性赋值的时候不带下划线
"""


class Person:
    def __init__(self, age: int):
        self._age = age
        self._time = 1574749600.202029

    @property
    def time(self):
        t_time = time.localtime(self._time)
        return time.strftime("%Y--%m--%d %H:%M:%S", t_time)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        print('value:', value)
        if isinstance(value, int):
            if 0 <= value <= 200:
                self._age = value
            else:
                raise ValueError
        else:
            raise ValueError


# p1 = Person(18)
# p1.age = 18
# p1.age = 'abc'

print('===========================================')

# print(p1.time)


class Circle:
    pi = 3.141592653

    def __init__(self, r):
        self.r = r
        self._area = 0

    @property
    def area(self):
        return Circle.pi * self.r ** 2

    @area.setter
    def area(self,value):
        print('给area属性赋值:', value)
        raise ValueError


c1 = Circle(1)
print(c1.area)

c1.r = 10
print(c1.area)

c1.area = 3.14
c1.area = 1000
