"""__author__=余婷"""

# 1.什么是迭代器(iter)
"""
迭代器也是python提供的容器型数据类型

迭代器存储数据的特点: 一个迭代器可以存储多个数据，如果要获取元素必须将元素从迭代器中取出，而且取一个就少一个；
取出来的数据不能再添加到迭代器中

"""
# 2.将数据存入迭代器中: 1)将别的序列转换成迭代器   2)创建生成器
list1 = [10, 20, 30, 40]
iter1 = iter(list1)
print(iter1)   # <list_iterator object at 0x110190400>
# print(len(iter1))   # TypeError: object of type 'list_iterator' has no len()

iter2 = iter('hello')
print(iter2)    # <str_iterator object at 0x109be0550>

# 3.获取迭代器中的元素
"""
迭代器中的元素不同通过什么方式取出来了，那么这个元素在迭代器中就不存在了

1)获取单个元素:
next(迭代器)  -> 取出迭代器中最前面的元素
"""
print(next(iter1))   # 10
print(next(iter1))   # 20
print(next(iter1))   # 30
print(next(iter1))   # 40
# print(next(iter1))   # StopIteration

# 2)遍历 - 一个一个的取所有的元素
for x in iter2:
    print('x:', x)

# print(next(iter2))    # StopIteration

print('=================')
iter3 = iter('python')
next(iter3)
next(iter3)
for y in iter3:
    print('y:', y)

iter4 = iter('python')
list2 = list(iter4)
print(list2)
print(next(iter4))    # StopIteration