"""__author__=吴佩隆"""

# 循环嵌套:外面的循环执行一次，里面的循环要执行完毕

# 计算1！+2！+3！+....10!=
num = 0
for i in range(1, 11):
    num1 = 1
    for j in range(1, i+1):
        num1 *= j
    num += num1
    print(num1, num)

print(num)

# 方法二:
sum1 = 0
sum2 = 1
for num in range(1,11):
    sum2 *= num
    sum1 += sum2
print(sum1)