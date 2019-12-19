"""__author__=余婷"""
# 1.数学集合运算: 并集(|), 交集(&), 差集(-), 对称差集(^), >/<(包含关系)
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

# 1)并集: 集合1 | 集合2  ->   将两个集合合并在一起产生一个新的集合
print(set1 | set2)   # {1, 2, 3, 4, 5, 6, 7, 8}

# 2)交集: 集合1 & 集合2  ->   获取两个集合的公共部分产生一个新的集合
print(set1 & set2)   # {4, 5, 6}

# 3)差集: 集合1 - 集合2  ->   获取集合1中去掉集合2剩下的部分
print(set1 - set2)    # {1, 2, 3}
print(set2 - set1)    # {8, 7}

# 4)对称差集：集合1 ^ 集合2  ->  获取集合1和集合2合并后去掉公共部分剩下的部分
print(set1 ^ set2)    # {1, 2, 3, 7, 8}

# 5) 集合1 > 集合2  - 判断集合1中是否包含集合2
#    集合1 < 集合2  - 判断集合2中是否包含集合1
set3 = {5, 6, 7, 8, 9}
set4 = {1, 2}
print(set3 > set4)    # False
print(set3 > {5, 6})  # True
print(set3 > {5, 6, 1})   # False

