"""__author__=吴佩隆"""
import pickle
import loading_page


def main_page():
    print("""
======欢迎来到1906python帅哥班学生管理系统======
    
1.添加学生
    
2.查找学生
    
3.删除学生
    
4.退出系统
""")

    while True:
        order = input('请输入指令:')
        return print('输入有误,请重新输入!') if order not in ['1', '2', '3', '4'] else order


def add_stu(stu_list):
    while True:

        name = input('请输入学生名字(按q返回):')
        if name == 'q':
            break

        while True:
            try:
                age = int(input('请输入学生年龄:'))
                break
            except ValueError:
                print('输入有误,请输入整数:')

        tel = input('请输入学生联系方式(按q返回):')
        if tel == 'q':
            break
        student_id = 0

        for i in range(1, len(stu_list) + 2):   # 删除的学生学号出现空缺
            for j in stu_list:                  # 通过两个for循环确定空缺的学号
                if j['id'] == i:                # 学号取同学数量+1
                    break                       # 相同跳过，没找到就赋值
            else:
                student_id = i
                break
        student_list = {'id': student_id, 'name': name, 'age': age, 'tel': tel}
        stu_list.append(student_list)
        print('录入成功!')


def check_stu(stu_list):
    while True:
        print("""
1.显示所有学生
        
2.按名字查找
""")
        try:
            order = int(input('请选择查看方式:'))
            break
        except ValueError:
            print('输入有误,重新输入!')

    if order == 1:
        for i in stu_list:
            print('学号:{}  姓名:{}  年龄:{}  联系方式{}'.format(i['id'], i['name'], i['age'], i['tel']))

    elif order == 2:
        name = 1
        while name != 'q':
            name = input('请输入你想查询的学生姓名(按q返回):')
            for i in stu_list:
                if i['name'] == name:
                    print('学号:{}  姓名:{}  年龄:{}  联系方式{}'.format(i['id'], i['name'], i['age'], i['tel']))
                    break
            else:
                print('查无此人')


def del_stu(stu_list):
    name = 1
    while name != 'q':
        name = input('请输入你想删除的学生姓名(按q返回):')
        for i in range(len(stu_list)):
            if stu_list[i]['name'] == name:
                sure = input('你确定要删除{}吗?(y/n)'.format(name))
                if sure == 'y':
                    del stu_list[i]
                    print('删除成功!')
                break
        else:
            print('查无此人')


def manage_main():
    flag = loading_page.loading_main()
    if flag:
        order = None
        with open('stu_list.data', 'rb') as f:
            stu_list = pickle.load(f)
        while order != '4':
            order = main_page()

            if order == '1':
                add_stu(stu_list)

            elif order == '2':
                check_stu(stu_list)

            elif order == '3':
                del_stu(stu_list)

        with open('stu_list.data', 'wb') as f:
            pickle.dump(stu_list, f)


if __name__ == '__main__':
    manage_main()