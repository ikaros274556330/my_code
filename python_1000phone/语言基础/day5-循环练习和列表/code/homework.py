"""__author__=吴佩隆"""
from random import randint

# nums = [x for x in range(randint(1, 50))]
# number = nums[int(len(nums) / 2)]
# number1 = nums[int(len(nums) / 2)-1]
#
# print(nums)
#
# if len(nums) % 2 != 0:
#     print(number)
# else:
#     print(number1, number)
#


# 冒泡排序法
# list_1 = []
#
# for i in range(50):
#     list_1.append(randint(1,100))
#
# print(list_1)
# for j in range(len(list_1)):
#     for k in range(len(list_1)-1):
#         if list_1[k] > list_1[k+1]:
#             list_1[k+1], list_1[k] = list_1[k], list_1[k+1]
#
# print(list_1)


# list_1 = [x for x in range(randint(1, 10))]
# print(list_1)
#
# for i in range(len(list_1)):
#     list_1[i] *= 2
#
# print(list_1)

# list_1 = ['a', 'b', 'c', 'b', 'd', 'e', 'c']
# list_2 = []
#
# for i in list_1:
#     if i not in list_2:
#         list_2.append(i)
# print(list_2)



# list_1 = []
#
# for i in range(10):
#     list_1.append(randint(0, 6535))
# print(list_1)
#
# list_2 = []
#
# for i in list_1:
#     list_2.append(chr(i))
# print(list_2)


# scores_list = [5, 7, 9, 6, 4, 5, 10, 6, 6, 9, 8, 7, 5, 3, 1]
#
# scores_list.sort()
# a = scores_list.pop()
# b = scores_list.pop(0)
# print(a, b)
#
# print('平均分', sum(scores_list)/len(scores_list))

# A = [1, 'a', 4, 90]
# B = ['a', 8, 'j', 1]
# C = []
#
# for i in A:
#     for j in B:
#         if i == j:
#             C.append(i)
#
# print(C)



# list_1 = []
# for i in range(10):
#     list_1.append(randint(1, 100))
# print(list_1)
#
# num = list_1[0]
# for i in list_1:
#     if i > num:
#         num = i
# print(num)

# times = 0
# nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]
# nums_1 = nums[:]
#
# for i in range(len(nums_1)):
#     for j in range(len(nums_1)):
#         if i != j:
#             if nums_1[i] == nums_1[j]:

# nums = [1, 2, 3, 1, 4, 2, 1, 3, 7, 3, 3]
#
# times = 0
# number = 0
# for i in nums:
#     if nums.count(i) > times:
#         times = nums.count(i)
#         number = i
# print(number)

# num1 = 0.08/1000
# height = 8848.13
#
# n = 0
#
# while num1 < height:
#     num1 *= 2
#     n += 1
# print(n)


# month = int(input('Please enter a month:'))
#
# a, b = 1, 1
#
# for i in range(month-1):
#     a, b = b, a+b
# print(a*2)


# num = int(input('输入一个正整数:'))
# num1 = num
# numbers = []
#
# while num != 1:
#     for i in range(2, num+1):
#         if num % i == 0:
#             numbers.append(i)
#             num //= i
#             break
#
# if len(numbers) == 1:
#     print('%d = 1 X %d' % (num1, num1))
# else:
#     print(num1, '=', end='')
#     for i in range(len(numbers)-1):
#         print('', numbers[i], 'X', end='')
# print('', numbers[-1], end='')

# num1 = int(input('第一个正整数:'))
# num2 = int(input('第二个正整数:'))
#
# a = [num1, num2]
# a.sort()                # 判断两个数的大小
#
# L = a[1]
# S = a[0]
#
# t = 1
# while L % S != 0:       # 辗除法思路，反复用较小数取余
#     t = L % S
#     L = S
#     S = t
# print('最大公约数', S)
#
# list_num1 = []
# list_num2 = []
#
#
# while num1 != 1:                 # 获取第一个数的质因数
#     for i in range(2, num1+1):
#         if num1 % i == 0:
#             list_num1.append(i)
#             num1 //= i
#             break
#
# while num2 != 1:                   # 获取第二个数的质因数
#     for i in range(2, num2+1):
#         if num2 % i == 0:
#             list_num2.append(i)
#             num2 //= i
#             break
#
# # print(list_num1)        # num1的质因数分解
# # print(list_num2)        # num2的质因数分解
#
# numbers_list = []       # 他们所有的质因数集合
#
# for i in list_num1:             # 没有的元素就添加
#     if i not in numbers_list:
#         numbers_list.append(i)
# for i in list_num2:
#     if i not in numbers_list:
#         numbers_list.append(i)
#
# for i in numbers_list[:]:           # 遍历所有质因数，判断当前质因数与原来两个列表里的差值
#     chazhi = list_num1.count(i) - numbers_list.count(i)
#     if chazhi > 0:                  # 如果插值大于0，则表示当前质因数不足需要添加
#         for j in range(chazhi):     # 根据插值循环添加质因数，保证相同质因数在结果列表里获得最大数量
#             numbers_list.append(i)
#
# for i in numbers_list[:]:
#     chazhi = list_num2.count(i) - numbers_list.count(i)
#     if chazhi > 0:
#         for j in range(chazhi):
#             numbers_list.append(i)
# B = 1
#
# for i in numbers_list:             # 结果列表里所有元素相乘就是最小公倍数
#     B *= i
# # print(numbers_list)
#
# print('最小公倍数', B)


# n = 1000
# numbers = []
#
# for i in range(1, n+1):
#     yin_zi = []             # 储存所有因子
#     for j in range(1, i):
#         if i % j == 0 and j not in yin_zi:  # 判断是否重复
#             yin_zi.append(j)
#     if sum(yin_zi) == i:
#         numbers.append(i)
#
# print(numbers)

# list_p = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# list_r = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# year = int(input('请输入年份:'))
# month = int(input('请输入月份'))
# day = int(input('请输入几号:'))
#
# n = 0
# for i in range(1, month):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         n += list_r[i-1]
#     else:
#         n += list_p[i-1]
# n += day
# print('%d年的第%d天' % (year, n))


# num = int(input('输入一个4位整数:'))

# new_list = []
# for i in str(num):
#     new_list.append((int(i)+5) % 10)

# new_list[0], new_list[1], new_list[2], new_list[3] = new_list[3], new_list[2], new_list[1], new_list[0]
#
# new_number = ''
# for i in new_list:
#     new_number += str(i)
# new_number = int(new_number)
#
# print('%d加密之后的数字是:%d' % (num, new_number))


# n = int(input('第几个丑数:'))
# numbers = []
# the_number = 1
# while len(numbers) != n:        # 保证最后丑数数列能取到值
#     num = the_number
#     yin_zi = [1]                    # 收集当前整数的所有质因分子
#     while num != 1:
#         for i in range(2, num+1):
#             if num % i == 0:
#                 yin_zi.append(i)
#                 num //= i
#                 break
#     for j in yin_zi:        # 遍历所有质因分子，如果有2，3，5以外的就pass掉
#         if j not in [1, 2, 3, 5]:
#             break
#     else:
#         numbers.append(the_number)  # 循环结束没有发现就添加入列表
#     the_number += 1
# print(numbers[n-1])



