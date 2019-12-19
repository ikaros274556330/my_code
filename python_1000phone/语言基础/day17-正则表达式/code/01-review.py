"""__author__=吴佩隆"""


# # 自定义错误类型:必须继承Exception这个类
# class ReadOnlyError(Exception):
#     def __str__(self):
#         # __str__返回值就是错误信息描述
#         return 'Give the read-only attribute assignment!'
#
#
# class Person:
#     def __init__(self):
#         self._name = '给我赋值就报错!'
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         raise ReadOnlyError
#
#
# p1 = Person()
#
# print(p1.name)
#
# # p1.name = 100     # 赋值就报错！

# lyrics = """
# [00:00.20]蓝莲花
# [00:00.80]没有什么能够阻挡
# [00:06.53]你对自由地向往
# [00:11.59]天马行空的生涯
# [00:16.53]你的心了无牵挂
# [02:11.27][01:50.22][00:21.95]穿过幽暗地岁月
# [02:16.51][01:55.46][00:26.83]也曾感到彷徨
# [02:21.81][02:00.60][00:32.30]当你低头地瞬间
# [02:26.79][02:05.72][00:37.16]才发觉脚下的路
# [02:32.17][00:42.69]心中那自由地世界
# [02:37.20][00:47.58]如此的清澈高远
# [02:42.32][00:52.72]盛开着永不凋零
# [02:47.83][00:57.47]蓝莲花
# """
#
#
# class Lyrics:
#
#     def __init__(self: str, lyc):
#         self.lyc = lyc
#
#     def parsing(self):                                             # 解析函数
#         list1 = self.lyc.split('\n')                               # 去除换行符
#         list1 = [i for i in list1 if i != '']                      # 去除空元素
#         list1 = [i.strip() for i in list1]                         # 去除空格
#
#         list2 = [[float(i[j:j + 10][1:3] + i[j:j + 10][4:9]),i[i.rfind(']') + 1:]] for i in list1 for j in range(len(i) - 9) if i[j] == '[']
#
#         list2.sort(key=lambda x: x[0])                             # 将列表以时间大小的顺序排列
#
#         return list2
#
#     def show_lyc(self, time1: str):                                # 显示函数
#         time1 = float(time1[0:2] + time1[3:])                      # 将输入的字符串转化成浮点以比较时间大小
#
#         for each in range(len(self.parsing())):                    # 遍历列表，找到大于输入时间的元素返回上一句歌词
#             if time1 <= self.parsing()[each][0]:
#                 return self.parsing()[each-1][1]
#
#
# a = Lyrics(lyrics)
# print(a.parsing())
# print()
# print(a.show_lyc('00:15.53'))
# print(a.show_lyc('02:15.60'))
# print(a.show_lyc('00:49.58'))




