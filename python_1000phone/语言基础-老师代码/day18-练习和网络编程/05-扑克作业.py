"""__author__=余婷"""
# 如果一个类继承enum模块中的Enum类，那么这个就是枚举
from enum import Enum
from random import shuffle
from copy import copy


# 5.写一个扑克游戏类， 要求拥有发牌和洗牌的功能(具体的属性和其他功能自己根据实际情况发挥)
class PokerNum(Enum):
    Three = (3, '3')
    Four = (4, '4')
    Five = (5, '5')
    Six = (6, '6')
    Seven = (7, '7')
    Eight = (8, '8')
    Nine = (9, '9')
    Ten = (10, '10')
    J = (11, 'J')
    Q = (12, 'Q')
    K = (13, 'K')
    A = (14, 'A')
    Two = (15, '2')
    Joker_S = (16, 'Joker')
    Joker_B = (17, 'JOKER')


# print(PokerNum.J, PokerNum.J.value)
# # # 获取当前枚举类中所有的数据
# for item in PokerNum.__members__.items():
#     print(item, type(item[1]))


class Poker:
    def __init__(self, color: str, num: PokerNum):
        self.color = color  # ♥、♠、♣、♦
        self.num = num   # 2-10，J,Q,K,A; 大王、小王

    def __repr__(self):
        return '{}{}'.format(self.color, self.num.value[1])

    # 让Poker对象可以比较大小(>)
    # p1 > p2  ->  p1.__gt__(p2)
    def __gt__(self, other):
        return self.num.value[0] > other.num.value[0]

    # p1 + p2  -> p1.__add__(p2)
    def __add__(self, other):
        return self.num.value[0] + other.num.value[0]

    # p1 * N  ->  p1.__mul__(N)
    def __mul__(self, other):
        list1 = []
        for _ in range(other):
            list1.append(copy(self))
        return list1


class PokerGame:
    def __init__(self):
        # 一副牌
        self.pokers = []
        # 创建牌
        nums = PokerNum.__members__.items()
        colors = ['♥', '♠', '♣', '♦']
        for num in nums:
            if num[1] == PokerNum.Joker_S or num[1] == PokerNum.Joker_B:
                continue
            for color in colors:
                # 创建牌对象
                p = Poker(color, num[1])
                self.pokers.append(p)

        self.pokers.append(Poker('', PokerNum.Joker_S))
        self.pokers.append(Poker('', PokerNum.Joker_B))
        # print(self.pokers)

    def __shuffle(self):
        # 方法一: 转换成集合
        # print(set(self.pokers))
        # 方法二: random.shuffle(列表)
        shuffle(self.pokers)
        print(self.pokers)

    def deal(self):
        self.__shuffle()
        poker_iter = iter(self.pokers)
        p1 = []
        p2 = []
        p3 = []
        for _ in range(17):
            p1.append(next(poker_iter))
            p2.append(next(poker_iter))
            p3.append(next(poker_iter))

        # 排序
        # p1.sort(key=lambda item: item.num.value[0], reverse=True)
        # p2.sort(key=lambda item: item.num.value[0], reverse=True)
        # p3.sort(key=lambda item: item.num.value[0], reverse=True)
        p1.sort(reverse=True)
        p2.sort(reverse=True)
        p3.sort(reverse=True)

        return p1, p2, p3, list(poker_iter)


game = PokerGame()
# game.shuffle()
print(game.deal())

print(game.deal())

print('==============补充：运算符重载=================')
# 所有的类型都是类;每个运算符都对应一个固定的魔法方法,使用运算符其实是在调用对应的魔法方法
# 10 + 29
p1 = Poker('♠', PokerNum.A)
p2 = Poker('♣', PokerNum.J)
# print(p1 > p2)
print(p1 + p2)
print(p1 < p2)
print(p1 * 4)
# print(p1 * p2)   # TypeError: 'Poker' object cannot be interpreted as an integer

