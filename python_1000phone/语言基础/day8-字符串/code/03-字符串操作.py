"""__author__=吴佩隆"""

# 1.查 - 获取字符(和列表获取元素的方式一样)
"""
1)获取单个字符:字符串[下标]
2)切片:字符串[开始下标:结束下标:步长]
3)遍历:直接遍历元素、通过下标遍历
"""
# 注意：一个空格是一个字符;一个缩进4个空格4个字符;\t对应一个字符
str1 = '\thello python!'
print(str1[-2])  # n
print(str1[2])  # e

print(str1[2:])  # ello python!

# 遍历每个元素
for x in str1:
    print('x:', x)

print('========================')

# 遍历每个元素，返回下标和元素
for x, y in enumerate(str1):
    print(x, y)


# 2.相关操作
# 1)运算符:
# a.+,*

str1 = 'abc'
str2 = '123'
print(str1+' '+str2)    # abc 123
print(str1 * 3)     # abcabcabc

# b.==,!=,is
print('abc' == 'abc')   # True
print('abc' == 'acb')   # False

# >,<,>=,<=
# 字符串1 > 字符串2
# 字符串比较大小比较的是字符串编码值的大小

"""
判断字符是否是小写字母: 'a' <= char <= 'z'
判断字符是否是大写字母: 'A' <= char <= 'Z'
判断字符是否是字母:'A' <= char <= 'Z' or 'a' <= char <= 'z'
判断字符是否是中文: '\u4e00' <= char <= '\u9fa5'
判断字符是否是数字: '0' <= char <= '9'
"""
print('abcdef' > 'bc')  # False
print('Z' < 'a')    # True

# 练习:输入一个字符串,判断这个字符串是否全是中文

str1 = input('请输入字符串:')
for i in str1:
    if not '\u4e00' <= i <= '\u9fa5':
        print('不是中文')
        break
else:
    print('是中文')

# 2)in / not in
# 字符串1 in 字符串2 -> 判断字符串2中是否包含字符串1

# 3)相关函数:len,str,sorted,reversed
# a.len(字符串)

print(len('\taaa1 2\n33'))   # 10 转义字符和空格算一个字符

# b.str(数据) - 所有数据都可以转换成字符串;直接将数据的打印值加引号

a = 100
str(a)      # '100'
str(True)   # 'True'
list1 = [10, 20, 30]
str4 = str(list1)   # '[10, 20, 30]'
print(len(str4), str4[0])   # 12 [

# c.sorted(字符串) - 按编码从小到大排列
str5 = 'python'
list2 = sorted(str5)
print(list2)    # ['h', 'n', 'o', 'p', 't', 'y']
