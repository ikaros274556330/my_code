# num = 0
#
# for i in range(101, 201):
#     for j in range(2, int(i**(1/2)+1)):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#         num += 1
#
#
# print(num)

# num = 0
#
# for i in range(100,1000):
#     if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
#         num += 1
#         print(i)

# num = 0
#
# for i in range(100, 1000):
#     if (i//100)**3 + (i/100//1)**3 + (i % 10)**3 == i:
#         print(i)

# num = int(input('斐波那契数列第几个:'))
# a = 1
# b = 1
#
# for i in range(1, num):
#     a, b = b, a+b
#
# print(a)

# num = 1
# num1 = 0
# for i in range(1,21):
#     num *= 1/i
#     num1 += num
# print(num)

# num = 1
# num1 = 0
# while num <= 100:
#     num1 += num
#     num += 1
# num2 = num1/100
#
# print(num1,num2)

# num = 1
# num1 = 0
# while num <= 100:
#     if num % 7 != 0:
#         num1 += num
#     num += 1
#
#
# print(num1)

# num = 0
# num1 = 1
# while num1:
#     num1 = int(input('请输入大于0的数字:'))
#     if num1 > 0:
#         num += num1
#     elif num1 < 0:
#         print('不累加')
# print(num)


# num = input('输入0-9的整数:')
# count = int(input('输入项数:'))
# num1 = 0
# for i in range(1, count+1):
#     num1 += int(num*i)
#
# print(num1)

# num1 = int(input('第一个整数:'))
# num2 = int(input('第二个整数:'))
# num3 = int(input('第三个整数:'))
#
#
# if num1 < num2:
#     if num1 < num3:
#         print(num1)
#         if num2 < num3:
#             print(num2)
#             print(num3)
#         else:
#             print(num3)
#             print(num2)
#     else:
#         print(num3)
#         print(num1)
#         print(num2)
# else:
#     if num2 < num3:
#         print(num2)
#         if num3 < num1:
#             print(num3)
#             print(num1)
#         else:
#             print(num1)
#             print(num3)
#     else:
#         print(num3)
#         print(num2)
#         print(num1)


# num1 = int(input('第一个整数:'))
# num2 = int(input('第二个整数:'))
# num3 = int(input('第三个整数:'))
#
# list_1 = [num1, num2, num3]
# list_1.sort()
# for i in list_1:
#     print(i)

# list_1 = []
#
# for i in range(1, 4):
#     a = int(input('请输入第%d个整数:' % i))
#     list_1.append(a)
# list_1.sort()
# for i in list_1:
#     print(i)

# n = int(input('输入一个整数:'))
#
# for i in range(n+1):
#     if i & 1 == 1:
#         print(' '*int((n/2)), '*'*i)
#     n -= 1

# for i in range(1,10):
#     for j in range(1,10):
#         if i >= j:
#             print('%dX%d=%d' % (j, i, j*i),end=' ')
#     print()


# for i in range(34):
#     for j in range(51):
#         for k in range(101):
#             if (i*3 + j*2 + k*0.5 == 100) and (i+j+k == 100):
#                 print('大马%d匹，中马%d匹，小马%d匹' % (i, j, k))

# for i in range(21):           # 21只公鸡超过100文
#     for j in range(34):       # 34只母鸡超过100文
#         for k in range(101):                # 总数不过百
#             if k % 3 == 0:
#                 l = k / 3
#                 if (i*5 + j*3 + l == 100) and (i + j + k == 100):
#                     print('公鸡%d只,母鸡%d只,雏鸡%d只' % (i, j, k))
# num = 0
# for i in range(7):
#     for j in range(51):
#         for k in range(21):
#             if i*15+j*2+k*5 == 100:
#                 num +=1
#                 print('洗发水%d瓶,香皂%d块,牙刷%d支' % (i, j, k))
# print(num,'种情况')
