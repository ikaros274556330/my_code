"""__author__=余婷"""

# 1.什么是列表(list)
"""
1)列表
列表是python提供的一种容器型数据类型; 以[]作为容器的标志，里面多个元素用逗号隔开: [元素1, 元素2, 元素3,...]
列表是可变的(元素个数、元素的值可变) - 元素支持增、删、改操作；有序的 - 支持下标操作

2)列表元素
列表中的元素可以是任何类型的数据; 同一个列表中的元素的类型可以不一样
[12, 12.8, True, "abc", [1, 2], (10, 100), {1, 2}, {"name": 100}]

a = 100
[10, a, a + 2]
"""
list1 = [1, 2, 3, 4, 1]
print(list1)

list2 = ['张三', 18, 89.5, True]
print(list2)

list3 = [12, 12.0, '张三', True, [1, 2], {'name': '小敏', 'age': 20}, lambda x: x*2]
print(list3)

# 2.查 - 获取列表中的元素
"""
1)获取单个元素
a.语法: 
列表[下标]     --   获取列表中指定下标对应的元素

b.说明
列表      -    列表值, 保存列表的变量, 结果是列表的表达式
[]       -    固定写法
下标      -    列表中的每个元素都会对应一个下标,来表示这个元素在列表中的位置。
              下标范围: 0 ~ 列表长度-1   -  从前往后依次增加(0表示第一个元素)
                       -1 ~ -列表疮毒   -  从后往前依次递减(-1表示最后一个元素)

注意: 下标不能越界!
"""
list4 = [10, 100, 1000]
print([1, 2, 3, 4][-1])     # 获取列表[1, 2, 3, 4]的最后一个元素
print(list4[1])             # 获取列表list4下标是1的元素
print(([1, 2, 3]+['a', 'b', 'c'])[-2])


"""
2)获取部分元素(切片)  
a.语法1
列表[开始下标:结束下标:步长] - 从开始下标开始获取，下标值每次增加步长去获取下一个元素，到结束下标前位置

注意: 列表切片的结果还是列表，新列表中的元素是原列表元素的一部分

b.说明:
如果步长为正，是从前往后取；那么开始下标所在位置必须在结束下标所在的位置的前面，否则取不到元素([])
如果步长为负，是从后往前取；那么开始下标所在的位置必须在结束下标所在的位置的后面，否则取不到元素([])
"""
list1 = ['路飞', '娜美', '山治', '索罗', '乌索普', '乔巴']
print(list1[1])
print(list1[1:4:1])    # ['娜美', '山治', '索罗']
print(list1[5:0:-1])   # ['乔巴', '乌索普', '索罗', '山治', '娜美']
print(list1[0:5:2])    # ['路飞', '山治', '乌索普']
print(list1[5:3:1])    # []
print(list1[-1:3:1])   # []


"""
2)切片 - 省略下标和步长
a.省略步长:      列表[开始下标:结束下标]   -  相当于步长是1 
b.省略开始下标:   
列表[:结束下标:步长] / 列表[:结束下标]    -  如果步长为正从第一个元素开始往后取；
                                         如果步长为负从最后一个开始往前取
c. 省略结束下标
列表[开始下标::步长] / 列表[开始下标:]    - 从该方向取到最后一个元素

d. 省略开始下标和结束下标
列表[::步长] / 列表[:]                  -  
"""
list1 = ['路飞', '娜美', '山治', '索罗', '乌索普', '乔巴']
print(list1[1:4])     # ['娜美', '山治', '索罗']
print(list1[:4:2])    # ['路飞', '山治']
print(list1[:3:-1])   # ['乔巴', '乌索普']
print(list1[:3])      # ['路飞', '娜美', '山治']
print(list1[3:])      # ['索罗', '乌索普', '乔巴']
print(list1[3::-1])   # ['索罗', '山治', '娜美', '路飞']
print(list1[::2])     # ['路飞', '山治', '乌索普']
print(list1[::-1])    # ['乔巴', '乌索普', '索罗', '山治', '娜美', '路飞']
print(list1[:])       # ['路飞', '娜美', '山治', '索罗', '乌索普', '乔巴']


"""
3)遍历列表  - 将列表中的元素一个一个的取出来
a.直接遍历获取元素
for 变量 in 列表:
    循环体
    
b.通过遍历下标来遍历
length = len(列表)
for 变量 in range(length):
    元素 = 列表[变量]
"""
# 1)直接变量
movies = ['暮光之城', '哪吒之魔童降世', '少年的你', '速度与激情', '肖生克的救赎', '摔跤吧爸爸']
for x in movies:
    print(x)

# 2)通过下标去遍历
length = len(movies)
print('============顺着取==============')
for index in range(length):
    print(movies[index])

print('============倒着取==============')
for index in range(-1, -length-1, -1):
    print(movies[index])

# 下标越界!
# print(movies[6])    # IndexError: list index out of range
# print(movies[-10])  # IndexError: list index out of range

# 注意: 切片的时候下标可以越界
print(movies[1:100])
# 136 7819 2302








