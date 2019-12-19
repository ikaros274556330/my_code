"""__author__=吴佩隆"""

import hashlib

# 1.什么是hashlib
"""
hashlib是python提供的用来通过哈希算法进行加密（产生摘要）的一个库
哈希又叫离散算法，主要包含md5、sha两种算法
"""


# 2.哈希算法加密特点
"""
1)加密后的摘要(密文)是不可逆的
2)相同的数据通过同一种算法产生的摘要是一样的
3)不同长度的数据通过同一种算法产生摘要的长度是一样的
"""


# 3.怎么产生数据的摘要
"""
1)创建hashlib的对象:  hashlib.算法名()
2)添加需要产生摘要的数据:哈希对象.update(数据)
注意：数据必须是二进制数据
3)生成摘要(密文):哈希对象.hexdigest()
"""


# 1.创建哈希对象
hash = hashlib.md5()


# 2.添加数据
pw = '123456'
hash.update(pw.encode())

# 3.生成摘要(密文)
result = hash.hexdigest()
print(result)


print('==============补充:字符串和二进制的相互转换==============')
# python中的bytes就是二进制对应的数据类型
# 1.字符串转二进制
"""
1) bytes(字符串,encoding='utf-8')

2) 字符串.encode()
"""

# 二进制转字符串
"""
1) str(二进制,encoding='utf-8')
2) 二进制.decode(encoding='utf-8')
"""