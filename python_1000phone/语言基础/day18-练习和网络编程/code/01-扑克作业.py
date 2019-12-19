"""__author__=吴佩隆"""

# 如果一个类继承enum模块中的Enum类,那么这个就是枚举
from enum import Enum
from random import *


class PokerNum(Enum):
    J = (11, 'J')
    Q = (12, 'Q')
    K = (13, 'K')
    A = (14, 'A')
    Two = (15, '2')
    Three = (3, '3')
    Four = (4, '4')
    Five = (5, '5')
    Six = (6, '6')
    Seven = (7, '7')
    Eight = (8, '8')
    Nine = (9, '9')
    Ten = (10, '10')
    Joker_s = (16, 'joker')
    Joker_b = (17, 'JOKER')


# for item in PokerNum.__members__:
#     print(item)


class Poker:
    def __init__(self, color, num):
        self.color = color  # ♥，♠，♦，♣
        self.num = num  # 2-10，J,Q,K,大王,小王

    def __repr__(self):
        return '{}{}'.format(self.color, self.num.value[1])

    #  重写比较运算，让对象支持 >
    def __gt__(self, other):
        return self.num.value[0] > other.num.value[0]


class PokerGame:
    def __init__(self):

        self.pokers = []

        nums = PokerNum.__members__.items()
        colors = ['♥', '♠', '♦', '♣']
        for num in nums:
            if num[1] == PokerNum.Joker_s or num[1] == PokerNum.Joker_b:
                continue
            for color in colors:
                p = Poker(color, num[1])
                self.pokers.append(p)

        self.pokers.append(Poker('', PokerNum.Joker_b))
        self.pokers.append(Poker('', PokerNum.Joker_s))
        print(self.pokers)

    def __shuffle(self):
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

        # p1.sort(reverse=True, key=lambda item: item.num.value[0])
        # p2.sort(reverse=True, key=lambda item: item.num.value[0])
        # p3.sort(reverse=True, key=lambda item: item.num.value[0])

        p1.sort(reverse=True)
        p2.sort(reverse=True)
        p3.sort(reverse=True)

        return p1, p2, p3, list(poker_iter)


game = PokerGame()
print(game.deal())


# 所有类型都是类;每个运算符都对应一个固定的魔法方法
# 使用运算符其实是在调用魔法方法
