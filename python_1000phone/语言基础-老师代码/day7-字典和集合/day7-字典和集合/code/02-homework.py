"""__author__=余婷"""


print('================第1题==================')
# 1.实现count的功能
names = ['曹操', '刘备', '司马懿', '吕布', '曹操']
name = '曹操'
count = 0
for x in names:
    if x == name:
        count += 1
print(count)


print('================第2题==================')
# 2.列表.extend(序列) - 将序列中的元素全部添加的列表中
names = ['曹操', '刘备', '司马懿', '吕布', '曹操']
# seq = 'hello'
# seq = [10, 20]
seq = (1, 200)
for x in seq:
    names.append(x)
print(names)


print('================第3题==================')
# 3.列表.index(元素) -> 获取指定元素在列表中的下标
names = ['曹操', '刘备', '司马懿', '吕布', '曹操']
item = '小乔'
for index in range(len(names)):
    if names[index] == item:
        print(index)
        break
else:
    # raise ValueError
    print('列表中没有该元素!')


print('================第4题==================')
# 4.列表.reverse() - 将原来的序列倒序过来（反过来）
# nums = [10, 20, 3, 40, 50]    # 5
# 0, 4;  1, 3     range(len//2)
# nums = [10, 20, 3, 40, 50, 4, 89]   # 7
# 0, 6;  1,5;  2,4
nums = [10, 20, 3, 40, 50, 4]    # 6
# 0, 5; 1, 4;  2, 3;
length = len(nums)
for x in range(length//2):
    y = length - 1 - x
    nums[x], nums[y] = nums[y], nums[x]
print(nums)



