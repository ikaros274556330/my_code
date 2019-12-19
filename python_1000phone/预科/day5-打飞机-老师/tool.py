"""__author__=余婷"""
import pygame
from math import pi


class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    
    
class Button:
    def __init__(self, x, y, w, h, text, color=Color.black, font_size=20, width=2):
        # 按钮基本属性
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.line_width = width
        self.font_size = font_size

        # 按钮点击事件
        self.click_action = None

    def click(self, pos):
        mx, my = pos
        if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
            # print('开始按钮')
            # 如果当前按钮已经绑定点击事件，就执行点击对应的操作
            if self.click_action != None:
                self.click_action()

    def show(self, surface):
        # 1)画弧线1
        rect1 = (self.x, self.y, self.h, self.h)
        pygame.draw.arc(surface, self.color, rect1, pi / 2, pi * 3 / 2, self.line_width)

        rect2 = (self.x + self.w - self.h, self.y, self.h, self.h)
        pygame.draw.arc(surface, self.color, rect2, pi * 3 / 2, pi / 2, self.line_width)

        # 2)画直线
        line1_x1, line1_y1 = self.x + self.h / 2, self.y
        line1_x2, line1_y2 = self.x + self.w - self.h / 2, self.y
        pygame.draw.line(surface, self.color, (line1_x1, line1_y1), (line1_x2, line1_y2), self.line_width)

        line2_x1, line2_y1 = self.x + self.h / 2, self.y + self.h
        line2_x2, line2_y2 = self.x + self.w - self.h / 2, self.y + self.h
        pygame.draw.line(surface, self.color, (line2_x1, line2_y1), (line2_x2, line2_y2), self.line_width)

        # 3)显示文字
        font = pygame.font.Font('./plane/bb.ttf', self.font_size)
        text_obj = font.render(self.text, True, self.color)
        tw, th = text_obj.get_size()
        t_x, t_y = self.x + self.w / 2 - tw / 2, self.y + self.h / 2 - th / 2
        surface.blit(text_obj, (t_x, t_y))



