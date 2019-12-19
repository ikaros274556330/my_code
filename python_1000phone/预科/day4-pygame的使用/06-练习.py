"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((600,600))
window.fill((0,0,0))
pygame.display.set_caption('动画')
x,y = 100,50
pygame.draw.circle(window,(255,255,0),(x,y),20)
pygame.display.flip()

num = 0
speed = 2
speed1 = 2
r = 255
g = 255
b = 255
while True:
    num += 1
    if num % 10000 == 0:
        pygame.draw.circle(window, (0,0,0), (x, y), 20)
        x -= speed
        y -= speed1
        if x < 20:
            speed = choice([-speed-1,-speed-2,-speed+1,-speed+2,-speed])
        elif x > 580:
            speed = choice([-speed-1,-speed-2,-speed+1,-speed+2,-speed])
        if y < 20:
            speed1 = choice([-speed1-1,-speed1-2,-speed1+1,-speed1+2,-speed1])
        elif y > 580:
            speed1 = choice([-speed1-1,-speed1-2,-speed1+1,-speed1+2,-speed1])
        pygame.draw.circle(window, (r, g, b), (x, y), 20)
        pygame.display.update()




    for event in pygame.event.get():
        # ======事件驱动程序======
        if event.type == pygame.QUIT:
            exit()