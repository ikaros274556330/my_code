# import pickle
#
#
# def pick(data):
#     with open('data_name.data', 'wb') as f:
#         pickle.dump(data, f)


# def leap_year():
#     while True:
#         try:
#             year = int(input('请输入一个年份:'))
#             break
#         except ValueError:
#             print('请输入有效年份!')
#     return '闰年' if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else '不是闰年'
#
# print(leap_year())

# class Rect:
#     def __init__(self, w:float, h:float):
#         self.w = w
#         self.h = h
#
#     def area(self):
#         return self.w * self.h
#
#     def perimeter(self):
#         return (self.w + self.h) * 2
#

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# a = 0
# for i in range(len(nums)-1):
#     i -= a
#     if nums[i] == nums[i+1]:
#         nums.remove(nums[i])
#         a += 1
#
# print(nums)

# digits = [9,9]
#
# a = ''
# for i in digits:
#     a += str(i)
# a = int(a) + 1
# print(list(str(a)))
# nums = [1,1,2,2,3,4,5,5,6,7]
# i,j = 0,0
# while j < len(nums):
#     print('i:',i,'j:',j)
#     if nums[i] == nums[j]:
#         j+=1
#     else:
#         i+=1
#         nums[i]=nums[j]
#         j+=1
# print(i+1,nums)

# nums = [0, 1, 2, 2, 3, 0, 4, 2]
# val = 2
#
# a = 0
# for i in range(len(nums)):
#     i -= a
#     if nums[i] == val:
#         nums.remove(nums[i])
#         a += 1
#
# print(nums)

# haystack = "hello"
# needle = "ll"
#
# for i in range(len(haystack)-(len(needle)-1)):
#     if haystack[i:i+len(needle)]==needle:
#         print(i)
#         break
# else:
#     print(-1)

# nums = [1,2,3,5,6,78,3,2,4,1,1,1,4,3,1,1,11,1]
# val = 1
#
# for i in nums:
#     if nums[-1] != val:
#
#         nums.insert(0,nums.pop())
#     else:
#         nums.remove(nums[-1])
#     print(nums)

# prices = [7, 6, 4, 3, 1]
#
# num = 0
# if len(prices) == 0 or len(prices) == 1:
#     print(0)
#
# num = prices[0]
# for i in range(1, len(prices) - 1):
#     if prices[i] < num:
#         num = prices[i]
#     print(i, num)
#
#     prices[i] = max((prices[i+1] - prices[i]), (prices[i] - num), 0)
#     print(prices)
#
# print(max(prices[1:-1]))

# nums = [4,1,2,1,2]
# a=None
#
# for i in range(len(nums)):
#     if nums != []:
#         a = nums.pop()
#         if a in nums:
#             nums.remove(a)
#             continue
#         else:
#             print(a)


# prices = [8, 6, 4, 3, 2,5,7,1]
#
# num = 0
# if len(prices) == 0 or len(prices) == 1:
#     print(0)
#
# if len(prices) == 2:
#     if prices[1] > prices[0]:
#         print(prices[1] - prices[0])
#     else:
#         print(0)
#
# num = prices[0]
# for i in range(1, len(prices) - 1):
#     if prices[i] < num:
#         num = prices[i]
#
#     prices[i] = max((prices[i] - num), (prices[i + 1] - prices[i]), (prices[i + 1] - num), 0)
#     print(prices)
# print(max(prices[1:-1]))

numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    if (target-numbers[i]) in numbers:
        print([i+1,numbers.index(target-numbers[i])+1])


