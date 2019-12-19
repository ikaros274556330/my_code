"""__author__=余婷"""

# 1.查 - 获取字符 (和列表获取元素的方式一样)
"""
1)获取单个字符: 字符串[下标]
2)切片: 字符串[开始下标:结束下标:步长]
3)遍历: 直接变量元素、通过下标遍历
"""
# 注意: 一个空格是一个字符; 按tab键是4个空格，对应4个字符; \t对应一个字符
# 获取单个字符
str1 = '\thello Python!'
print(str1[-2])    # n
print(str1[2])     # e
# print(str1[100])   # IndexError: string index out of range

# 切片
print(str1[2:])     # ello Python!
print(str1[1:-1:2])  # hloPto
print(str1[:3:-1])   # !nohtyP ol

# 遍历
for x in str1:
    print('x:', x)


"""
for 下标,元素 in enumerate(序列):
    循环体
"""
print('==========')
for index, item in enumerate(str1):
    print(index, item)


# 2. 相关操作
# 1)运算符:
# a. +, *
str1 = 'abc'
str2 = '123'
print(str1 + " " + str2)   # abc 123
print(str1 * 3)   # abcabcabc

# b. ==, !=
print('abc' == 'abc')   # True
print('abc' == 'acb')   # False

# >, <, >=, <=
# 字符串1 > 字符串2
# 字符串比较大小比较的是字符串编码值的大小
"""
判断字符是否是小写字母: 'a'<= char <= 'z'
判断字符是否是大写字母: 'A'<= char <= 'Z'
判断字符是否是字母: 'A' <= char <= 'Z' or 'a'<= char <= 'z'
判断字符是否是中文: '\u4e00' <= char <= '\u9fa5'
判断字符是否是数字: '0' <= char <= '9'
"""
print('abcdef' > 'bc')   # False
print('Z' < 'a')    # True
print('abaaaa' < 'aczzzzzz')   # True

char = input('请输入一个字符:')
if '\u4e00' <= char <= '\u9fa5':
    print(char, '是中文')
else:
    print(char, '不是中文')

# 练习: 输入一个字符串，判断这个字符串是否是中文字符串(全是中文)
value = input('请输入:')
for char in value:
    if not '\u4e00' <= char <= '\u9fa5':
        print('非中文字符串')
        break
else:
    print('是中文字符串')

# 2) in / not in
# 字符串1 in 字符串2  ->  判断字符串2中是否包含字符串1
str3 = 'abc 123'
print('b' in str3)   # True  10 in [10, 20, 30]
print('abc' in str3)  # True  [10, 20] in [10, 20, 30]  -> False
print('ac' in str3)   # False

# 3)相关函数: len, str, sorted, reversed
# a.len(字符串)
print(len('\tabc\n123\u4eee'))    # 9
print(len(' abc123'))       # 7
print(len(' '))      # ' ' -> 1; '' -> 0

# b.str(数据)  - 所有数据都可以转换成字符串; 直接将数据的打印值加引号
a = 100
str(a)          # '100'
str(True)       # 'True'
list1 = [10, 20, 30]
str4 = str(list1)     # '[10, 20, 30]'
print(len(str4), str4[0])     # 12  [

# c.sorted(字符串)
str5 = 'pythonH12QWz'
list2 = sorted(str5)
print(list2)   # ['1', '2', 'H', 'Q', 'W', 'h', 'n', 'o', 'p', 't', 'y', 'z']
print(''.join(list2))   # 12HQWhnoptyz




