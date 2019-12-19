"""__author__=余婷"""

# 1.字符串.capitalize()  - 将字符串的首字母变成大写字母
str1 = 'python'
new_str1 = str1.capitalize()
print(new_str1)

# 97 - 65  == 32; 98-66 == 32
char = 'j'
print(chr(ord(char)-32))

# 2.center/ljust/rjust/zfill
"""
字符串.center(宽度, 填充字符)   # xabcx
字符串.ljust(宽度, 填充字符)    # abcxx
字符串.rjust(宽度, 填充字符)    # xxabc
字符串.zfill(宽度) == 字符串.rjust(宽度, '0') 
"""
print('abc'.center(7, '+'))   # ++abc++
print('abc'.ljust(7, '+'))    # abc++++
print('abc'.rjust(7, '+'))    # ++++abc
print('abc'.zfill(7))         # 0000abc
# 001， 004， 009， 023， 045， 102
num = 21
print(str(num).zfill(3))

# 3.
# 字符串1.count(字符串2)  -> 统计字符串1中字符串2出现的次数
# 字符串1.count(字符串2,开始下标,结束下标)  - 统计字符串1开始下标到结束下标范围内字符串2出现的次数
str2 = 'how are you? i am fine! thank you!'
print(str2.count('you'))   # 2
print(str2.count('a'))     # 3

print(str2.count('you', 0, 15))   # 1
print(str2.count('you', 0, 4))    # 0

# 4.
str1 = 'you'
str2 = 'how are you'
# 判断str2是否以str1结尾
print(str2[-len(str1):] == str1)


# 5.字符串查找
"""
字符串1.find(字符串2) - 获取字符串2第一次在字符串1出现的位置(用大于等于0的下标值表示);
                      字符串2不存在结果是-1
字符串1.index(字符串2) - 获取字符串2第一次在字符串1出现的位置(用大于等于0的下标值表示)；
                       字符串2不存在会报错
"""
str2 = 'how are you? i am fine! thank you!'
print(str2.index('you'))   # 8
print(str2.find('you123'))    # 8
print(str2.find('you123'))   # -1
# print(str2.index('you123'))  # ValueError: substring not found

# 6.join
"""
字符串.join(序列)  - 将序列中的元素用字符串连接在一起产生一个新的字符串；
                   序列中的元素是字符串
"""
str3 = '+'.join('abc')
print(str3)    # a+b+c

str4 = ''.join(['name', 'age', 'gender'])
print(str4)

str5 = ''.join({'a': 1, 'b': 1})
print(str5)    # ab

# 7.字符串替换
"""
1) 字符串1.replace(字符串2, 字符串3)   -> 将字符串1中所有的字符串2都替换成字符串3
2) 
字符串1.maketrans(字符串2,字符串3)  -> 创建字符串2和字符串3一一对应的映射表
字符串1.translate(替换的映射表) 
"""
str2 = 'how are you? i am fine! thank you!'
new_str2 = str2.replace('you', 'me')
print(new_str2)   # how are me? i am fine! thank me!

# 创建映射表
table = str.maketrans('a!', 'b+')
new_str2 = str2.translate(table)   # 将字符串str2中所有的a都替换成b, 所有的!都替换成+
print(new_str2)

# 8.字符串切割
"""
字符串1.split(字符串2)  -  将字符串1中所有的字符串2作为切割点切成多分
"""
str2 = 'how are you? i am fine! thank you!'
print(str2.split(' '))  # ['how', 'are', 'you?', 'i', 'am', 'fine!', 'thank', 'you!']



