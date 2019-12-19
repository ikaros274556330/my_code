"""__author__=吴佩隆"""
from studentSystem import fileManager
USER_NAME = ''

"""
1.程序中保存所有的学生:一个列表中有多个字典，每个字典4个键值对
{
    'all_student':[
        {'name':1,'age':2,'tel':3,'id':4},
        {'name':1,'age':2,'tel':3,'id':4},
        {'name':1,'age':2,'tel':3,'id':4},
        ...
    ],
    'num':0
}

2.所有学生需要做数据持久化:将数据保存带json文件
方案一:所有用户的学生信息保存在一个文件中

方案二:一个用户管理的学生信息对应一个文件，用户名作文件名(推荐使用)

"""


def show_student(stu):
    print('学号:{id},姓名:{name},年龄:{age},📞:{tel}'.format(**stu))


def find_student():

    user_message = fileManager.read_json_file(USER_NAME+'.json')
    if not user_message:
        all_student = []
    else:
        all_student = user_message['all_student']

    # 如果没有学生
    if not all_student:
        print('该账号没有可以管理的学生')
        return

    print('1.查看看所有学生\n2.按姓名找\n3.按学号查找\n其他，返回')
    value = input('请选择(1~3):')

    if value == '1':
        for i in all_student:
            show_student(i)

    elif value == '2':
        name = input('请输入学生姓名:')
        count = 0
        for i in all_student:
            if i['name'] == name:
                count += 1
                show_student(i)
        if count == 0:
            print('查无此人!')

    elif value == '3':
        stu_id = input('请输入学号:')
        for i in all_student:
            if i['id'] == stu_id:
                show_student(i)
                break
        else:
            print('查无此人')

    else:
        print('输入有误!')
        return


def add_student():
    # 0.读本地文件数据
    user_message = fileManager.read_json_file(USER_NAME+'.json')
    # user_message = None(第一次)

    if not user_message:
        user_message = {}

    while True:
        # 1.输入学生信息
        stu_name = input('请输入学生姓名:')
        stu_age = input('请输入学生年龄:')
        stu_tel = input('请输入学生电话:')

        # 生成学生
        # 如果字典为空，默认返回0
        num = user_message.get('num', 0)
        num += 1
        user_message['num'] = num       # 更新学号
        stu_id = str(num).zfill(3)

        # 2.创建学生
        stu = {'name': stu_name, 'age': int(stu_age), 'tel': stu_tel, 'id': stu_id}

        # 添加学生
        # all_student = []
        all_student = user_message.get('all_student', [])
        all_student.append(stu)
        user_message['all_student'] = all_student

        result = fileManager.write_json_file(USER_NAME+'.json', user_message)
        if result:
            print('添加成功！')
            print('1.继续\n'
                  '2.返回')
            value = input('请选择:')
            if value == '2':
                return
        else:
            print('添加失败！')
            return


def alter_student():
    user_message = fileManager.read_json_file(USER_NAME + '.json')
    if not user_message:
        all_student = []
    else:
        all_student = user_message['all_student']

    # 如果没有学生
    if not all_student:
        print('该账号没有可以管理的学生')
        return

    stu_id = input('请输入要修改的学生学号:')
    for stu in all_student:
        if stu['id'] == stu_id:
            show_student(stu)
            alter_stu = stu
            break
    else:
        print('查无此人')
        return
    print('1.修改姓名\n2.修改年龄\n3.修改电话\n其他.返回')
    value = input('请选择:')
    if value == '1':
        new_name = input('请输入新名字:')
        alter_stu['name'] = new_name

    elif value == '2':
        new_age = int(input('输入新年龄:'))
        alter_stu['age'] = new_age

    elif value == '3':
        new_tel = input('输入新电话:')
        alter_stu['tel'] = new_tel

    else:
        return

    result = fileManager.write_json_file(USER_NAME+'.json', user_message)
    if result:
        print('修改成功！')
    else:
        print('修改失败！')


def del_student():
    user_message = fileManager.read_json_file(USER_NAME + '.json')
    if not user_message:
        all_student = []
    else:
        all_student = user_message['all_student']

    # 如果没有学生
    if not all_student:
        print('该账号没有可以管理的学生')
        return

    del_stu = input('请输入要删除的学生:')
    for stu in all_student:
        if stu['name'] == del_stu:
            all_student.remove(stu)
            fileManager.write_json_file(USER_NAME + '.json', user_message)
            print('删除成功！')
            break
    else:
        print('查无此人！')


def show_manager_page():
    page = fileManager.read_text_file('managerPage')

    while True:
        # 显示页面
        print(page % USER_NAME)
        value = input('请选择(1~5):')

        # 根据选择实现不同功能
        if value == '1':
            add_student()

        elif value == '2':
            find_student()

        elif value == '3':
            alter_student()

        elif value == '4':
            del_student()

        elif value == '5':
            return

        else:
            print('输入有误,重新输入!')
