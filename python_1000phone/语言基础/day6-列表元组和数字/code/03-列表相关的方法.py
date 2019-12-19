"""__author__=吴佩隆"""

names = ['曹操', '刘备', '诸葛亮', '小乔', '貂蝉', '刘备', '刘备']
# 1.列表.count(元素) -> 统计列表中指定元素的个数
print(names.count('刘备'))

# 2.列表.extend(序列) - 将序列中的元素全部添加到列表中
# 用+拼接会产生新列表，extend则不会
names.append('华佗')
print(names)

names.extend('黄盖')
print(names)

# 3.列表.index(元素) -> 获取指定元素在列表中的下标
# a.如果元素不存在会报错
# b.如果元素有多个，只会返回第一个

nums = [10, 3, 50, 3, 90]
print(nums.index(3))

# 4.列表.reverse() -> 将原来列表倒叙
# 列表[::-1]产生新序列，reverse()不会
nums = [1, 9, 3]
nums.reverse()
print(nums)

# 5.列表.clear() -> 清空列表

# 注意:清空列表用clear,直接赋值位[]
nums = [1, 2, 3]
nums.clear()
print(nums)

# 6.列表.copy() -> 复制列表中的元素，产生一个新的列表，将新列表地址返回，赋值后两个不影响
# 列表1 == 列表2  -  直接赋值，两个列表相互影响
# copy()和列表[:]的功能一模一样，都属于浅拷贝

# 7.列表.sort() -> 将列表中的元素从小到大排序(直接修改列表元素的顺序，不会产生新列表)
# 列表.sort(reverse=True) -> 从大到小排序,不产生新列表
# 列表.sort(reverse=True) 相当于 列表.sort();列表.reverse()
scores = [1, 8, 9, 4, 6, 3, 1, 8, 9]
scores.sort()
print(scores)

# 8.排序函数:sorted(序列) -> 不修改原序列，从小到大排序后创建新列表
#           sorted(序列,reverse=True) -> 不修改原列表,从大到小排序创建新列表

str1 = 'hello'
new_str1 = sorted(str1)
print(new_str1)         # ['e', 'h', 'l', 'l', 'o'] 只会产生列表

# reversed(序列) -> 将序列中的元素倒叙，产生一个新的序列对应的迭代器


