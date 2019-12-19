"""__author__=余婷"""
from sys import getrefcount

# 1.内存管理基础(C)
"""
内存分为栈区间和堆区间， 栈区间的内存是系统自动申请自动释放；堆上的内存需要程序通过调用malloc函数去申请，通过调用free函数去释放;
高级语言(java\C++\OC\Python)中的内存管理机制，都是针对堆上的内存的管理进行的自动化操作
"""
# 2.Python的内存管理机制
"""
1)内存的申请
python中所有的数据都是存在堆中的，变量是保存在栈区间的，变量中保存的是保存在堆中的数据的地址。
重新给变量赋值，会先在内存开辟新的内存保存新的数据，然后将新的数据的地址重新保存到变量
但是如果使用数字或者字符串给变量赋值,不会直接开辟新的内存，而是先检查内存有没有这个数据，如果有直接将原来的数据的地址给变量

2)内存的释放(垃圾回收机制)
在python中一个数据对应的内存空间是否释放，就看这个数据的引用计数是否为0；如果引用计数为0，数据对应的内存就会被自动释放
循环引用问题: python的垃圾回收机制会自动处理循环引用问题

增加引用计数: 增加数据的引用(让更多的变量来保存数据的地址)
减少引用计数: 删除引用，或者让引用去保存新的数据
"""
print('======================内存申请====================')
a = 10
print(id(a))
a = 100
print(id(a))

b = []
print(id(b))     # 4495144200
b = []
print(id(b))     # 4495187272

c = {'a': 10}
print(id(c))     # 4493576304
c = {'a': 10}
print(id(c))     # 4493576376

d = 100
print(id(d))   # 4491424800
d = 100
print(id(d))   # 4491424800

e = 'abc'
print(id(e))   # 4484038984
e = 'abc'
print(id(e))   # 4484038984

print('=========================内存释放======================')
list1 = [1, 2, 3]    # re: 1
print(getrefcount(list1))  # 2

list2 = list1
print(getrefcount(list1))   # 3

dict1 = {'a': list1}
print(getrefcount(list1), getrefcount(list2))   # 4

del list1
print(getrefcount(list2))    # 3

dict1['a'] = 'abc'
print(getrefcount(list2))    # 2


# 循环引用
list1 = [1, 2, 3]
list2 = [list1, 10, 20]
list1.append(list2)

del list1
del list2


class Person:
    pass


Person()

list3 = [[100, 200], 20, 30, 40]
# del list3[0]
list3.pop(0)


num = 6
print(getrefcount(num))