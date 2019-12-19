"""__author__=吴佩隆"""


# 0.什么时候使用
"""
如果需要同时保存多个数据 -> 序列(容器型数据类型)
如果要保存的多个数据是相同意义的数据(数据不需要区分) -> 列表
如果要保存的数据意义不同(数据之间需要区分) -> 字典
"""
# 1.什么是字典(dict)

"""
a.什么是字典
字典是容器型数据类型，将{}作为容器的标志，
里面多个元素用逗号隔开，字典中元素是键值对:{键1:值1,键2:值2,...}
可变的(支持增删改)，无序(不支持下标操作)

b.键值对
字典中所有元素都必须是键值对，键和值必须成对出现;
字典存数据存的是值，键只是用来区分和说明不同的值
键 - 任意不可变数据都可以作为键，实际开发的时候一般将字符串作为key;键是唯一的
值 - 任何类型的数据都可以作为字典的value
"""

dict1 = {'abc': 19, 'a': True, 'b': [1, 2], 'c': {'name': '小明'}}
print(dict1)

# 键是不可变的
dict2 = {10: 100, 'a': 200, (1, 2): 300}
# dict3 = {10:100,'a':200,{'a':100}:300} TypeError: unhashable type: 'dict'

# 2.字典的增删改查
# 1）查 - 获取字典的值
"""
a.获取单个值
字典[key] - 获取字典中指定key对应的值,如果key不存在会报错
字典.get(key) - 获取字典中指定key对应的值,如果key不存在返回None
字典.get(key,默认值) - 获取字典中指定key对应的值,如果key不存在返回默认值
"""
person = {'name': '小明', 'age': 20, 'tel': '13888888888'}
print(person['tel'])
print(person.get('tel'))
print(person.get('height'))  # None
print(person.get('height', 0))  # 0

"""
b.遍历
for key in 字典:
    循环体
"""
for key in person:
    print(key, person[key])

# 同样效果,但效率极低,多消耗一次遍历资源
# for key, value in person.items():
#     print(key, value)

# 3.增/改
"""
字典[key] = 值   -   当key存在，修改指定的值,不存在就添加
"""
person['name'] = '小花'
print(person)

person['score'] = 87
print(person)

# 4.删 - 删除键值对
"""
1)del 字典[key] - 删除字典中指定key对应的键值对,不存在会报错
2)字典.pop(key) - 取出字典中指定key对应的值(对应键值对也会消失)
"""
print('=================================================')

# 练习:保存一个班所有的学生信息(姓名、学号、年龄、成绩、电话;假设一个班5个人)


all_student = [
    {'name': '小明', 'age': 28, 'score': 90, 'tel': '13888712688'},
    {'name': '小花', 'age': 16, 'score': 78, 'tel': '13658798888'},
    {'name': '小蓝', 'age': 21, 'score': 23, 'tel': '13593688328'},
    {'name': '小红', 'age': 17, 'score': 68, 'tel': '13888546888'},
    {'name': '小绿', 'age': 30, 'score': 76, 'tel': '13158888888'}
]

# 1)统计以上学生中不及格学生人数
# 2)将打印所有未成年人的学生姓名
# 3)将25岁以上学生的电话设置为'保密'
num = 0
for stu in all_student:
    if stu['score'] < 60:
        num += 1
print(num)

for stu in all_student:
    if stu['age'] < 18:
        print(stu['name'])

for stu in all_student:
    if stu['age'] > 25:
        stu['tel'] = '保密'

print(all_student)


