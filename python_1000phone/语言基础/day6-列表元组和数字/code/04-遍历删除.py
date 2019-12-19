"""__author__=吴佩隆"""

# 坑一:直接遍历元素删除满足条件的 -> 遍历时元素取不完导致删不干净
scores = [34, 89, 56, 45, 90, 54, 20, 90]
for num in scores:
    if num < 60:
        scores.remove(num)

print(scores)

# 解决坑一:保证遍历过程能够把需要删除的列表元素全部取出
scores = [34, 89, 56, 45, 90, 54, 20, 90]
t_scores = scores[:]
for num in t_scores:
    if num < 60:
        scores.remove(num)
print(scores)

# 坑二:
# 方法1
scores = [34, 89, 56, 45, 90, 54, 20, 90]
times = 0
for index in range(len(scores)):
    if scores[index-times] < 60:
        del scores[index-times]
        times += 1
print(scores)

# 方法2
scores = [34, 89, 56, 45, 90, 54, 20, 90]
index = 0
while index < len(scores):
    if scores[index] < 60:
        del scores[index]
        continue

    index += 1

print(scores)