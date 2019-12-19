"""__author__=余婷"""

# 1.什么是递归函数
"""
声明函数的时候调用函数本身， 这样的函数就是递归函数(自己调用自己)
递归可以实现循环效果, 原则上除了死循环，其他的循环递归都可以实现
"""
# def func1():
#     print('========')
# #
# #     func1()
#
# func1()

# 2.递归怎么用
"""
使用递归的套路:
a.设置临界值 - 循环结束的条件(保证函数结束)
b.找关系 - 找f(n)和f(n-1)的关系
c.假设函数的功能已经实现，通过f(n-1)去实现f(n)的功能
"""


# 写一个递归函数，计算1+2+3+...n
def yt_sum(n):
    # 1.找临界值
    if n == 1:
        return 1

    # 2.找关系
    """
    f(n) ->  1+2+3+...+n-1+n
    f(n-1) -> 1+2+3+...+n-1
    f(n) = f(n-1) + n
    """
    # 3.用f(n-1)实现f(n)的功能
    return yt_sum(n-1)+n


# print(yt_sum(100))
# print(yt_sum(10))
print(yt_sum(5))

"""
yt_sum(5): n=5; if 5==1;   return yt_sum(4)+5    1+2+3+4+5
yt_sum(4): n=4; if 4==1;   return yt_sum(3)+4    1+2+3+4
yt_sum(3): n=3; if 3==1;   return yt_sum(2)+3    1+2+3
yt_sum(2): n=2; if 2==1;   return yt_sum(1)+2    1+2
yt_sum(1): n=1; if 1==1; return 1
"""


# 写一个递归函数，求斐波那契数列的第n个数
# 1,1,2,3,5,8,13,21,....
def series(n):
    # 1.找临界值
    if n == 1 or n == 2:
        return 1
    # 2.关系: f(n) = f(n-1)+f(n-2)
    return series(n-1)+series(n-2)


print(series(9))


# 练习:递归实现f(n)
"""
n = 4
*
**
***
****

n = 3
*
**
***
"""


def print_star(n):
    if n == 1:
       print('*')
       return

    # 关系: 实现f(n-1)的功能后，再打印一行n个*
    print_star(n-1)
    print(n*'*')


print_star(5)




