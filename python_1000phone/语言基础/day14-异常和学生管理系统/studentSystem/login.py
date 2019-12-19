"""__author__=吴佩隆"""
from studentSystem import fileManager, studentManager
users_file = 'users.json'
"""
账号密码的存储:
程序中:用一个字典保存所有的账号和密码 - {账号1:密码1,账号2:密码2...}
数据持久化:将所有的账号对应的字典保存在文件中(users.json)
"""


def login():
    # 1.输入账号和密码
    user_name = input('请输入账号:')
    password = input('请输入密码:')

    # 2.检测输入的账号是否已经注册
    all_user = fileManager.read_json_file(users_file)
    if not all_user:
        print('登陆失败!该账号没有注册')
        return
    if user_name not in all_user:
        print('登陆失败!该账号没有注册')
        return

    # 如果注册过，判断密码是否正确
    pw = all_user[user_name]
    if pw == password:
        print('登陆成功!')
        # 进入管理系统
        studentManager.USER_NAME = user_name
        studentManager.show_manager_page()
    else:
        print('登陆失败!密码错误!')


def register():
    while True:
        user_name = input('请输入账号(3~6位):')
        if 3 <= len(user_name) <= 6:
            break
        else:
            print('账号不符合要求，重输!')

    # 输入密码
    while True:
        password = input('请输入密码(6~12位)')
        if 6 <= len(password) <= 12:
            break
        else:
            print('密码不符，重输!')

    # 3.检测账号是否已经注册过
    all_user = fileManager.read_json_file(users_file)
    if not all_user:
        all_user = {}
    if user_name in all_user:
        print('注册失败！该账号已经注册过~')
        return

    # 4.注册
    all_user[user_name] = password
    result = fileManager.write_json_file(users_file, all_user)
    if result:
        print('注册成功！')
    else:
        print('注册失败！')


def show_login_page():
    page = fileManager.read_text_file('loginPage')

    while True:
        print(page)
        value = input('请选择(1~3):')
        if value == '1':
            login()
        elif value == '2':
            register()
        elif value == '3':
            # print('退出...')
            # break
            # return
            exit()
        else:
            print('输入有误,重新选择!')