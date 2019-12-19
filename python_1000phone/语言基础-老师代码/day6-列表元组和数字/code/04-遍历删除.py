"""__author__=余婷"""

# 坑一： 直接遍历元素删除满足条件的元素 -> 因为遍历的时候列表中的元素取不完导致删不干净
scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
for num in scores:
    print(num)
    if num < 60:
        scores.remove(num)
print(scores)

"""
scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
0 num = 34:  34<60 ->  scores = [89, 56, 45, 90, 34, 54, 20, 90]
1 num = 56:  56<60 ->  scores = [89, 45, 90, 34, 54, 20, 90]
2 num = 90:  90<60
3 num = 34:  34<60 ->  scores = [89, 45, 90, 54, 20, 90]
4 num = 20:  20<60 ->  scores = [89, 45, 90, 54, 90]
5 循环结束!
"""

# 解决坑一: 保证遍历过程能够把需要删除的列表中的元素全部取完
scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
# t_scores = scores[:]
# for num in t_scores:
#     if num < 60:
#         scores.remove(num)
# print(scores)

for num in scores[:]:
    if num < 60:
        scores.remove(num)
print(scores)

# 坑二:
# scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
# length = len(scores)
# for index in range(length):
#     if scores[index] < 60:
#         del scores[index]
# print(scores)
"""
index = 4?
scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
length = len(scores) = 9
index = 0: 34 < 60   ->   del scores[0] -> scores = [89, 56, 45, 90, 34, 54, 20, 90]
index = 1: 56 < 60   ->   del scores[1] -> scores = [89, 45, 90, 34, 54, 20, 90]
index = 2: 90 < 60
index = 3: 34 < 60   ->   del scores[3]  -> scores = [89, 45, 90, 54, 20, 90]
index = 4: 20 < 60   ->   del scores[4]  -> scores = [89, 45, 90, 54, 90]
index = 5: IndexError: list index out of range
"""
scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
index = 0
while index < len(scores):
    # print(scores[index])
    if scores[index] < 60:
        del scores[index]
        continue
        # index -= 1
    index += 1

print(scores)
"""
scores = [34, 89, 56, 45, 90, 34, 54, 20, 90]
index = 0, 0 < 9: 34 < 60  ->  scores = [89, 56, 45, 90, 34, 54, 20, 90]
index = 0, 0 < 8: 89 < 60  ->  index += 1, index = 1
index = 1, 1 < 8: 56 < 60  ->  scores = [89, 45, 90, 34, 54, 20, 90]
index = 1, 1 < 7: 45 < 60  ->  scores = [89, 90, 34, 54, 20, 90]
index = 1, 1 < 6: 90 < 60  ->  index += 1, index = 2
index = 2, 2 < 6: 34 < 60  ->  scores = [89, 90, 54, 20, 90]
index = 2, 2 < 5: 54 < 60  ->  scores = [89, 90, 20, 90]
index = 2, 2 < 4: 20 < 60  ->  scores = [89, 90, 90]
index = 2, 2 < 3: 90 < 60  ->  index += 1, index = 3
index = 3, 3 < 3: 循环结束
"""