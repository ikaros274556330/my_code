"""__author__=余婷"""

films = ['一人之下', '一拳超人', '不良人', '死亡笔记']
print(films)

# 1.增 - 添加元素
"""
1)列表.append(元素)  -  在指定的列表的末尾添加一个元素
2)列表.insert(下标, 元素)   -  在列表指定下标前插入指定元素
"""
# 1)append
films.append('秦时明月')
print(films)

films.append('海贼王')
print(films)

# 2)insert
films.insert(1, '柯南')
print(films)

# 2.删  - 删除列表元素
# 1) del 列表[下标]   -  删除指定下标对应的元素(下标不能越界)
films = ['一人之下', '柯南', '一拳超人', '不良人', '死亡笔记', '秦时明月', '海贼王']
del films[2]
print(films)

# 2) 列表.remove(元素)   -  删除列表中指定元素
# 注意:a.如果元素不存在会报错!  b.如果元素在列表中有多个，只删第一个
# films.remove('你好')    # ValueError: list.remove(x): x not in list
nums = [10, 2, 45, 2, 9]
nums.remove(2)
print(nums)    # [10, 45, 2, 9]

nums.remove(45)
print(nums)    # [10, 2, 9]

# 3)
# 列表.pop()     -   取出列表中最后一个元素, 返回被取出的元素
# 列表.pop(下标)    -   取出列表中指定下标对应的元素，返回被取出的元素
nums = [10, 2, 45, 2, 9]
del_num = nums.pop()
print(nums)    # [10, 2, 45, 2]
print(del_num)

nums = [10, 2, 45, 2, 9, -2]
del_num = nums.pop(-2)
print(nums)   # [10, 2, 45, 9]
print(del_num)

# 练习: 删除下面这个列表中所有小于60的元素
# [89, 90, 78, 60, 87]
scores = [89, 45, 56, 20, 90, 78, 60, 23, 87, 20, 50]
# temp = scores[:]
for num in scores[:]:
    if num < 60:
        scores.remove(num)
print(scores)

# 3.改 - 修改元素的值
# 列表[下标] = 值   -  将列表中指定下标对应的元素修改成指定的值
nums = [10, 2, 45, 2, 9, -2]
nums[0] = 100
print(nums)

# 练习: 将scores中所有小于60的分数换成'不及格'
scores = [89, 45, 56, 20, 90, 78, 60, 23, 87, 20, 50]

for index in range(len(scores)):
    if scores[index] < 60:
        scores[index] = '不及格'

print(scores)
