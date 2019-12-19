"""__author__=吴佩隆"""

# student = {'name': '张三', 'age': 19, 'scores': 89, 'tel': '13888888888', 'gender': '男'}
# print(student)

students = [{'name': '张三', 'age': 19, 'scores': 80, 'tel': '13888888888', 'gender': '男'},
            {'name': '王五', 'age': 15, 'scores': 89, 'tel': '13888812345', 'gender': '女'},
            {'name': '李四', 'age': 27, 'scores': 55, 'tel': '13123488888', 'gender': '女'},
            {'name': '刘二', 'age': 17, 'scores': 89, 'tel': '13884565888', 'gender': '不明'},
            {'name': '吴九', 'age': 25, 'scores': 23, 'tel': '13888845468', 'gender': '女'},
            {'name': '周七', 'age': 30, 'scores': 97, 'tel': '13789645888', 'gender': '男'}]
# # num = 0
# for i in students:
#     if i['scores']<60:
#         num += 1
# print(num)

# for i in students:
#     if i['scores'] < 60:
#         print(i['name'],i['scores'])

# num = 0
#
# for i in students:
#     if i['age'] < 18:
#         num += 1
# print(num)

# for i in students:
#     if i['tel'][-1]=='8':
#         print(i['name'])

# a = (0, '')
# for i in students:
#     if i['scores'] > a[0]:
#         a = i['scores'], i['name']
#
# print(a)

# for i in range(len(students)):
#     for j in range(len(students)-1):
#         if students[j]['scores'] < students[j+1]['scores']:
#             students[j], students[j+1] = students[j+1], students[j]

# 方法2
# 高阶函数排序
# students.sort(reverse=True, key=lambda item: item['scores'])
# print(students)

# 方法3
# 选择排序 原理:遍历列表，用当前元素依次与后面元素比较交换位置，然后用第二个元素，以此类推
# 第一次循环选出最大值，第二次循环选出剩下元素的最大值，以此类推
# nums = [8, 3, 5, 1, 9, 5, 4, 3, 37, 7, 89, 6, 54]
# for i in range(len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         if nums[i] < nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
# print(nums)

# for i in students:
#     print(i)

# for i in students:
#     if i['gender'] == '不明':
#         students.remove(i)
#
# print(students)

# python = ['川内', '贝尔法斯特', '赤城', '胡德', '企业', '伊丽莎白', '加贺', '亚利桑那']
#
# c = ['赤城', '加贺', '苍龙', '凌波', '企业', '川内', '拉菲', '长门']
#
# java = ['Z23', '圣地亚哥', '企业', '川内', '苍龙', '拉菲', '标枪']

# print(len(set(python+c+java)))
# print(set(python) - set(c) - set(java))
# a = set(python) - set(c) - set(java)
# # b = set(c) - set(java) - set(python)
# # d = set(java) - set(c) - set(python)
# # print(a | b | d)

# a = set(python) & set(c) - set(java)
# b = set(python) & set(java) - set(c)
# c = set(c) & set(java) - set(python)
#
# print(a|b|c)

# print(set(python) & set(c) & set(java))

# python_1906 = {'名字': 'python-1906',
#                '位置': '力宝大厦18楼',
#                '老师': [
#                    {'名字': '老张', '性别': '', 'qq': '', '职位': ''},
#                    {'名字': '老余', '性别': '', 'qq': '', '职位': ''}
#                ],
#                '学生': [
#                    {'名字': '',
#                     '学校': '',
#                     '电话': '',
#                     '性别': '',
#                     '年龄': '',
#                     '紧急联系人': {
#                         '姓名': '',
#                         '电话': '',
#                         '关系': ''
#
#                     },
#                     }, {'名字': '',
#                         '学校': '',
#                         '电话': '',
#                         '性别': '',
#                         '年龄': '',
#                         '紧急联系人': {
#                             '姓名': '',
#                             '电话': '',
#                             '关系': ''
#
#                         },
#                         }, {'名字': '',
#                             '学校': '',
#                             '电话': '',
#                             '性别': '',
#                             '年龄': '',
#                             '紧急联系人': {
#                                 '姓名': '',
#                                 '电话': '',
#                                 '关系': ''
#
#                             },
#                             }, {'名字': '',
#                                 '学校': '',
#                                 '电话': '',
#                                 '性别': '',
#                                 '年龄': '',
#                                 '紧急联系人': {
#                                     '姓名': '',
#                                     '电话': '',
#                                     '关系': ''
#
#                                 },
#                                 }
#                ]}
