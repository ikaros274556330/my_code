"""__author__=余婷"""

# 1.continue
"""
continue是循环体中的关键字
当执行循环体的时候，如果遇到continue,那么当次循环结束，直接进入下次循环的判断
"""
for x in range(4):
    print('====')
    if x % 2 == 0:
        continue
    print('++++')

# 2.break
"""
break是循环体中的关键字
当执行循环体的时候，如果遇到break, 那么整个循环直接结束
"""
print('========================')
for x in range(4):
    print('====')
    break
    print('++++')
print('end', x)


# 功能: 不断输入数字直到输入的是0为止，然后再求输入的所有的奇数的和
sum1 = 0
while True:
    value = int(input('请输入数字:'))
    if value == 0:
        break

    if value % 2 == 0:
        continue

    sum1 += value

print(sum1)

# 3.else
"""
1)完整的for循环
for 变量 in 序列:
    循环体
else:
    代码段
    
2)完整的while循环
while 条件语句:
    循环体
else:
    代码段
    

else中的代码段: 当循环自然死亡(for后的变量数据取完了；while后面的条件为False)，
              else后面的代码段会在循环结束后执行；如果循环是因为遇到break而结束的
              那么else后面代码段就不会执行
else的意义：可以通过判断else中的代码有没有执行来判断循环有没有遇到break       
"""
print('============================')
for x in range(4):
    print(x)
    break
else:
    print('else')
print('~~~~')



# 4.while的循环的用法
"""
while True:
    需要重复执行的代码段
    if 退出循环的条件:
        break
"""

