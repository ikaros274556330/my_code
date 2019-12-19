"""__author__=余婷"""
"""
1.字符串
'',""
不可变，有序

2.字符
\n 
\t
\'
\"
\\
\u4e00
阻止转义

3.字符编码
ASCII、Unicode

chr(编码值)
ord(字符)

4.查
5.相关操作: +, *, >, <, >=, <=, ==, !=
小写字母: 'a' <= char <= 'z'

in / not in

len, str

6.格式字符串
字符串 % (值1, 值2,...)
格式占位符: %s, %d(%-Nd, %Nd), %f(%.Nf), %c

字符串.format(值1, 值2,...)

7.相关方法
字符串1.join(序列)
字符串1.replace(字符2,字符串3, count)
字符串1.split(字符串2) 
字符串1.zfill(长度)
"""
str1 = r'h\nu\kkk\u4e00'

str2 = 'abcef电话机'
str3 = 'abcpzg'
print(str2 > str3)

# print('a' <= str2 <= 'z')


