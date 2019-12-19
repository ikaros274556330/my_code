"""__author__=吴佩隆"""

import json


def main_page():
    while True:
        print("""
    =============欢迎来到1906管理系统===========
    
             1  登录
             2  注册
             3  修改密码
             4  退出   
    """)
        order = input('请输入你想执行的操作:')
        return print('输入有误，请重新输入！') if order not in ['1', '2', '3', '4'] else order


def loading(user_list):
    while True:
        user = input('请输入你的用户名(q键返回):')
        if user == 'q':
            break
        for name in user_list:
            if name['user'] == user:
                break
        else:
            print('没有注册过的用户')
            break
        pw = input('请输入你的密码(q键返回):')
        if pw == 'q':
            break
        for secret in user_list:
            if secret['pw'] == pw:
                break
        else:
            print('你输入的密码有误')
            break
        print('登录成功!')
        return True


def registered(user_list):
    while True:
        user = input('请输入你的用户名(q返回):')
        if user == 'q':
            break
        for name in user_list:
            if name['user'] == user:
                print('用户名已经被注册！')
                break
        else:
            pw = input('请输入你的密码(q返回):')
            if pw == 'q':
                break
            if len(pw) != 0:
                user_list.append({'user':user,'pw':pw})
                print('注册成功')
                return True
            else:
                print('密码不符合要求！')


def save(user_list):
    user_massage = json.dumps(user_list)
    with open('../files/load_manage.txt', 'w') as f:
        f.write(user_massage)


def main():
    with open('../files/load_manage.txt', 'r') as f:
        user_massage = f.read()

    user_list = json.loads(user_massage)
    print(user_list)

    order = None

    while order != 4:
        order = main_page()
        if order == '1':
            flag = loading(user_list)
            if flag:
                save(user_list)
                return True

        elif order == '2':
            flag = registered(user_list)
            if flag:
                save(user_list)
                return True

        elif order == '3':
            pass
    save(user_list)


main()







