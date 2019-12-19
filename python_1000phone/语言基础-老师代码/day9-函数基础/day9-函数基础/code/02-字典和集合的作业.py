"""__author__=余婷"""

# 1.声明一个字典保存一个学生的信息，学生信息包括：姓名，年龄，成绩（单科），电话，性别（男女不明）
stu = {'name': '小明', 'age': 18, 'score': 89, 'tel': '1728272333', 'gender': '男'}

# 2.声明一个列表，在列表中保存6个学生的信息(6个题1中的字典)
students = [
    {'name': '小明', 'age': 18, 'score': 93, 'tel': '1728272338', 'gender': '男'},
    {'name': '小花', 'age': 30, 'score': 56, 'tel': '1728272335', 'gender': '女'},
    {'name': '小红', 'age': 16, 'score': 89, 'tel': '1728272338', 'gender': '不明'},
    {'name': 'Tom', 'age': 22, 'score': 93, 'tel': '1728272339', 'gender': '男'},
    {'name': '小炮', 'age': 17, 'score': 90, 'tel': '1728272334', 'gender': '女'},
    {'name': '托儿索', 'age': 6, 'score': 30, 'tel': '1728272337', 'gender': '男'}
]
print('=============不及格学生===========')
# a.统计不及格学生的个数
# b.打印不及格学生的名字和对应的成绩
count = 0
for stu in students:
    score = stu['score']
    if score < 60:
        count += 1
        print(stu['name'], score)
print('不及格学生的个数:' + str(count))


print('==============未成年学生===============')
# c.统计未成年学生的个数
count = 0
for stu in students:
    if stu['age'] < 18:
        count += 1
print('未成年学生的个数:%d' % count)

# d.打印手机尾号是8的学生的名字
print('手机尾号是8的学生:')
for stu in students:
    if stu['tel'][-1] == '8':
        print(stu['name'])


print('===============最高分==============')
# e.打印最高分和对应的学生的名字
# 方法一：只获取一个最高分对应的学生
max1 = students[0]    # 将第一个学生的分数设置为默认的最高分
for stu in students[1:]:
    if stu['score'] > max1['score']:
        max1 = stu
print(max1['score'], max1['name'])

# 方法二: 获取同时为最高分的多个学生
# [80， 79， 80， 84， 85， 70， 85]
"""
max_score= 85
max_students = [4, 6]
"""
max_score = students[0]['score']   # 最大分数
max_students = [students[0]['name']]       # 最高分对应的所有的学生的名字
for stu in students[1:]:
    # 如果分数和最高分相等：就将名字直接添加到列表中
    if stu['score'] == max_score:
        max_students.append(stu['name'])

    # 如果分数大于最高分, 清空原来的最高分对应的名字，添加新的名字
    elif stu['score'] > max_score:
        max_score = stu['score']
        max_students.clear()
        max_students.append(stu['name'])

print('最高分{}, 对应的学生有:{}'.format(max_score, str(max_students)[1:-1]))

# f.将列表按学生成绩从大到小排序(挣扎一下，不行就放弃)
# 方法一: 高阶函数
# students.sort(reverse=True, key=lambda item: item['score'])
# print(students)

# 方法二: 选择排序:
"""
第一轮: 获取整个序列中的最小值放到第一位
第二轮: 从除了第一位以外的元素中选出第二小的值放到第二位
...
"""
# nums = [8, 3, 5, 1]
# length = len(nums)
# for index1 in range(length-1):
#     for index2 in range(index1+1, length):
#         if nums[index2] > nums[index1]:
#             nums[index1], nums[index2] = nums[index2], nums[index1]
# print(nums)

length = len(students)
for index1 in range(length-1):
    for index2 in range(index1+1, length):
        if students[index2]['score'] > students[index1]['score']:
            students[index1], students[index2] = students[index2], students[index1]

print(students)

# g.删除性别不明的所有学生
for stu in students[:]:
    if stu['gender'] == '不明':
        students.remove(stu)
print(students)

# 3.用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
python = {'stu1', 'stu2', 'stu5', 'stu6', 'stu8', 'stu9'}
java = {'stu1', 'stu3', 'stu4', 'stu6'}
h5 = {'stu1', 'stu3', 'stu5', 'stu6', 'stu7', 'stu9'}
# 	a. 求选课学生总共有多少人
set1 = python | java | h5
print('选课所有学生:', set1)

#  	b. 求只选了第一个学科的人的数量和对应的名字
set2 = python - java - h5
print('第一个学科的人的名字:', set2)

# 	e. 求选了三门学生的学生的数量和对应的名字
set3 = python & java & h5
print('选了三门学生的学生:', set3)

#  	d. 求只选了两门学科的学生的数量和对应的名字
set4 = ((python & java) | (python & h5) | (java & h5)) - set3
print('只选了两门学科的学生:', set4)

# 	c. 求只选了一门学科的学生的数量和对应的名字
set5 = set1 - set3 - set4
print('只选了一门学科的学生:', set5)










