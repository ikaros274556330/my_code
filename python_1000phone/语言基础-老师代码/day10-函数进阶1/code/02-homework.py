"""__author__=余婷"""

# 3.输入用户名，判断用户名是否合法(用户名中只能由数字和字母组成)
user_name = 'Abc=123'
for char in user_name:
    if not (char.isalpha() or char.isdigit()):
        print('%s不是合法用户名' % user_name)
        break
else:
    print('%s是合法用户名' % user_name)


# 4.输入用户名，判断用户名是否合法(用户名必须包含且只能包含数字和字母，并且第一个字符必须是大写字母)
user_name = 'Gabc123'
if user_name[0].isupper():
    count = 0   # 统计数字字符的个数

    for char in user_name[1:]:
        if not (char.isalpha() or char.isdigit()):
            print('%s不合法' % user_name)
            break
        else:
            if char.isdigit():
                count += 1
    else:
        if count == 0:
            print('%s不合法' % user_name)
        else:
            print('%s合法' % user_name)

else:
    print('%s不合法' % user_name)


# 5.输入一个字符串，将字符串中所有的数字字符取出来产生一个新的字符串
# 例如：输入'abc1shj23kls99+2kkk'   输出：'123992'
str1 = 'abc1shj23kls99+2kkk'
num_str = ''   # sum1 = 0
for char in str1:
    if char.isdigit():
        num_str += char
print(num_str)


# 6.输入一个字符串，将字符串中所有的小写字母变成对应的大写字母输出  (用upper方法和自己写算法两种方式实现)
# 例如: 输入**'a2h2klm12+' **  输出 **'A2H2KLM12+'**
str2 = 'a2h2klm12+A'
new_str2 = ''
for char in str2:
    if char.islower():
        new_str2 += chr(ord(char) - 32)
    else:
        new_str2 += char
print(new_str2)


# 9.输入字符串，将字符串的开头和结尾变成'+'，产生一个新的字符串
# 例如: 输入字符串**'abac12a'**,  输出**'+bc12+'**
str3 = 'abac123a'
print('+'+str3[1:-1]+'+')


# 11.写程序实现字符串函数find/index的功能(获取字符串1中字符串2第一次出现的位置)
# 例如: 字符串1为:**how are you? Im fine, Thank you!**  , 字符串2为:**you**,  打印**8**
def str_index(str1, str2):
    length = len(str2)
    for index in range(len(str1)):
        if str1[index:index+length] == str2:
            print(index)
            break
    else:
        print(-1)


str4 = 'how are you? Im fine, Thank you!'
str5 = 'are'
str_index(str4, str5)

# 12.获取两个字符串中公共的字符
# 例如: 字符串1为:**abc123**, 字符串2为: **huak3** , 打印:**公共字符有:a3**
str6 = 'abc123'
str7 = 'huak3'
print(''.join(set(str6) & set(str7)))

