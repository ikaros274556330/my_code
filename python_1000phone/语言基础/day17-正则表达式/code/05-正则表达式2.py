"""__author__=吴佩隆"""

import re

# 1.分之
"""
正则1|正则2 - 先让正则1去匹配，如果失败再用正则2匹配;
只要有一个匹配成功就成功
"""
# 匹配3个数字或者3个字符
re_str = r'\d{3}|[a-zA-Z]{3}'
print(re.fullmatch(re_str,'jab'))
print(re.fullmatch(re_str,'j3b'))  # None

# 匹配一个字符串:abc前是3个数字或者字母

# re_str = r'\d{3}abc|[a-zA-Z]{3}abc'
# re_str = r'(\d{3}|[a-z]{3})abc'


# 2) () - 分组
"""
(正则表达式) - 将正则表达式看成一个整体进行操作
整体控制次数:()匹配次数
重复: 带分组的正则表达式\M  -  \M后面的内容，重复\M前面第M个分组
"""
re_str = r'(\d+)([a-z]+)=\2'
print(re.fullmatch(re_str, '6hk=hk'))

# re_str = r'[01][\d]{0,2}|[2][0-4]\d|[2][5][0-5]'
#
# print(re.fullmatch(re_str,'255'))

