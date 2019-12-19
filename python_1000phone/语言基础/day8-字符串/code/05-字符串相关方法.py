"""__author__=吴佩隆"""

# 1.字符串.capitalize() -将字符串的首字母变成大写
print('python'.capitalize())  # Python

# 97-65 == 32; 98-66 == 32
char = 'j'
print(chr(ord(char) - 32))  # J  小写转大写

# 2.center/ljust/rjust/zfill

"""
字符串.center(宽度,填充字符)
字符串.ljust(宽度,填充字符)
字符串.rjust(宽度,填充字符)
字符串.zfill(宽度) == 字符串.rjust(宽度,'0')
"""

print('abc'.center(7, 'X'))  # XXabcXX
print('abc'.ljust(7, 'X'))  # abcXXXX
print('abc'.rjust(7, 'X'))  # XXXXabc
print('abc'.zfill(7))  # 0000abc

# 3.count()
# 字符串1.count(字符串2) - 统计字符串2在字符串1中出现了多少次
str2 = 'hello python!'
print(str2.count('o'))  # 2
print(str2.count('th'))  # 1

# 4.字符串查找
"""
字符串1.find(字符串2)  -  获取字符串2第一次出现在字符串1中的位置，没有不会报错
字符串1.index(字符串2)    跟上面一样，但没有会报错
"""

# 5.join
"""
字符串.join(序列) - 将序列中的元素与字符串拼接在一起，产生新的字符串
                    序列中的元素必须是字符串
"""
str3 = '+'.join('雷军牛逼')  # 雷+军+牛+逼
print(str3)

# 6.字符串替换
"""
1)字符串1.replace(字符串2,字符串3) -> 将1中2替换成3，产生新的
2)
字符串1.maketrans(字符串1,字符串2) -> 创建字符串和字符串3一一对应的映射表
字符串1.translate(替换映射表)
"""
str4 = 'how are you? I am fine 3Q!'

print(str4.replace('a', 'what'))  # how whatre you? I whatm fine 3Q!

table = str.maketrans('a!', 'b+')  # 将字符串4中的a变成b,!变成+
new_str4 = str4.translate(table)
print(new_str4)  # how bre you? I bm fine 3Q+

# 7.字符串切割
"""
字符串1.split(字符串2) - 将字符串1中所有字符串2作为切割点切成多份
"""
str5 = 'how are you? I am fine 3Q!'
print(str5.split(' '))  # ['how', 'are', 'you?', 'I', 'am', 'fine', '3Q!']
