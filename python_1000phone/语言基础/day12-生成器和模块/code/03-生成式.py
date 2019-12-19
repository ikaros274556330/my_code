"""__author__=吴佩隆"""

# 1.什么是生成式
"""
生成式就是生成器;只是写法更简洁

1)语法一:
生成器 = (表达式 for 变量 in 序列)

def 函数名():
    for 变量 in 序列:
        yield 表达式
生成器 = 函数名()

2)语法二:
生成器 = (表达式 for 变量 in 序列 if 条件语句)

3)语法三:
生成器 = (表达式 for 变量1 in 序列1 for 变量2 in 序列2)
"""


# 2.列表生成式
"""
将上面所有语法中的(),变成[]。结果就是原来生成器变成列表
列表生成 = [表达式 for 变量 in 序列] = list(生成器)
"""


gen2 = (num for num in range(1, 11))
print(next(gen2))
print(next(gen2))
print('===========================================')
gen3 = (num for num in range(10) if num % 2 != 0)
print(next(gen3))
print(next(gen3))

print('===========================================')
gen4 = (x for x in range(0, 10) if x % 2)
for i in gen4:
    print(i)
