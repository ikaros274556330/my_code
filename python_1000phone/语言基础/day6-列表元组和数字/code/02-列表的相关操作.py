"""__author__=吴佩隆"""

# 1.数学运算
# 1)数学运算符:+，*

# 列表1 + 列表2 -> 产生一个新列表,新列表是1和2的合并
list1 = [1, 2, 3]
list2 = ['张三', '李四']
print(list1 + list2)

# 列表 * N / N * 列表 -> 列表中的元素重复N次,产生一个新列表
print(list1*3)

# 2)比较运算:(必须一模一样才True,位置不对也False)
# ==,!=
# 列表1 == 列表2 -> 判断两个列表的值是否相等
list3 = [1, 2, 3]
list4 = [2, 1, 3]
print(list3 == list4)

# is
# 变量1 is 变量2 -> 判断地址，is 就是直接判断id(变量)是否相等

# >,<,>=,<=(了解)
# 两个列表依次比较相同位置元素,得出答案返回结果，相等就依次比较后面元素
print([1, 2, 3, 100] > [10, 20])  # False

# 2.in 和 not in
"""
元素 in 列表 -> 判断列表中是否存在指定元素
元素 not in 列表 -> 判断列表中是否不存在指定元素
"""

names = ['小明', '小花', '小红', '小蓝']
print('小红' in names)    # True
print('雷军' in names)    # False

# 3.相关函数(len、max、min、list、sum)
# 1)len(序列) - 获取序列的长度(元素的个数)

# 2)max(序列)/min(获取序列中元素的最大值/最小值)
# 要求:a.序列中所有的元素的类型一致(数字看成一种类型) b.元素本身必须支持比较大小
scores = [23, 89, 78, 12, 91]
print(max(scores))
print(min(scores))

# 3)sum
# sum(数字序列) - 求序列中所有元素的和
print(sum(range(101)))

# 4)list
# list(序列数据) - 将指定的数据转换成列表;数据必须是序列
print(list('abc'))
print(list(range(10, 15)))

