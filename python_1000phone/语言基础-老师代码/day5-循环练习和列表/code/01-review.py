"""__author__=余婷"""

# 1.if-elif-else
"""
if 条件语句:
    代码段
elif 条件语句:
    代码段
elif 条件语句:
    代码段
elif 条件语句:
    代码段
elif 条件语句:
    代码段
...
else:
    代码段
"""
# 2.for
"""
for 变量 in 序列:
    循环体
else:
    代码段
    
range(N)   -> N > 0
range(M, N)    -> M < N
range(M, N, step)   -> 如果step > 0, M < N; 如果step < 0, M > N
"""
for x in range(1, 10, 2):
    print(x)

print('==============================')
for x in range(10, 0, -1):
    print(x)

# 3.while循环
"""
while 条件语句:
    循环体
else:
    代码段
    

while True:
    需要重复执行操作
    if 循环结束的条件:
        break
"""
# 4.关键字
"""
continue: 结束一次循环
break: 结束整个循环
else: 循环自然死亡执行else中的代码；如果遇到break,不执行else中的代码
"""



