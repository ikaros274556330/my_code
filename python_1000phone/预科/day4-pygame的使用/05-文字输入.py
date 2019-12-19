"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))
pygame.display.set_caption('文字输入')

pygame.display.flip()

font = pygame.font.Font('./sucai/bb.ttf', 30)
x,y=0,0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            # 获取按键对应的字符
            text = chr(event.key)
            text_new = font.render(text,True,(0,0,0))
            window.blit(text_new,(x,y))
            # 获取文字对象宽度和高度
            w,h = text_new.get_size()
            x += w + 2
            if x >= 400:
                x = 0
                y += h
            elif y >= 600:
                x = 0
                y = 0
                window.fill((255,255,255))
            pygame.display.update()