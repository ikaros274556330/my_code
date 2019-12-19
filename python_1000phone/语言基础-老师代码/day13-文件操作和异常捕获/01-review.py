"""__author__=余婷"""
"""
1.生成器
调用带有yield关键字的函数

2.生成式
语法：  (表达式 for 变量 in 序列)
       (表达式 for 变量 in 序列 if 条件语句)
       (表达式 for 变量1 in 序列1 for 变量2 in 序列2)
       
3.模块
import 模块  
from 模块 import 变量1, 变量2...

注意: import在导入模块的时候会检查当前模块之前是否已经导入过，如果已经导入过不会重新导入
"""
# from test1 import a
# print('========')
# import test1
#
# print(a)
# print(test1.b)

import test1
import test2

# 1.写一个生成式交换字典的键值对
dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {1:'a', 2:'b', 3:'c'}
dict2 = dict((dict1[key], key) for key in dict1)
print(dict2)
