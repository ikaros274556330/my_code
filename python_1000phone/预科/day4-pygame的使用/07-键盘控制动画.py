"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('动画')

# 创建一个静态小球
x,y = 100,25
x_speed = 0     # x速度
y_speed = 0     # y速度
pygame.draw.circle(window,(255,255,0),(x,y),25)


pygame.display.flip()
num = 0
while True:
    num += 1
    if num % 10000 == 0:
        # 涂白
        pygame.draw.circle(window, (255, 255, 255), (x, y), 25)
        # 改变坐标
        x += x_speed
        y += y_speed
        # 重新画新球
        pygame.draw.circle(window, (255, 255, 0), (x, y), 25)
        pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x_speed = 0
                y_speed = -1
            elif event.key == pygame.K_DOWN:
                x_speed = 0
                y_speed = 1
            elif event.key == pygame.K_LEFT:
                x_speed = -1
                y_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 1
                y_speed = 0