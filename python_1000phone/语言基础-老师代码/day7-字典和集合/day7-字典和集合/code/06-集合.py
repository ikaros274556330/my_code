"""__author__=余婷"""

# 1.什么是集合(set)
"""
集合是容器型数据类型，将{}作为容器标志里面多个元素用逗号隔开: {元素1, 元素2, 元素3,...}
可变的(支持增删改)、无序的(不支持下标操作)

集合中的元素: 不可变的，唯一的(自带去重)
"""
# 1.空集合
# 注意: {}表示空字典
x = {}
print(type(x))

# set1是一个空集合
set1 = set()

# 2.集合中的元素
set2 = {1, 2, 'hus', (10, 2)}
print(set2)

# 集合中的元素不可变
# set3 = {[1, 2], 2, 'hus'}    # TypeError: unhashable type: 'list'

# 集合中的元素是唯一的
set4 = {1, 2, 'hus', 1}
print(set4)    # {1, 2, 'hus'}


# 2.增删改查
# 1)查 - 遍历集合
set5 = {23, 3, 5, 67, 8}
for x in set5:
    print(x)


# 2)增
# a.添加单个元素: 集合.add(元素)  -  在集合中添加指定元素
set5.add(100)
print(set5)

# b.集合.update(序列)  -  将序列中所有的元素添加到集合中
set5.update('abc')
print(set5)

set5.update({'name': '小明', 'age': 18})
print(set5)

# 3).删 - 删除元素
# 集合.remove(元素)  - 删除集合中指定元素，元素不存在报错
# 集合.discard(元素) - 删除集合中指定元素, 元素不存在不报错
set5.remove(100)
print(set5)

set5.discard(67)
print(set5)
set5.discard(1000)

# 3.相关操作
# 1) in / not in
set5 = {23, 3, 5, 67, 8}
print(8 in set5)

# 2)len， set
# set(序列)  - 所有的序列都能转换成集合(元素不可变); 自动去重
list1 = [10, 23, 10, 25, 30, 12, 23]
list1 = list(set(list1))
print(list1)
