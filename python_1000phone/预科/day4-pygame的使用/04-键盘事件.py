"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))
pygame.display.set_caption('键盘事件')

font1 = pygame.font.Font('./sucai/bb.ttf', 20)

pygame.display.flip()
w = 0
h = 0
while True:
    """
    1.键盘按下
    pygame.KEYDOWN - 按键按下
    pygame.KEYUP - 按键弹起

    键盘事件中要关注按下的是哪个:event.key
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            R = randint(0,255)
            G = randint(0, 255)
            B = randint(0, 255)
            text = font1.render(chr(event.key), True, (R, G, B))
            window.blit(text, (w, h))
            w += 11
            pygame.display.update()
            if event.key == pygame.K_KP_ENTER:
                h += 20
                w = 0

            # if event.key == pygame.K_UP:
            #     print('上')
            # elif event.key == pygame.K_DOWN:
            #     print('下')
            # print('按键按下',event.key,(chr(event.key)))
        # elif event.type == pygame.KEYUP:
        #     print('按键弹起')