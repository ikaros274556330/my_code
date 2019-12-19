"""__author__=吴佩隆"""

"""
1.输入一个字符串，打印所有奇数位上的字符(下标是1，3，5，7…位上的字符)

例如: 输入'abcd1234 '   输出'bd24'  
"""

# def ji_shu(str1):
#     print(str1[1::2])
#
# ji_shu('abcd1234')

"""
2.输入用户名，判断用户名是否合法(用户名长度6~10位)
"""

# def good_id(name):
#     if 6 <= len(name) <= 10:
#         print('合法')
#     else:
#         print('不合法')
#
#
# name = input('请输入你的姓名:')
# good_id(name)

"""
3.输入用户名，判断用户名是否合法(用户名中只能由数字和字母组成) 
"""

# def user_name(name):
#     for i in name:
#         if not ('A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9'):
#             print('不合法')
#             break
#     else:
#         print('合法')
#
#
# name = input('请输入你的姓名:')
#
# user_name(name)

"""
4.输入用户名，判断用户名是否合法(用户名必须包含且只能包含数字和字母，并且第一个字符必须是大写字母)  
"""
# def user_name(name):
#     if 'A' <= name[0] <= 'Z':
#         for i in name:
#             if not ('A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9'):
#                 print('不合法')
#                 break
#         else:
#             print('合法')
#     else:
#         print('不合法')
#
#
# name = input('请输入你的姓名:')
#
# user_name(name)

"""
5.输入一个字符串，将字符串中所有的数字字符取出来产生一个新的字符串  
"""

# def all_number(strs):
#     all_num = ''
#     for i in strs:
#         if i.isdigit():
#             all_num += i
#
#     return all_num
#
#
# strs = input('输入一串带数字的字符串:')
#
# print(all_number(strs))

"""
6.输入一个字符串，将字符串中所有的小写字母变成对应的大写字母输出  (用upper方法和自己写算法两种方式实现)
"""
# strs = input('输入一个子字符串:')
# print(strs.upper())

# def upper1(strs):
#     new_strs = ''
#     for i in strs:
#         if 'a' <= i <= 'z':
#             new_strs += chr((ord(i)-32))
#         else:
#             new_strs += i
#     return new_strs
#
# str1 = input('输入一个子字符串:')
# print(upper1(str1))

"""
7.输入一个小于1000的数字，产生对应的学号
"""

# def stu_number(value):
#     if len(value) > 3:
#         print('输入有误')
#     else:
#         print('py1906' + value.zfill(3))
#
#
# stu_id = input('输入学生学号:')
# stu_number(stu_id)

"""
8.输入一个字符串，统计字符串中非数字字母的字符的个数 
例如: 输入'anc2+93-sj胡说'  输出:4     输入'==='   输出:3
"""

# def special_num(strs):
#     num = 0
#     for i in strs:
#         if not ('A' <= i <= 'Z' or 'a' <= i <= 'z' or '0' <= i <= '9'):
#             num += 1
#     return num
#
#
# print(special_num('anc2+93-sj胡说'))

"""
9.输入字符串，将字符串的开头和结尾变成'+'，产生一个新的字符串  
例如: 输入字符串'abc123',  输出'+bc12+'
"""
# def aba(strs):
#     print('+'+strs[1:-1]+'+')
# aba('abc123')

"""
10.输入字符串，获取字符串的中间字符  
例如: 输入'abc1234'  输出:'1'     输入'abc123'  输出'c1'
"""
# def center_str(strs):
#     if len(strs) & 1 == 1:
#         print(strs[(len(strs)-1)//2])
#     else:
#         print(strs[(len(strs)//2-1)]+strs[len(strs)//2])
#
# center_str('abc1234')
# center_str('abc123')

"""
11.写程序实现字符串函数find/index的功能(获取字符串1中字符串2第一次出现的位置)

例如: 字符串1为:how are you? Im fine, Thank you!  , 字符串2为:you,  打印8

"""


def findindex(str1, str2):
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:len(str2) + i] == str2:
            return i
    else:
        return -1


str1 = 'how are you? Im fine, Thank you!'
str2 = 'you'

print(findindex(str1, str2))

"""
12.获取两个字符串中公共的字符
例如: 字符串1为:abc123, 字符串2为: huak3 , 打印:公共字符有:a3
"""
# print(''.join(set('abc123') & set('huak3')))
