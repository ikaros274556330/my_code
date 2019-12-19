"""__author__=余婷"""


# 0.什么时候使用
"""
如果需要同时保存多个数据  ->  序列(容器型数据类型)
如果要保存的多个数据是相同意义的数据(数据之间不需要区分)   ->  列表
如果要保存的多个数据的意义不同(数据之间需要分区)   ->    字典
"""
student = ['余婷', 18, '女', 155, 50, 89]
student1 = ['张三', 50, '男', 170, 50, 45]
print(student[1])
print(student1[-1])

student2 = {'name': '余婷', '年龄': 18, '性别': '女', '身高': 155, '体重': 50, '成绩': 89}
print(student2['年龄'])
print(student2['成绩'])

# 1.什么是字典(dict)
"""
a.什么是字典
字典是容器型数据类型, 将{}作为容器的标志,里面多个元素用逗号隔开，但是字典中的元素是键值对: {键1:值1, 键2:值2,...}
可变的(支持增删改), 无序(不支持下标操作)

b.键值对
字典中的所有元素都必须是键值对, 键和值必须成对出现; 字典存数据存的是值，键是用来区分和说明不同的值的
键 - 任意不可变的数据都可以作为键， 实际开发的时候一般将字符串做为key；键是唯一的
值 - 任何类型的数据都可以作为字典的value
"""
dict1 = {'abc': 19, 'a': True, 'b': [1, 2], 'c': {'name': '小明'}}
print(dict1)

# 键是不可变
dict2 = {10: 100, 'a': 200, (1, 2): 300}
# dict3 = {10: 100, 'a': 200, ['a': 10]: 300}     # TypeError: unhashable type: 'list'
# key是唯一的
dict4 = {'a': 10, 'a': 100, 'b': 20}
print(dict4)    # {'a': 100, 'b': 20}


# 2.字典的增删改查
# 1)查  - 获取字典的值
"""
a.获取单个值
字典[key]  -  获取字典中指定key对应的值, 如果key不存在会报错
字典.get(key)  -  获取字典中指定key对应的值, 如果key不存在不会报错，并且返回None
字典.get(key, 默认值)   -  获取字典中指定key对应的值, 如果key不存在不会报错, 并且返回指定的默认值
"""
person = {'name': '小明', 'age': 20, 'tel': '1530002273'}
print(person['tel'])
# print(person['height'])   # KeyError: 'height'

print(person.get('age'))
print(person.get('height'))       # None
print(person.get('height', 0))    # 0

"""
b.遍历
for key in 字典:
    循环体
"""
# 推荐使用这种方式遍历
for x in person:
    print('x:', x, person[x])


# 其他的遍历方式(不要写这样的代码)
for key, value in person.items():
    print(key, value)
print(person.items())

# list1 = []
# for key in person:
#     tuple1 = (key, person[key])
#     list1.append(tuple1)
# print(list1)
# for key, value in list1:
#     print(key, value)

# 3.增/改
"""
字典[key] = 值   -  当key存在的时候，修改字典指定key对应的值;当key不存在的时候，添加'key:值'的键值对
"""
person = {'name': '小明', 'age': 20, 'tel': '1530002273'}
person['name'] = '小花'
print(person)
person['score'] = 90
print(person)

# 4.删  -  删除键值对
"""
1) del 字典[key]   -  删除字典中指定key对应的键值对
2) 字典.pop(key)   -  取出字典中指定key对应的值(key对应的键值对会从字典中消失)
"""
person = {'name': '小花', 'age': 20, 'tel': '1530002273', 'score': 90}
del person['age']
print(person)

name = person.pop('name')
print(person, name)


# 练习: 保存一个班所有的学生的信息(姓名、学号、年龄、成绩、电话; 假设一般5个人)
all_student = [
    {'name': '小明', 'age': 28, 'score': 90, 'tel': '1828333333'},
    {'name': '小红', 'age': 16, 'score': 78, 'tel': '16253723283'},
    {'name': 'Tom', 'age': 21, 'score': 23, 'tel': '12623378293'},
    {'name': 'Bom', 'age': 17, 'score': 98, 'tel': '13572378237'},
    {'name': '大黄', 'age': 30, 'score': 76, 'tel': '18923672368'}
]

# 1)统计以上学生中不及格学生的人数
count = 0
for student in all_student:
    if student['score'] < 60:
        count += 1
print('不及格学生的人数:', count)


# 2)将打印所有未成年人学生的姓名
print('未成年学生:')
for student in all_student:
    if student['age'] < 18:
        print(student['name'])


# 3)将年龄为25岁以上的学生的电话号码设置为'保密'
for student in all_student:
    if student['age'] > 25:
        student['tel'] = '保密'
print(all_student)







