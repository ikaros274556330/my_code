"""__author__=吴佩隆"""

import re

# 1.转意符号
"""
在有特殊意义或者特殊功能的符号前加\让它特殊的功能和意义消失
"""

# 注意:独立的有特殊意义的符号,在[]中它的特殊意义会自动消失

# 2.re模块
# 1).compile(正则表达式) - 编译创建正则表达式对象

re_obj = re.compile(r'\d{3}')
re_obj.fullmatch('234')

re.fullmatch(r'\d{3}','234')  # 跟上面一样

# 2)fullmatch(正则表达式,字符串) - 让正则表达式和整个字符串进行匹配;
# 如果成功返回对象，失败返回None。

result = re.fullmatch(r'(\d{3})([a-z]{4})', '234hksj')
print(result)

# 匹配对象
"""
a.获取匹配结果:
匹配对象.group() - 获取整个正则表达式匹配到的结果
匹配对象.group(N) - 获取第N个分组匹配的结果

b.获取匹配结果在原字符中的范围
匹配对象.span()

c.获取原字符串
匹配对象.string
"""

print(result.group())      # 234hksj
print(result.group(1))     # 234
print(result.group(2))     # hksj

print(result.span())       # (0, 7)
print(result.span(1))      # (0, 3)
print(result.span(2))      # (3, 7)

print(result.string)       # 234hksj

# 3) match(正则表达式,字符串) - 让字符串开头和正则表达式进行匹配
# 返回值是匹配对象或者None
# 参数中后面写flags=re.I 忽略大小写

print(re.match(r'\d{3}','789你好哈哈00023=='))
print(re.match(r'\d{3}abc','789ABC的哦设佛',flags=re.I))

# 4) search(正则表达式,字符串) - 在字符串中查找第一个满足正则表达式的子串
# 返回值是匹配对象或None

print(re.search(r'\d{3}','积分送耳机佛369dsef==6576767'))

# 5) findall(正则表达式,字符串) - 获取字符串中所有满足正则表达式的字串;
# 返回值是列表,列表中的元素就是字符串
print(re.findall(r'\d+[a-z]{2}','安抚348金达我26626dsefef烧烤2322hhj3'))
print(re.findall(r'(\d+)[a-z]{2}','安抚348金达我26626dsefef烧烤2322hhj3'))

# 注意:如果正则中有分组,会按照要求查找,但只返回分组中的值!如果两个分组,会以
# 元组的形式返回

# 6)finditer(正则表达式,字符串) - 获取字符串中所有满足正则的子串;
# 返回值是迭代器,迭代器中的元素是匹配对象

result = re.finditer(r'(\d+)([a-z]{2})','安抚348金达我26626dsefef烧烤2322hhj3')
print(list(result))

# 7)split(正则表达式,字符串) - 以正则表达式匹配到的字串作为切割点进行切割
# 返回值是列表,列表中的元素是字符串
result = re.split(r'\d+','打我的的83大王阿瓦达9啊达瓦0233s大撒伟大')
print(result)

# 8)sub(正则表达式,字符串1,字符串2) - 将字符串2中满足正则的字串替换成字符串1
result = re.sub(r'\d+', 'and', '打我的的83大王阿瓦达9啊达瓦0233s大撒伟大')
print(result)

# 9) 参数flags
"""
以上所有的函数都有一个参数flags,可以传re.I表示匹配的时候忽略大小写;
re.S表示可以多行匹配.  可以和\n进行匹配,不加re.S匹配不了
"""
print(re.match(r'a.b', 'a\nb哈哈哈'))   # None
print(re.match(r'a.b', 'a\nb哈哈哈', flags=re.S))

