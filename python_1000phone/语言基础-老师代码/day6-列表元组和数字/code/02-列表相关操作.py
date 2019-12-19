"""__author__=余婷"""

# 1.运算符
# 1）数学运算符: +, *
# 列表1 + 列表2  ->  产生一个新的列表,新列表中的元素是两个列表中元素的合并
list1 = [1, 2, 3]
list2 = ['张三', '李四']
print(list1 + list2)

# 列表 * N / N * 列表  ->  列表中的元素重复N次，产生一个新的列表
print(list1 * 3)

# 2)比较运算:
# ==, !=
# 列表1 == 列表2   -> 判断两个列表的值是否相等
list3 = [1, 2, 3]
list4 = [2, 1, 3]
print(list3 == list4)   # False

list4 = [1, 2, 3]
print(list3 == list4)  # True

# is
# 变量1 is 变量2    ->  判断地址是否相等
li1 = [1, 2]
li2 = [1, 2]
print(li1 == li2)
print(li1 is li2)    # print(id(li1) == id(li2))


# >, <, >=, <= (了解)
print([30, 20, 3, 100] > [10, 20000])    # True


print('================in/not in================')
# 2. in和not in
"""
元素 in 列表       ->   判断列表中是否存在指定的元素
元素 not in 列表   ->   判断列表中是否不存在指定的元素
"""
names = ['小明', '小花', '小红', '张三']
print('小红' in names)      # True
print('李四' in names)      # False
print(['小明'] in names)    # False


print('==================相关函数=================')
# 3.相关函数:len、max、min、list、sum
# 1)len(序列)  - 获取序列的长度(元素的个数)
print(len([1, 2, 3]))   # 3
print(len('hello'))   # 5

# 2) max/min
# max(序列)/min(序列)  -> 获取序列中元素的最大值/最小值
# 序列的要求:a.序列中所有的元素的类型一致(数字看成一种类型)  b.元素本身支持比较大小
scores = [23, 89, 89, 78, 90, 91, 12]
print(max(scores))   # 91
print(min(scores))   # 12

scores = [23, '100', 90, '23']
# print(max(scores))    # TypeError: '>' not supported between instances of 'str' and 'int'

# 3) sum
# sum(数字序列)  -> 求序列中所有元素的和
scores = [1, 2, 3]
print(sum(scores))
print(sum(range(101)))

# 4) list
# list(数据)   -> 将指定的数据转换成列表; 数据必须是序列(所有的序列都可以转换成列表)
# print(list(100))   # TypeError: 'int' object is not iterable
print(list('hello'))   # ['h', 'e', 'l', 'l', 'o']
print(list(range(10, 15)))   # [10, 11, 12, 13, 14]




