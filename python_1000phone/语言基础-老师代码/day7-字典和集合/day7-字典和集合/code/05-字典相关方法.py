"""__author__=余婷"""

# 1.字典.clear()  -  清空字典
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kind': '土狗'}
dog.clear()
print(dog)

# 2.字典.copy()  -  拷贝字典，返回新的字典
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kind': '土狗'}
dog2 = dog.copy()
dog['name'] = '小黄'
print(dog2)

# 3.dict.fromkeys(序列, 值)   -   创建新字典；将序列中的元素作为key，指定的值作为每个key的value，去创建一个新的字典
dict1 = dict.fromkeys(['name', 'age', 'gender'], 0)
print(dict1)

# 4.字典.items()、字典.values()、字典.keys()
# 字典.keys() -> 获取字典所有的key并且返回, 返回的数据类型是序列但是不是列表
# 字典.values()  -> 获取字典所有的value并且返回，返回的数据类型是序列但是不是列表
# 字典.items() ->  同时获取字典所有的key和value, 返回一个序列，序列中元素是有两个元素的元祖，这两个元素分别是key和value
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kind': '土狗'}
print(list(dog.keys()))   # ['name', 'age', 'gender', 'kind']
print(list(dog.values()))  # ['大黄', 4, '公狗', '土狗']
print(dog.items())    # dict_items([('name', '大黄'), ('age', 4), ('gender', '公狗'), ('kind', '土狗')])


# 5.字典.setdefault(key, value)  -  字典中添加键值对(key存在的时候不会修改)
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kind': '土狗'}
dog.setdefault('color', '黄色')
print(dog)

dog.setdefault('name', '财财')
print(dog)

# 6.字典1.update(字典2)   -  将字典2中的键值对更新到字典1中（不存在的就添加，存在的就覆盖）
dog = {'name': '大黄', 'age': 4, 'gender': '公狗', 'kind': '土狗'}
dict2 = {'name': '小明', 'height': 170}
dog.update(dict2)
print(dog)


# 练习2:
# 设置数据保存一个班级的信息： 班级名字、位置、所有的老师(名字、性别、QQ、职责)、
#                         所有的学生(姓名、学校、电话、性别、年龄、紧急联系人(...))
class1 = {
    'class_name': 'python1906',
    'teachers': [
        {'name': '余婷', 'gender': '女', 'qq': '726550822', 'duty': '讲师'},
        {'name': '张老师', 'gender': '女', 'qq': '828333', 'duty': '班主任'}
    ],
    'students': [
        {
            'name': '小明',
            'school': '川大',
            'tel': '2382638',
            'contacts': {
                            'name': '张三',
                            'tel': '2327387',
                            'relationship': '父亲'
                        }
        },
        {
            'name': '小红',
            'school': '交大',
            'tel': '82939283',
            'contacts': {
                            'name': '李四',
                            'tel': '2327387',
                            'relationship': '母亲'
                        }
        }
    ]
}

for student in class1['students']:
    if student['name'] == '小明':
        print(student['contacts']['name'])








