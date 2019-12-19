"""__author__=吴佩隆"""

from random import randint

"""
1.编写函数，求1+2+3+…N的和
"""

# def sum1(x: int) -> int:
#     """
#     求1+2+3+…x的和
#     :param x: x的值
#     :return: 和的值
#     """
#     num = 0
#     for i in range(1, x + 1):
#         num += i
#     return num
#
#
# print(sum1(5))

"""
2.编写一个函数，求多个数中的最大值
"""

# def max1(*x: int) -> int:
#     """
#     返回传入参数的最大值
#     :param x: 一个或多个int值
#     :return: x中的最大值
#     """
#     return max(x)
#
#
# print(max1(5, 10, 50))

"""
3.编写一个函数，实现摇骰子的功能，打印N个骰子的点数和 
"""

# def dice(x: int) -> int:
#     """
#     求x个骰子的和
#     :param x: x个骰子
#     :return: x个骰子的和
#     """
#     num = []
#     for _ in range(x):
#         num.append(randint(1, 6))
#     print(num)
#     return sum(num)
#
#
# print(dice(3))

"""
4.编写一个函数，交换指定字典的key和value。
例如:dict1={'a':1, 'b':2, 'c':3}  -->  dict1={1:'a', 2:'b', 3:'c'} 
"""

# def change_keyvalue(dict1: dict) -> dict:
#     """
#     交换一个字典的key和value
#     :param dict1: 传入一个字典
#     :return: 交换后的结果
#     """
#     for key in dict1.copy():
#         dict1[dict1[key]] = key
#         del dict1[key]
#     return dict1
#
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
#
# print(change_keyvalue(dict1))

"""
5.编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串 
例如: 传入'12a&bc12d-+'   -->  'abcd' 
"""

# def get_abc(str1: str) -> str:
#     """
#     返回一个字符串的所有字母组成的新字符串
#     :param str1:一个字符串
#     :return:字母组成的新字符串
#     """
#     new_str = ''
#     for i in str1:
#         if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
#             new_str += i
#     return new_str
#
#
# print(get_abc('12a&bc12d-+'))

"""
6.写一个函数，求多个数的平均值 
"""

# def average(*num) -> float:
#     """
#     返回一个或多个数平均值
#     :param num: 一个或多个数
#     :return: 平均值
#     """
#     return sum(num) / len(num)
#
#
# print(average(1, 2, 3, 4, 5, 6))

"""
7.写一个函数，默认求10的阶乘，也可以求其他数字的阶乘  
"""

# def factorial(x=10) -> int:
#     """
#     求x的阶乘，默认为10
#     :param x: 整数
#     :return: 结果
#     """
#     num = 1
#     for i in range(1, x+1):
#         num *= i
#     return num
#
#
# print(factorial(5))

"""
8.写一个自己的capitalize函数，能够将指定字符串的首字母变成大写字母
"""

# def capitalize1(str1: str) -> str:
#     """
#     字符串首字母小写转大写
#     :param str1: 任何字符串
#     :return: 转换后结果
#     """
#     if 'a' <= str1[0] <= 'z':
#         return chr(ord(str1[0])-32) + str1[1:]
#
#
# print(capitalize1('python牛逼！'))

"""
9.写一个自己的endswith函数，判断一个字符串是否已指定的字符串结束
例如: 字符串1:'abc231ab' 字符串2:'ab' 函数结果为: True
     字符串1:'abc231ab' 字符串2:'ab1' 函数结果为: False
"""

# def endswith1(str1: str, str2: str) -> bool:
#     """
#     判断字符串1结尾是否以字符串2结尾
#     :param str1: 字符串1
#     :param str2: 字符串2
#     :return: 布尔值
#     """
#     return str1[-len(str2):] == str2
#
#
# print(endswith1('abc231ab', 'ab'))
# print(endswith1('abc231ab', 'ab1'))

"""
10.写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串   
例如: '1234921'  结果: True
      '23函数'   结果: False
      'a2390'    结果: False
"""

# def isdigit1(str1: str) -> bool:
#     """
#     判断字符串是否全由数字组成
#     :param str1:任意字符串
#     :return:布尔值
#     """
#     for i in str1:
#         if not ('0' <= i <= '9'):
#             return False
#     else:
#         return True
#
#
# print(isdigit1('1234921'))
# print(isdigit1('23函数'))
# print(isdigit1('a2390'))

"""
11.写一个自己的upper函数，将一个字符串中所有的小写字母变成大写字母 
例如: 'abH23好rp1'   结果: 'ABH23好RP1' 
"""

# def upper1(str1: str) -> str:
#     """
#     将str1中所有小写转大写
#     :param str1: 任意字符串
#     :return: 转换后结果
#     """
#     new_str = ''
#     for i in str1:
#         if 'a' <= i <= 'z':
#             new_str += chr(ord(i) - 32)
#         else:
#             new_str += i
#     return new_str
#
#
# print(upper1('abH23好rp1'))

"""
12.写一个自己的rjust函数，创建一个字符串的长度是指定长度，原字符串在新字符串中右对齐，剩下的部分用指定的字符填充  
例如: 原字符:'abc'  宽度: 7  字符:'^'    结果: '^^^^abc'
     原字符:'你好吗'  宽度: 5  字符:'0'    结果: '00你好吗'
"""

# def rjust1(str1: str, wid: int, str2: str) -> str:
#     """
#     实现rjust函数
#     :param str1: 原字符串
#     :param wid: 字符串总长
#     :param str2: 填充字符串
#     :return: 填充后的字符串
#     """
#     if len(str1) >= len(str2) and wid >= len(str1):
#         return (wid - len(str1)) * str2 + str1
#     else:
#         print('输入有误')
#
#
# print(rjust1('abc', 7, '^'))
# print(rjust1('你好吗', 5, '0'))


"""
13.写一个自己的index函数，统计指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1
例如: 列表: [1, 2, 45, 'abc', 1, '你好', 1, 0]  元素: 1   结果: 0,4,6  
     列表: ['赵云', '郭嘉', '诸葛亮', '曹操', '赵云', '孙权']  元素: '赵云'   结果: 0,4
     列表: ['赵云', '郭嘉', '诸葛亮', '曹操', '赵云', '孙权']  元素: '关羽'   结果: -1
"""

# def index1(list1: list, str1):
#     num = []
#     for i in range(len(list1)):
#         if list1[i] == str1:
#             num.append(i)
#     if len(num) > 0:
#         return str(num)[1:-1]
#     else:
#         return '-1'
#
#
# list1 = [1, 2, 45, 'abc', 1, '你好', 1, 0]
# list2 = ['赵云', '郭嘉', '诸葛亮', '曹操', '赵云', '孙权']
#
# print(index1(list1, 1))
# print(index1(list2, '赵云'))
# print(index1(list2, '关羽'))

"""
14.写一个自己的len函数，统计指定序列中元素的个数  
例如: 序列:[1, 3, 5, 6]    结果: 4
     序列:(1, 34, 'a', 45, 'bbb')  结果: 5  
     序列:'hello w'    结果: 7
"""

# def len1(x) -> int:
#     num = 0
#     for i in x:
#         num += 1
#
#     return num
#
#
# print(len1((1, 34, 'a', 45, 'bbb')))

"""
15.写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，取字典值的最大值  
例如: 序列:[-7, -12, -1, -9]    结果: -1   
     序列:'abcdpzasdz'    结果: 'z'  
     序列:{'小明':90, '张三': 76, '路飞':30, '小花': 98}   结果: 98
"""

# def max1(x):
#     """
#     返回序列的最大值，字典返回值的最大值
#     :param x: 一个容器
#     :return: 最大值
#     """
#     if isinstance(x, dict):
#         a = []
#         for i in x:
#             a.append(x[i])
#         a.sort()
#         return a[-1]
#     else:
#         b = list(x)
#         b.sort()
#         return b[-1]
#
#
# list1 = [-7, -12, -1, -9]
# str1 = 'abcdpzasdz'
# dict1 = {'小明':90, '张三': 76, '路飞':30, '小花': 98}
# print(max1(list1))
# print(max1(str1))
# print(max1(dict1))


"""
16.写一个函数实现自己in操作，判断指定序列中，指定的元素是否存在  
例如: 序列: (12, 90, 'abc')   元素: '90'     结果: False
     序列: [12, 90, 'abc']   元素: 90     结果: True    
"""


# def in1(x, y) -> bool:
#     """
#     实现in函数
#     :param x: 一个序列
#     :param y: 待查元素
#     :return: 布尔值
#     """
#     for i in x:
#         if i == y:
#             return True
#     else:
#         return False
#
#
# tuple1 = (12, 90, 'abc')
# list1 = [12, 90, 'abc']
# print(in1(tuple1, '90'))
# print(in1(list1, 90))


"""
17.写一个自己的replace函数，将指定字符串中指定的旧字符串转换成指定的新字符串 
例如: 原字符串: 'how are you? and you?'   旧字符串: 'you'  新字符串:'me'  结果: 'how are me? and me?'
"""


# def replace1(str1: str, str2: str, str3: str) -> str:
#     """
#     实现replace函数
#     :param str1: 原字符串
#     :param str2: 需要替换的字符串
#     :param str3: 待替换字符串
#     :return: 替换后的新字符串
#     """
#
#     if str2 in str1:
#         list_str = str1.split(str2)
#         new_str = str3.join(list_str)
#         return new_str
#     else:
#         return '-1'
#
#
# str1 = 'how are you? and you?'
# str2 = 'you'
# str3 = 'me'
# print(replace1(str1, str2, str3))


"""
18.写四个函数，分别实现求两个列表的交集、并集、差集、补集的功能   
"""


# def list_jj(list1, list2) -> list:
#     """交集"""
#     return [i for i in list1 if i in list2]
#
#
# def list_bj(list1, list2) -> list:
#     """并集"""
#     return list(set(list1 + list2))
#
#
# def list_cj(list1, list2) -> list:
#     """差集"""
#     return [i for i in list1 if i not in list2]
#
#
# def list_bg(list1, list2) -> list:
#     """补集"""
#     return [i for i in list1+list2 if (list1+list2).count(i) != 2]
#
#
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8, 9]
#
# print(list_jj(list1, list2))
# print(list_bj(list1, list2))
# print(list_cj(list1, list2))
# print(list_bg(list1, list2))
