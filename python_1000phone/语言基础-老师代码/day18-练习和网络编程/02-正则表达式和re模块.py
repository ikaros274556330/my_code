"""__author__=余婷"""
import re

# 1.转义符号
"""
在有特殊意义或者特殊功能的符号前加\让它特殊的功能和意义消失
"""
re_str = r'\d\d\.\d\d'
print(re.fullmatch(re_str, '23.34'))

re_str = r'\\wabc'
print(re.fullmatch(re_str, '\wabc'))

# 注意: 独立的有特殊意义的符号，在[]中它的特殊意义会自动消失
re_str = r'[+*]abc'
print(re.fullmatch(re_str, '*abc'))

re_str = r'\d\d[.]\d\d'
print(re.fullmatch(re_str, '23.89'))

re_str = r'[-p+\]]abc'
print(re.fullmatch(re_str, '-abc'))

print(re.fullmatch(r'[\\mabc]', '\\'))

print('========================re模块=========================')
# 2.re模块
# 1)compile(正则表达式)  - 编译创建正则表达式对象
re_obj = re.compile(r'\d{3}')
re_obj.fullmatch('234')

re.fullmatch(r'\d{3}', '345')

# 2)fullmatch(正则表达式, 字符串)  -  让正则表达式和整个字符串进行匹配；如果匹配成功返回匹配对象，匹配失败返回None

result = re.fullmatch(r'(\d{3})([a-z]{4})', '234hksj')
print(result)

# 匹配对象
"""
a.获取匹配结果: 
匹配对象.group()   - 获取整个正则表达式匹配到的结果
匹配对象.group(N)  - 获取第N分组匹配到的结果

b.获取匹配结果在原字符串中的范围
匹配对象.span()

c.获取原字符串
匹配对象.string
"""
print(result.group())   # 234hksj
print(result.group(1))  # 234
print(result.group(2))  # hksj

print(result.span())   # (0, 7)
print(result.span(2))  # (3, 7)

print(result.string)   # 234hksj

# 3）match(正则表达式, 字符串)  -  让字符串开头和正则表达式进行匹配; 返回值是匹配对象或者None
print(re.match(r'\d{3}', '789佳的说法0023-==='))
print(re.match(r'\d{3}abc', '345ABC就开始大锅饭', flags=re.I))

# 4) search(正则表达式, 字符串)  - 在字符串中查找第一个满足正则表达式的子串；返回值是匹配对象或者None
print(re.search(r'\d{3}', '时代峰峻34890shh==23992课时费'))

# 5) findall(正则表达式,字符串)  - 获取字符串中所有满足正则表达式的子串；返回值是列表，列表中的元素是字符串
print(re.findall(r'\d+', '安抚348净宽度34920skdsf45烧开后09823hsd3sd89'))

print(re.findall(r'\d+[a-z]{2}', '安抚348净宽度34920skdsf45烧开后09823hsd3sd89'))
# ['34920sk', '09823hs', '3sd']

print(re.findall(r'(\d+)[a-z]{2}', '安抚348净宽度34920skdsf45烧开后09823hsd3sd89'))
# ['34920', '09823', '3']

print(re.findall(r'(\d+)([a-z]{2})', '安抚348净宽度34920skdsf45烧开后09823hsd3sd89'))
# [('34920', 'sk'), ('09823', 'hs'), ('3', 'sd')]

# 6) finditer(正则表达式,字符串) - 获取字符串中所有满足正则表达式的子串; 返回值是迭代器，迭代器中的元素是匹配对象
result = re.finditer(r'(\d+)([a-z]{2})', '安抚348净宽度34920skdsf45烧开后09823hsd3sd89')
print(list(result))

# 7)split(正则表达式,字符串)  - 以正则表达式匹配到的子串作为切割点，对字符串进行切割; 返回值是列表，列表中的元素是字符串
result = re.split(r'\d+', '暗红色的83大黄金黄色的9罚款0233s闪电发货890')
print(result)   # ['暗红色的', '大黄金黄色的', '罚款', 's闪电发货', '']

# 8)sub(正则表达式,字符串1,字符串2)  -  将字符串2中满足正则表达式的子串全部替换成字符串1；返回值是替换后的字符串
result = re.sub(r'\d+', 'and', '暗红色的83大黄金黄色的9罚款0233s闪电发货890')
print(result)


# 9）参数flags
"""
以上所有的函数都有一个参数flags, 可以加re.I表示匹配的时候忽略大小写；加re.S表示单行匹配(默认是多行匹配re.M)
多行和单行的主要区别: 多行匹配.不能和\n进行匹配；单行.可以和\n进行匹配
"""
print(re.fullmatch(r'a.b', 'a\nb'))   # None
print(re.fullmatch(r'a.b', 'a\nb', flags=re.S))

print(re.search(r'a.+b', '世纪东方anmb\n是否b大括号'))
print(re.search(r'a.+b', '世纪东方anmb\n是否b大括号', re.S))








