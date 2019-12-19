"""__author__=余婷"""
import re

# 1.什么是正则表达式
# 用正则符号来描述字符串规则让字符串匹配更简单的一种工具; 正则本身的语法和语言无关，几乎所有的编程语言都支持正则
# python通过提供re模块来支持正则表达式

# value = input('请输入电话号码:')
#
# re = re.fullmatch(r'1[3-9]\d{9}', value)
# print(re)
#
# # if len(value) == 11:
# #     if value[0] == '1':
# #         if value[1] == '3' or value[1] == '4':
# #     else:
# #         print('不合法')

# 2.正则符号
print('=========================匹配符号===========================')
# 1) 普通字符 - 在正则表达式中没有特殊功能或者特殊意义的字符都是普通字符
# 普通字符在正则表达式中就代表这个符号本身，匹配的时候只能和这个指定的字符进行匹配
# re_str = r'1[3-9]\d{9}'  # python
# re_str = /1[3-9]\d{9}/
re_str = r'abc'
result = re.fullmatch(re_str, 'abc')
print(result)

# 2) .   -   代表任意字符
# 注意: 一个.代表一个任意字符

re_str = r'a.b'   # 匹配一个长度是3的字符串，第一个字符是a,最后一个字符是b, 中间是任意字符
print(re.fullmatch(re_str, 'abc'))   # None
print(re.fullmatch(re_str, 'a你b'))

print(re.fullmatch(r'a..b', 'au9b'))

# 3) \w  - ASCII码表中只能匹配字母、数字或者下划线；ASCII码表以外的都可以匹配
# 注意: 一个\w只能匹配一个字符
re_str = r'a\wb'
print(re.fullmatch(re_str, 'awb'))
print(re.fullmatch(re_str, 'a8b'))
print(re.fullmatch(re_str, 'a_b'))
print(re.fullmatch(re_str, 'a+b'))   # None
print(re.fullmatch(re_str, 'a胡b'))

# 4) \d - 匹配任意一个数字字符
re_str = r'a\d\db'
print(re.fullmatch(re_str, 'a23b'))
print(re.fullmatch(re_str, 'a33b'))
print(re.fullmatch(re_str, 'aa3b'))   # None

# 5) \s - 匹配任意一个空白字符
re_str = r'a\sb'
print(re.fullmatch(re_str, 'a b'))
print(re.fullmatch(re_str, 'a\tb'))
print(re.fullmatch(re_str, 'a\nb'))
print(re.fullmatch(re_str, 'a   b'))   # None

# 6) \W, \D, \S
# \D - 匹配任意非数字字符
print(re.fullmatch(r'a\Db\Sc\Wd', 'aZb=c+d'))
print(re.fullmatch(r'a\Db\Sc\Wd', 'a2b=c+d'))   # None
print(re.fullmatch(r'a\Db\Sc\Wd', 'aZb c+d'))   # None
print(re.fullmatch(r'a\Db\Sc\Wd', 'aZb=c胡d'))   # None

# 7) [字符集]  - 匹配字符集中的任意一个字符
"""
注意： 一个[]只能匹配一个字符

a. [普通字符集]  例如: [abc] - 匹配a、b、c三个字符中的任意一个
                     [aA123] - 匹配a、A、1、2、3中的任意一个字符
b. [字符1-字符2] 例如:  [1-9]  - 匹配123456789中的任意一个字符
                      [0-9]  - \d
                      [a-z]  - 匹配任意一个小写字母
                      [A-Z]  - 匹配任意一个大写字母
                      [a-zA-Z] - 匹配任意一个字母
                      [\u4e00-\u9fa5]  - 匹配任意一个中文字符
                      [1-9abc] - 匹配1~9或者abc中的任意一个字符
                      [a-zA-Z0-9_]  - 匹配字母数字下划线
                      [\dxyz]  - 任意数字或者x、y、z
注意: 字符1的编码值必须小于字符2的编码值

"""
print(re.fullmatch(r'a[xyz89?]b', 'azb'))
print(re.fullmatch(r'a[xyz]b', 'anb'))
print(re.fullmatch(r'a[23456789]b', r'a7b'))
print(re.fullmatch(r'a[1-9abc]b', 'aab'))
print(re.fullmatch(r'a[abc1-9]b', 'aab'))
print(re.fullmatch(r'a[ac1-9b]b', 'aab'))
print(re.fullmatch(r'a[+*-]b', 'a-b'))
print(re.fullmatch(r'a[\dxyz]b', 'axb'))
print(re.fullmatch(r'a[\\dxyz]b', 'a\\b'))

# 8)[^字符集]  -  匹配除了字符集以外的任意一个字符
"""
[^abc]  - 匹配除了abc以外的任意一个字符
[^1-9]  - 匹配除了1~9以外的任意一个字符
"""
print(re.fullmatch(r'a[^xyz]b', 'a=b'))   # None
print(re.fullmatch(r'a[xyz^]b', 'a^b'))


print('============================检测符号===========================')
# 1) \b  - 检测是否是单词结尾
"""
单词结尾 - 所有可以区分出两个不同单词的符号都是单词结尾，其中字符串开头和字符串结尾
用法: 检测\b所在的位置是否是单词结尾；不影响匹配的时候的字符串长度
"""
# 匹配一个长度是3的字符串，第一个字符是a,最后一个字符是b,中间是任意一个数字；并且要求b的后面是单词边界
re_str = r'a\db\b'
print(re.fullmatch(re_str, 'a7b'))

re_str = r'a\bxy'
print(re.fullmatch(re_str, 'a xy'))   # None

re_str = r'abc\b\sxyz'
print(re.fullmatch(re_str, 'abc xyz'))

result = re.search(r'\d\d\d\b', 'ashdjfhow2378how 899kah989sf 789')
print(result)

# 2)^ - 检测字符串开头
# 判断^所在的位置是否是字符串开头
re_str = r'^\d\d\d'
print(re.fullmatch(re_str, '123'))
print(re.search(re_str, 'k898ahs237khhj'))

# 3)$ - 检测字符串结尾
re_str = r'\d\d\d$'
print(re.search(re_str, '123k898ahs237khhj990'))

re_str = r'^\d\d\d\d\d$'


print('=========================匹配次数=======================')
# 1) ?  - 匹配0次或1次
"""
x?   -  x出现0次或1次
\d?  -  任意数字出现0次或1次
[a-z]?  - 小写字母出现0次或1次
"""
re_str = r'ax?b'
print(re.fullmatch(re_str, 'ab'))
print(re.fullmatch(re_str, 'axb'))
print(re.fullmatch(re_str, 'axxb'))   # None

# 2) *  - 匹配0次或多次
re_str = r'a\d*b'   # r'a\d\d...\d\db'
print(re.fullmatch(re_str, 'ab'))
print(re.fullmatch(re_str, 'a2b'))
print(re.fullmatch(re_str, 'a12b'))
print(re.fullmatch(re_str, 'a1272937928329b'))

# 3) +  - 匹配1次或多次
re_str = r'a\d+b'
print(re.fullmatch(re_str, 'ac'))   # None
print(re.fullmatch(re_str, 'a2b'))
print(re.fullmatch(re_str, 'a12b'))
print(re.fullmatch(re_str, 'a1272937928329b'))

# 4){}
"""
{N}  -  匹配N次
{M,N} - 匹配M到N次:  ? -> {0,1}
{M,}  - 匹配至少M次  * -> {0,}   + -> {1,}
{,N}  - 匹配最多N次
"""
re_str = r'a\d{5}b'
print(re.fullmatch(re_str, 'a78988b'))
print(re.fullmatch(re_str, 'a7898b'))   # None
print(re.fullmatch(re_str, 'a789880b'))  # None

re_str = r'a\d{3,5}b'
print(re.fullmatch(re_str, 'a78988b'))
print(re.fullmatch(re_str, 'a7898b'))
print(re.fullmatch(re_str, 'a789880b'))   # None

# 练习: 写一个正则表达式判断输入的内容是否是整数
# 123 -> 成功!  123a -> 失败!   -123  -> 成功!   --123 -> 失败!   +123 -> 成功
re_str = r'[+-]?[1-9]\d*'




