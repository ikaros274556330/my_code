"""__author__=余婷"""

# 1.什么是生成式
"""
生成式就是生成器；只是写法上更简洁，只有一行代码

1)语法一:
生成器 = (表达式 for 变量 in 序列) 

相当于普通生成器:
def 函数名():
    for 变量 in 序列:
        yield 表达式
生成器 = 函数名()


2)语法二:
生成器 = (表达式 for 变量 in 序列 if 条件语句)

def 函数名():
    for 变量 in 序列:
        if 条件语句:
           yield 表达式 
生成器 = 函数名()

3)语法三
生成器 = (表达式 for 变量1 in 序列1 for 变量2 in 序列2)

def 函数名():
    for 变量1 in 序列1:
        for 变量2 in 序列2:
           yield 表达式  
生成器 = 函数名()
"""

# 2.列表生成式
"""
将上面生成式语法中所有的()变成[],结果就会由原来的生成器，变成列表

生成器 = (表达式 for 变量 in 序列) 
[表达式 for 变量 in 序列]  == list(生成器)
"""


# 写一个生成器：产生数字1~10
# 方法一:
def create_num():
    for num in range(1, 11):
        yield num


gen1 = create_num()

# 方法二:
gen2 = (num for num in range(1, 11))
print(gen2)   # <generator object <genexpr> at 0x10e3c0468>
# print(next(gen2))
# print(next(gen2))

print([num for num in range(1, 11)], list(gen2))


gen3 = ('str%s' % x for x in range(5))
print(next(gen3))


def func2():
    for x in range(5):
        yield 'str%s' % x


gen4 = (x for x in range(0, 10) if x % 2)
# gen4中的元素:  1,3,5,7,9
for num in gen4:
    print('num:', num)
