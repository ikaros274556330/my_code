"""__author__=余婷"""

print('test2的模块名:', __name__)

a = 100


def func1():
    print('test2中的函数2')


if __name__ == '__main__':
    a = 100
    print('!!!!!!!!!!!')
    print('===============')
    print(a)

    for _ in range(100):
        print('++++++++')

    func1()

if __name__ == '__main__':
    print('**********')
