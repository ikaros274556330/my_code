"""__author__=余婷"""

"""
1.私有化
2.getter和setter
3.继承
"""


# 自定义错误类型:
# 要求这个类必须继承Exception
class ReadOnlyError(Exception):
    # __str__返回值就是错误信息描述
    def __str__(self):
        return '给只读属性赋值！'


class Person:
    def __init__(self):
        self._name = 'xiaoming'

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        raise ReadOnlyError
        print(value)
        self._name = value


p = Person()
print(p.name)

# p.name = '小花'


class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class B(A):
    def __init__(self, a=0, b=1, c=2, d=3):
        super().__init__(a, b, c)
        self.d = d


b1 = B(1, 2, 3, 4)
print(b1.d, b1.a)


b1 = B(10, 20, 30, 40)
print(b1.d, b1.a)

print(B.__mro__)