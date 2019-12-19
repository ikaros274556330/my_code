"""__author__=余婷"""
# import pygame
# pygame.display
# pygame.font

# 1.什么是包
"""
包含__init__.py文件的文件夹； 包是用来管理模块

"""

# ==============1. 导入指定包中指定模块: 使用模块的时候 - 包.模块==============
# import game.display
# print(game.display.bg)   # 背景
# game.display.create_window(100, 200)   # 创建窗口:100x200

# ==============2. 导入指定包中指定模块,对'包.模块'进行重命名==============
# import game.display as display
# print(display.bg)  # 背景
# display.create_window(10, 8)    # 创建窗口:10x8

# ==============3. 导入指定包中指定模块: 使用模块的时候 - 模块==============
# from game import display, font
# print(display.bg)
# display.create_window(1, 2)

# ==============4.直接导入包中指定模块中的指定的变量=======================
# from game.display import create_window, bg
# print(bg)
# create_window(3, 4)

# import game
# print(game.display.bg)
# print(game.bg)

from game import bg, func1
print(bg)
func1()



