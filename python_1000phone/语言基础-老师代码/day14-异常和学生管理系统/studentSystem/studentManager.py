"""__author__=余婷"""
from studentSystem import fileManager

USER_NAME = ''

"""
1.程序中保存所有学生: 一个列表中有多个字典，每个字典有4个键值对分别是: 'name', 'age', 'tel', 'id'

{
    'all_student': [
        {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
        {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
        {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
        ... 
    ],
    'num': 0    # 当前账号添加的学生的个数
}

2.所有学生需要做数据持久化: 将数据保存到json文件, 文件名:
方案一: 所有用户的学生信息保存在一个文件中: all_user_students
{
    用户名1:{
         'all_student': [
            {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
            {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
            {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
            ... 
        ]
    }, 
    用户名2:{
         'all_student': [
            {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
            {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
            {'name': 1, 'age': 2, 'tel': 3, 'id': 4},
            ... 
        ]
    }
    ....
}
 
方案二: 一个用户管理的学生信息对应一个文件，用户名作为文件名(推荐使用)

"""


def show_student(stu):
    print('学号:{id}, 姓名:{name}, 年龄:{age}, ☎:{tel}'.format(**stu))


def find_student():
    # 1.读出文件中保存的数据
    user_message = fileManager.read_json_file(USER_NAME+'.json')
    # 2.获取所有的学生
    if not user_message:
        all_student = []
    else:
        all_student = user_message['all_student']

    #  如果没有学生
    if not all_student:
        print('该账号没有可以管理的学生!')
        return

    print('1.查看所有学生\n2.按姓名查找\n3.按学生查找\n其他.返回')
    value = input('请选择(1~3):')
    if value == '1':
        for stu in all_student:
            show_student(stu)

    elif value == '2':
        name = input('请输入学生姓名:')
        count = 0
        for stu in all_student:
            if stu['name'] == name:
                count += 1
                show_student(stu)
        if count == 0:
            print('没有该学生!')

    elif value == '3':
        stu_id = input('请输入学生学号:')
        for stu in all_student:
            if stu['id'] == stu_id:
                show_student(stu)
                break
        else:
            print('没有该学生!')
    else:
        # print('输入有误!')
        return


# ===============添加学生==============
def add_student():
    # 0.读本地文件数据
    user_message = fileManager.read_json_file(USER_NAME+'.json')
    if not user_message:
        user_message = {}

    while True:
        # 1.输入学生信息
        stu_name = input('请输入学生姓名:')
        stu_age = input('请输入学生年龄:')
        stu_tel = input('请输入学生电话:')

        # 生成学号
        num = user_message.get('num', 0)

        num += 1
        stu_id = str(num).zfill(3)
        user_message['num'] = num

        # 2.创建学生
        stu = {'name': stu_name, 'age': int(stu_age), 'tel': stu_tel, 'id': stu_id}

        # 添加学生
        all_student = user_message.get('all_student', [])
        all_student.append(stu)

        user_message['all_student'] = all_student

        # 更新文件
        result = fileManager.write_json_file(USER_NAME+'.json', user_message)
        if result:
            print('添加成功')
            print('1.继续\n2.返回')
            value = input('请选择:')
            if value != '1':
                return

        else:
            print('添加失败')
            return


def alter_student():
    # 1.读出文件中保存的数据
    user_message = fileManager.read_json_file(USER_NAME + '.json')
    # 2.获取所有的学生
    if not user_message:
        all_student = []
    else:
        all_student = user_message['all_student']

    #  如果没有学生
    if not all_student:
        print('该账号没有可以管理的学生!')
        return

    # 3.确定需要修改哪个学生的信息
    stu_id = input('请输入需要修改信息的学生的学号:')
    for stu in all_student:
        if stu['id'] == stu_id:
            show_student(stu)
            alter_stu = stu
            break
    else:
        print('没有该学生!')
        return

    print('1.修改姓名\n2.修改年龄\n3.修改电话\n其他.返回')
    value = input('请选择:')
    if value == '1':
        new_name = input('请输入新名字:')
        alter_stu['name'] = new_name
    elif value == '2':
        new_age = int(input('请输入新的年龄:'))
        alter_stu['age'] = new_age
    elif value == '3':
        new_tel = input('请输入新的电话号码:')
        alter_stu['tel'] = new_tel
    else:
        return

    # 更新数据
    result = fileManager.write_json_file(USER_NAME+'.json', user_message)
    if result:
        print('修改成功!')
    else:
        print('修改失败!')






def show_manager_page():
    page = fileManager.read_text_file('managerPage')
    while True:
        # 显示页面
        print(page % USER_NAME)
        # 选择
        value = input('请选择(1~5):')

        # 根据选择实现不同的功能
        if value == '1':
            # print('添加学生')
            add_student()
        elif value == '2':
            # print('查看学生')
            find_student()
        elif value == '3':
            # print('修改学生信息')
            alter_student()
        elif value == '4':
            print('删除学生')
        elif value == '5':
            # print('返回')
            return
        else:
            print('输入有误，请重新输入!')



