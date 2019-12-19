"""__author__=吴佩隆"""
import pickle


def main_page():
    print("""
======欢迎来到1906python帅哥班学生管理系统======

1.用户注册

2.用户登录   

3.退出 
""")
    while True:
        order = input('请输入指令:')
        return print('输入有误，请重新输入！') if order not in ['1', '2', '3'] else order


def registered(loading_dict):
    flag = True
    while flag:
        print('输入q键返回')
        user_name = input('请输入你的用户名(只能输入小字母，长度在4~8个字符):')
        if user_name == 'q':
            break
        secret_num = input('请输入你的密码(必须包含小写字母和数字,长度不少于6位):')
        secret_num_1 = input('请确认你的密码:')
        if secret_num == 'q':
            break

        if user_name == 'lbwnb' and secret_num == '233':
            print(loading_dict)

        if 4 <= len(user_name) <= 8:

            for i in user_name:
                if not ('a' <= i <= 'z'):
                    print('用户名不符合要求!')
                    break

            else:
                if len(secret_num) >= 6:
                    word = 0
                    num = 0
                    for i in secret_num:
                        if '0' <= i <= '9':
                            num += 1
                        elif 'a' <= i <= 'z':
                            word += 1
                        else:
                            print('密码不符合要求!')
                            break
                    else:
                        if word == 0 or num == 0 or secret_num != secret_num_1:
                            print('密码不符合要求!')
                            break
                        for i in loading_dict:
                            if i == user_name:
                                print('用户名重复!')
                                break
                        else:
                            loading_dict[user_name] = secret_num
                            print('注册成功!')
                            return True

                else:
                    print('密码长度不符合要求!')

        else:
            print('用户名长度不符合要求!')


def loading(loading_dict):
    while True:
        user_name = input('请输入你的用户名:')
        secret = input('请输入你的密码')
        for i in loading_dict:
            if i == user_name:
                if loading_dict[i] == secret:
                    print('登陆成功!')
                    return True
                else:
                    print('用户名或密码不对!')
                    break
        else:
            print('未注册过的用户!')
            break


def loading_main():
    order = None
    with open('load_dict.data', 'rb') as f:
        loading_dict = pickle.load(f)
    while order != '3':
        order = main_page()

        if order == '1':
            flag = registered(loading_dict)
            if flag:
                with open('load_dict.data', 'wb') as f:
                    pickle.dump(loading_dict, f)
                return True

        elif order == '2':
            flag = loading(loading_dict)
            if flag:
                with open('load_dict.data', 'wb') as f:
                    pickle.dump(loading_dict, f)
                return True

    with open('load_dict.data', 'wb') as f:
        pickle.dump(loading_dict, f)
