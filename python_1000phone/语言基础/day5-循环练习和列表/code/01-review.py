"""__author__=吴佩隆"""

# 交换a,b的值的办法

# python写法
a = 10
b = 20

a, b = b, a

# C/java
"""
a = 10
b = 20
t = a
a = b
b = t 
"""

#素数：

# for num in range(101, 201):
#     flag = True
#     for x in range(2, num):
#         if num % x == 0:
#             flag = False
#             break
#
#     if flag == True:
#         print(num)
#
# num = input('输入一个正整数:')
#
# a = [x for x in num]
# a.reverse()
# for i in a:
#     print(i, end='')
#
# print(len(a), '位数')
#
# num = 345
# count = 0
# while True:
#     print(num % 10, end='')
#
#     num //= 10
#     count += 1
#     if num == 0:
#         break
# print()
# print(count, '位数')
