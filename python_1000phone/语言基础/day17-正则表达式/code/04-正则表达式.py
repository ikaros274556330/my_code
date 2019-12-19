"""__author__=吴佩隆"""
import re

# 1.什么是正则表达式
"""
用正则符号来描述字符串规则让字符串匹配更简单的一种工具;正则本身
的语法和语言无关，几乎所有的变成语言都支持正则
python通过re模块来支持正则表达式
"""

# value = input('请输入电话号码')
#
# re = re.fullmatch(r"1[3-9]\d{9}", value)
#
# print(re)

# 2.正则符号
"""
1)普通字符 - 在正则表达式中没有特殊功能或者特殊意义的字符都是普通字符
普通字符在正则表达式中就代表这个符号本身，匹配的时候只能和这个指定的
字符匹配

"""
# r'1[3-9]\d{9}'   python写法

re_str = r'abc'
result = re.fullmatch(re_str, 'abc')
print(result)

print('========================================================')
"""
2) . - 代表任意字符
"""
# 注意:一个.代表一个任意字符
re_str = r'a.b'  # 匹配一个长度是3的字符串,第一个字符是a,最后一个是b,中间是任意字符
print(re.fullmatch(re_str, 'abc'))  # None
print(re.fullmatch(re_str, 'a+b'))

print(re.fullmatch(r'a..b', 'au9b'))

"""
3) \w - ASCII码表中只能匹配字母、数字、下划线; ASCII码表以外的都可以匹配
注意 ： 一个\w只能匹配一个字符
"""
re_str = r'a\wb'
print(re.fullmatch(re_str, 'a_b'))

"""
4) \d - 匹配任意一个数字字符
"""
re_str = r'a\d\db'
print(re.fullmatch(re_str, 'a69b'))

"""
5) \s - 匹配任意一个空白字符
"""
re_str = r'a\sb'
print(re.fullmatch(re_str, 'a b'))
print(re.fullmatch(re_str, 'a\tb'))
print(re.fullmatch(re_str, 'a\nb'))
print(re.fullmatch(re_str, 'a,b'))  # None

"""
6) \W, \D, \S
\D - 匹配任意非数字字符
"""

print(re.fullmatch(r'a\Db\Sc\wd', 'aXb=cpd'))

"""
7)[字符集] - 匹配字符集中的任意一个字符

注意：一个[]只能匹配一个字符

a.[普通字符集]  例如:[abc] - 匹配a、b、c三个字符中任意一个

b.[字符1-字符2] 例如: [1-9] - 匹配123456789中的任意一个字符
                    [0-9] - \d
                    [a-z] - 匹配小写
                    [A-Z] - 匹配大写
                    [a-zA-Z] - 匹配任意一个字符
                    [\u4e00-\u9fa5] - 匹配任意一个中文字符
                    [1-9abc] - 匹配1到9或者a,b,c中任意一个字符
                    [a-zA-Z0-9_] - 字母数字下划线
                    [\dxyz] - 数字或者x,y,z
                    
注意:字符1的编码值必须小于字符2的编码值
"""
print(re.fullmatch(r'a[xyz]b', 'ayb'))
print(re.fullmatch(r'a[xyz]b', 'a8b'))  # None

print(re.fullmatch(r'a[23]b', 'a7b'))  # None
print(re.fullmatch(r'a[1-9abc]b', 'a8b'))
print(re.fullmatch(r'a[-+*]b', 'a*b'))
print(re.fullmatch(r'a[\dxyz]b', 'a9b'))

"""
8)[^字符集] - 匹配除了字符集以外的任意字符
[^abc] - 除了abc以外的任意字符
[^1-9] - 除了1到9以外的任意字符
"""
print(re.fullmatch(r'a[^xyz]b','axb'))  # None
print(re.fullmatch(r'a[^xyz]b','a9b'))
print(re.fullmatch(r'a[xyz^]b','a^b'))

print('================检测符号=================')

"""
1) \b - 检测是否是单词结尾

单词结尾 - 所有可以区分出两个不同单词的符号都是单词结尾，其中包括字符串开头和结尾
用法:检测\b所在的位置是否是单词结尾;不影响匹配的时候的字符串长度
"""
# 匹配一个长度是3的字符串,并且第一个字符是a,最后一个字符是b,中间是任意一个数字;
#  并且要求b的后面是单词边界
re_str = r'a\db\b'
print(re.fullmatch(re_str, 'a7b'))

re_str = r'a\bxy'
print(re.fullmatch(re_str,'a xy'))

re_str = r'abc\b\sxyz'
print(re.fullmatch(re_str,'abc xyz'))
print('=========================================================')
result = re.search(r'\d\d\d\b', 'aawfdafhowawf544545 awd1 789 6awd')
print(result)

print(re.search(r'\d\b','6 abc'))
print('=============================================================')
"""
2) ^ - 检测字符串开头
判断^所在的位置是否是字符串开头
"""
re_str = r'^\d\d\d'
print(re.fullmatch(re_str,'123'))  # 只有三个数字能匹配成功
print(re.search(re_str,'897awdawd155awd'))
print(re.search(re_str,'w897awdawd155awd'))  # None

"""
3) $ - 检测字符串结尾
"""
re_str = r'\d\d\d$'
print(re.search(re_str, '123Kawd6556awd 666'))

print('======================匹配次数==========================')

"""
1) ? - 匹配0次或1次
x? - x出现0次或1次
\d? - 任意数字出现0次或1次
[a-z]? - 小写字母出现0次或1次
"""
re_str = r'ax?b'
print(re.fullmatch(re_str, 'ab'))
print(re.fullmatch(re_str, 'axb'))
print(re.fullmatch(re_str, 'axxb'))  # None

"""
2) * - 匹配0次或多次
"""
re_str = r'a\d*b'
print(re.fullmatch(re_str, 'ab'))
print(re.fullmatch(re_str, 'a456465b'))

"""
3) + - 匹配1次或多次
"""

re_str = r'a\d+b'
print(re.fullmatch(re_str, 'ab'))  # None
print(re.fullmatch(re_str, 'a45646546b'))

"""
4){}

{N} - 匹配N次
{M,N} - 匹配M到N次     ? ->  {0,1}
{M,} - 匹配至少M次   *  ->  {0,}
{,N} - 匹配最多N次   +   ->  {1,}
"""
re_str = r'a\d{5}b'
print(re.fullmatch(re_str, 'a47856b'))
print(re.fullmatch(re_str, 'a4785456b'))  # None

re_str = r'a\d{3,5}b'
print(re.fullmatch(re_str, 'a12b'))      # None
print(re.fullmatch(re_str, 'a1248b'))

# 练习:写一个正则表达式判断输入内容是否是整数
# 123 成功 123a 失败 -123 成功 --123 失败 +123 成功

# re_str = r'[+-]?[1-9]\d*'

print('==================贪婪和非贪婪====================')
"""
匹配次数不确定的时候有贪婪和非贪婪两种状态
?,*,+,{M,N},{M,},{,N} - 默认是贪婪的
??, *?,+?,{M,N}?,{M,}?,{,N}? - 非贪婪

贪婪 - 在能匹配成功的前提下，尽可能多的匹配
"""

re_str = r'\d{3,5}'
print(re.search(re_str, 'abc2732939333==='))    # match='27329'

re_str = r'\d{3,5}?'
print(re.search(re_str, 'abc2732939333==='))    # match='273'

re_str = r'\d+'
print(re.search(re_str,'abc2732939333==='))     # match='2732939333'

# 贪婪
re_str = r'a.+b'
print(re.search(re_str, '==a123baasdgb5'))
# match='a123baasdgb'>

# 非贪婪
re_str = r'a.+?b'
print(re.search(re_str, '==a123baasdgb5'))
# match='a123b'
