"""__author__=余婷"""

"""
1.类和对象的概念
类: 拥有相同功能和相同属性的对象的集合
对象: 类的实例

2.类的声明
class 类名:
    类的说明文档
    类中的属性
    类中的方法

3.对象的创建
类()

4.__init__方法

5.类的字段和对象属性
类的字段:
 
对象属性:

6.类中的方法
对象方法：
类方法：
静态方法：

7.对象属性的增删改查
"""


class Person:
    num = 61

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def message(self):
        print('%s说，人类的数量是:%d亿' % (self.name, Person.num))



