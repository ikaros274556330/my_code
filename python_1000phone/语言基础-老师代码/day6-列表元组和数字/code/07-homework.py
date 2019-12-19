"""__author__=余婷"""

# 6.有一个长度是10的列表，数组内有10个人名，要求去掉重复的
# 例如:names = ['张三', '李四', '大黄', '张三'] -> names = ['张三', '李四', '大黄']
# 方法一:
names = ['张三', '张三', '张三', '李四', '李四','大黄', '张三', '小明', '张三','李四']
index = 0
while index < len(names):
    n1 = names[index]
    index2 = index + 1
    while index2 < len(names):
        if n1 == names[index2]:
            del names[index2]
            continue
        index2 += 1

    index += 1

print(names)

# 方法二
names = ['张三', '张三', '张三', '李四', '李四','大黄', '张三', '小明', '张三','李四']
names = list(set(names))
print(names)


# 8.用一个列表来保存一个节目的所有分数，求平均分数(去掉一个最高分，去掉一个最低分，求最后得分)
list9 = [60, 70, 89, 90, 88, 92, 97, 95]
sum1 = 0
max1 = list9[0]
min1 = list9[0]
for num in list9:
    # 求和
    sum1 += num
    # 求最大值
    if num > max1:
        max1 = num
    # 求最小值
    if num < min1:
        min1 = num

print((sum1-max1-min1)/(len(list9)-2))


