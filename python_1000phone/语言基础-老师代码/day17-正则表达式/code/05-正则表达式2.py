"""__author__=余婷"""
import re

print('====================贪婪和非贪婪=================')
"""
匹配次数不确定的时候有贪婪和非贪婪两种状态
?、*、+、{M,N}, {M,}, {,N}  -  默认是贪婪的
??, *?, +?, {M,N}?, {M,}?, {,N}?   -  非贪婪

贪婪 - 在能匹配成功的前提下，尽可能多的匹配
非贪婪 - 在能匹配成功的前提下，尽可能少的匹配

"""
re_str = r'\d{3,5}'
print(re.search(re_str, 'abc2732939333===='))  # match='27329'
re_str = r'\d{3,5}?'
print(re.search(re_str, 'abc2732939333===='))  # match='273'
re_str = r'a\d{3,5}?b'
print(re.search(re_str, 'a7283b238kk===='))   # match='a7283b'


re_str = r'\d+'
print(re.search(re_str, 'abc2732939333===='))  # match='2732939333'


re_str = r'a.+b'
print(re.search(re_str, '==a12xb67yusb0293==='))  # match='a12xb67yusb'

re_str = r'a.+?b'
print(re.search(re_str, '==a12xb67yusb0293==='))  # match='a12xb'


print('====================分之和分组====================')
# 1) |  -  分之
"""
正则1|正则2  - 先让正则1去匹配，如果匹配再用正则2匹配;只要两个中有一个能够匹配成功就成功
"""
# 匹配三个数字或者三个字母的字符串
re_str = r'\d{3}|[a-zA-Z]{3}'
print(re.fullmatch(re_str, '890'))

# 匹配一个字符串: abc前是3个数字或者3个字母
# 123abc, uJhabc
re_str = r'\d{3}abc|[a-zA-Z]{3}abc'


# 2) ()  - 分组
"""
(正则表达式)  - 将正则表达式看成一个整体进行操作
整体控制次数: ()匹配次数
重复:  带分组的正则表达式\M  --  在\M的位置重前面第M个分组匹配到的内容
"""
# ab78hj90lo23
re_str = r'[a-z]{2}\d{2}[a-z]{2}\d{2}[a-z]{2}\d{2}'

# 9h8k9j8j7h6u5k....
re_str = r'(\d[a-z])+'

# 匹配一个字符串: abc前是3个数字或者3个字母
re_str = r'(\d{3}|[a-z]{3})abc'
print(re.fullmatch(re_str, 'mskabc'))

# abc123abc -成功！  xab234xab  - 成功!  xyz123xyz -成功！
# abc123acb -失败!   xab234sdk  -失败！
# ab-ab   abc-abc   123-123

re_str = r'(\d+)abc\1'
print(re.fullmatch(re_str, '234abc234'))
print(re.fullmatch(re_str, '12345abc12345'))
print(re.fullmatch(re_str, '234abc890'))   # None

re_str = r'(\d+)([a-z]+)=\2'
print(re.fullmatch(re_str, '6kh=kh'))

re_str = r'(\d+)=\1([a-z]+)'
print(re.fullmatch(re_str, '123=123ioo'))

re_str = r'(\d{3})=(\1){2}'
print(re.fullmatch(re_str, '234=234234'))
