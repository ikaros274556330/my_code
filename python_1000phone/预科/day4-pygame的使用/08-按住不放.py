"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((0,0,0))
pygame.display.set_caption('按住不放')

x,y = 200,200
x_speed,y_speed = 0,0
image1 = pygame.image.load('./sucai/Icon-ldpi.png')
w,h = image1.get_size()
window.blit(image1,(x,y))

pygame.display.flip()
flag = False  # 图片是否移动
while True:
    # 控制图片是否移动
    if flag == True:
        pygame.draw.rect(window,(0,0,0),(x,y,w,h))
        x += x_speed
        y += y_speed
        window.blit(image1, (x, y))
        pygame.display.update()
        pygame.time.delay(5)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # 弹起不动
        elif event.type == pygame.KEYUP:
            flag = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                flag = True
                x_speed = 0
                y_speed = -1
            elif event.key == pygame.K_DOWN:
                flag = True
                x_speed = 0
                y_speed = 1
            elif event.key == pygame.K_LEFT:
                flag = True
                x_speed = -1
                y_speed = 0
            elif event.key == pygame.K_RIGHT:
                flag = True
                x_speed = 1
                y_speed = 0


