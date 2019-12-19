"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('鼠标事件应用')


pygame.display.flip()

while True:

    # ======检测事件======
    for event in pygame.event.get():
        # 针对不同事件做出不同反应
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if y <= 300:
                R = randint(0,255)
                G = randint(0, 255)
                B = randint(0, 255)
                pygame.draw.circle(window, (R,G,B),event.pos,20,0)
                pygame.display.update()

        elif event.type == pygame.MOUSEMOTION:
            R = randint(0,255)
            G = randint(0, 255)
            B = randint(0, 255)
            pygame.draw.circle(window, (R,G,B),event.pos,2,0)
            pygame.display.update()
