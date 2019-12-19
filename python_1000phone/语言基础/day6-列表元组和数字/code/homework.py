"""__author__=吴佩隆"""


# def count_1(list, obj):
#     count = 0
#     for i in list:
#         if obj == i:
#             count += 1
#     return count
#
#
# list_1 = ['a', 'b', 'c', 'd', 'a', 'a', 'a']
#
# print(count_1(list_1, 'a'))


# def extend1(list1, list2):
#     for i in list2:
#         list1.append(i)
#     return list1
#
#
# list_1 = [1, 2, 3]
# list_2 = 'abc'
#
# print(extend1(list_1, list_2))


# def index1(list_1,obj):
#     num = 0
#     for i in range(len(list_1)):
#         if list_1[i] == obj:
#             num = i
#             break
#     return num
#
#
# list_1 = ['a', 'b', 'c', 'd', 'e', 'f']
#
# print(index1(list_1, 'c'))

# def reverse1(list1):
#     for i in range(len(list_1)):
#         list_1.insert(i, list_1.pop())
#
#     return list_1
#
#
# list_1 = [1, 2, 3, 4, 5, 6, 7]
#
#
# print(reverse1(list_1))

# def reverse2(list1):
#     for i in range(len(list1), 0, -1):
#         list1.append(list1.pop(i-1))
#
#     return list1
#
#
# list_1 = [1, 2, 3, 4, 5, 6]
# 
# print(reverse2(list_1))