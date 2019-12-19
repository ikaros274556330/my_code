"""__author__=吴佩隆"""


# 1.什么是包
"""
包含__init__.py文件的文件夹;包是用来管理模块
"""

# # 1.导入指定包中指定模块
# import game.display
#
#
# print(game.display.bg)
# game.display.create_window(100, 200)


# 2.导入指定包中指定模块，对'包.模块'进行重命名
# import  game.display as display
# print(display.bg)
# display.create_window(10, 8)

# 3.导入包中指定模块
# from game import display, font
# print(display.bg)


# 4.直接导入包中指定模块中的指定变量
from game.display import create_window, bg
print(bg)