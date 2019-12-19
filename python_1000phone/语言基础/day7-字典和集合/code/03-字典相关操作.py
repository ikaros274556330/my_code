"""__author__=吴佩隆"""

# 1.运算符: ==,!=,is
# 不支持+，*，<，<=，>，>=
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True

# 2.in/not in
# key in 字典 / key not in 字典  -  判断key是否存在/不存在
dog = {'name': '旺财', 'age': 3, 'kind': '中华田园犬'}
print('name' in dog)  # True
print('旺财' in dog)  # False

# 3.len, dict
# len(字典) - 字典中键值对的个数
# dict(数据) - 将指定的数据抓换成字典;
# 数据要求:
# 1)数据本身是序列
# 2)序列中的元素也是序列
# 3)小序列中的元素有且只有两个,第一个元素不可变

# 字典转列表 - 将字典所有key取出来作为列表元素
list1 = list(dog)
print(list1)        # ['name', 'age', 'kind']
