"""__author__=余婷"""

print('test1开始执行')
# a全局变量
a = 100
print('test1:', a)

# x是全局变量
for x in range(1000):
    print('x:', x)


# func1全局变量
def func1():
    b = 200
    print('test1中的函数1')


func1()


print('test1执行结束!')


