# """__author__=吴佩隆"""
#
# from random import randint
#
# list_1 = ['张三', '张三', '张三', '张三', '张三', '李四', '张三', '李四', '张三', '李四']
#
# for i in range(len(list_1)):
#     for j in range(len(list_1)-1):
#         if list_1[j] > list_1[j+1]:
#             list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
# print(list_1)
#
#
# list_2 = list_1[:]
# for j in range(len(list_1)-1):
#     if list_1[j] == list_1[j+1]:
#         list_2.remove(list_1[j])
#         print(list_2)
# print(list_2)
#

s = '{[]}'
print(s[0]==s[-1])
def A(s):
    a = ['()', '[]', '{}']
    if s != '':
        if len(s) & 1 == 0:
            if s[0] == s[-1]:
                for i in range(len(s) // 2):
                    if s[i] != s[-1 - i]:
                        return False
                else:
                    return True


            else:
                num = 0
                for i in range(len(s) // 2):
                    if (s[i + num] + s[i + num + 1]) not in a:
                        return False
                    num += 1
                else:
                    return True
        else:
            return False
    else:
        return False

print(A(s))