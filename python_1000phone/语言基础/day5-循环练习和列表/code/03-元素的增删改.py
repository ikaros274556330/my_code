"""__author__=吴佩隆"""

list_1 = ['a', 'b', 'c', 'd']
print(list_1)

# 1.增 - 添加元素
"""
1)列表.append(元素) - 在指定列表末尾添加元素
2)列表.insert(下标,元素) - 在列表指定下标前插入指定元素
"""

list_1.append('e')
print(list_1)

list_1.insert(2, 'f')
print(list_1)

# 2.删 - 删除列表元素

# 1)del 列表[下标] - 删除指定下标的元素(下标不能越界)


del list_1[1]
print(list_1)

# 2)列表.remove(元素) - 删除列表中指定元素
# 注意:a.如果元素不存在会报错   b.如果指定元素有多个只会删除第一个

list_1.remove('d')
print(list_1)

# 3)
# 列表.pop()  -   取出列表中最后一个元素，返回被取出的元素
# 列表.pop(下标)    -   取出列表中指定下标对应的元素，返回被取出的元素

del_num = list_1.pop(1)
print(list_1)
print(del_num)

# 练习：删除下面列表中所有小于60的元素

scores = [89, 45, 56, 20, 90, 78, 60, 23, 87, 20, 50]

for i in scores[:]:
    if i < 60:
        scores.remove(i)

print(scores)

# 3.改 - 修改元素的值
# 列表[下标] = 值    -   将列表中指定下标对应的元素修改成指定的值


# 练习：将下面列表中低于60分的换成’不及格‘

scores = [89, 45, 56, 20, 90, 78, 60, 23, 87, 20, 50]

for i in range(len(scores)):
    if scores[i] < 60:
        scores[i] = '不及格'

print(scores)