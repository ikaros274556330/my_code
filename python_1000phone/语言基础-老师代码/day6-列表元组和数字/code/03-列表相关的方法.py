"""__author__=余婷"""


names = ['赵云', '小乔', '貂蝉', '吕布', '诸葛亮', '司马懿', '小乔']
# 1.列表.count(元素)  ->  统计列表中指定元素的个数
print(names.count('赵云'))    # 1
print(names.count('大乔'))    # 0
print(names.count('小乔'))    # 2

# 2.列表.extend(序列)  - 将序列中的元素全部添加到列表中
names.append('后裔')
print(names)   # ['赵云', '小乔', '貂蝉', '吕布', '诸葛亮', '司马懿', '小乔', '后裔']
names.extend('后裔')
print(names)   # ['赵云', '小乔', '貂蝉', '吕布', '诸葛亮', '司马懿', '小乔', '后裔', '后', '裔']
# names.append([1, 2])
# print(names)   # ['赵云', '小乔', '貂蝉', '吕布', '诸葛亮', '司马懿', '小乔', '后裔', '后', '裔', [1, 2]]
names.extend([1, 2])
print(names)    # ['赵云', '小乔', '貂蝉', '吕布', '诸葛亮', '司马懿', '小乔', '后裔', '后', '裔', 1, 2]

# 3.列表.index(元素)   ->   获取指定元素在列表中的下标(下标值是0 ~ 长度-1)
# a.如果元素不存在会报错
# b.如果元素有多个
nums = [10, 3, 50, 3, 90]
# print(nums.index(100))    # ValueError: 100 is not in list
print(nums.index(3))   # 1
print(nums.index(50))  # 2


# 4.列表.reverse()   ->  将原来的列表倒序(反过来)
nums = [1, 9, 3]
nums.reverse()
print(nums)   # [3, 9, 1]

nums = [1, 9, 3]
new_nums = nums[::-1]
print(nums, new_nums)    # [1, 9, 3] [3, 9, 1]

# 5.列表.clear()   -> 清空列表
nums = [10, 3, 50, 3, 90]
nums.clear()
print(nums)

# 注意: 清空列表用clear， 而不是直接赋值为[]
nums = [10, 3, 50, 3, 90]
nums = []
print(nums)

# 6.列表.copy()  -> 复制列表中的元素，产生一个新的列表, 将新列表的地址返回。赋值后两个相互不影响
# 和列表[:]的功能一模一样， 都属于浅拷贝
heros = ['后裔', '甄姬', '凯', '庄周', '蔡文姬']
# 直接赋值，赋值后两个列表相互影响
heros2 = heros
print(heros2)   # ['后裔', '甄姬', '凯', '庄周', '蔡文姬']
del heros2[-1]
print(heros2)   # ['后裔', '甄姬', '凯', '庄周']
print(heros)    # ['后裔', '甄姬', '凯', '庄周']


heros = ['后裔', '甄姬', '凯', '庄周', '蔡文姬']
heros2 = heros.copy()
print(heros2)   # ['后裔', '甄姬', '凯', '庄周', '蔡文姬']
del heros2[-1]
print(heros2)   # ['后裔', '甄姬', '凯', '庄周']
print(heros)    # ['后裔', '甄姬', '凯', '庄周', '蔡文姬']


# 7. 列表.sort()  ->  将列表中的元素从小到大排序(直接修改列表元素的顺序，不会产生新的列表)
#    列表.sort(reverse=True)   -> 将列表中的元素从大到小排序(直接修改列表元素的顺序，不会产生新的列表)
#    列表.sort(reverse=True)  相当于  列表.sort(); 列表.reverse()
scores = [89, 78, 90, 56, 76, 30]
scores.sort()
print(scores)

scores = [89, 78, 90, 56, 76, 30]
scores.sort(reverse=True)
print(scores)


# 8.排序函数: sorted(序列)  ->  不修改原序列，排序后产生一个新的列表（从小到大,升序）
#            sorted(序列, reverse=True)  ->  不修改原序列，排序后产生一个新的列表(从大到小， 降序)
scores = [89, 78, 90, 56, 76, 30]
new_scores = sorted(scores)
print(scores)   # [89, 78, 90, 56, 76, 30]
print(new_scores)   # [30, 56, 76, 78, 89, 90]

str1 = 'hello'
new_str1 = sorted(str1)
print(new_str1)     # ['e', 'h', 'l', 'l', 'o']

# reversed(序列)  -> 将序列中的元素倒序，产生一个新的序列对应的迭代器(了解)
# new_str2 = reversed('abc')
# str2 = ''
# for x in new_str2:
#     str2 += x
# print(str2)






