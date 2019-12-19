"""__author:吴佩隆__"""
import pygame
from math import *
from random import *
pygame.init()
window = pygame.display.set_mode((500,700))
window.fill((255,255,255))
pygame.display.set_caption('创建图形')

# ======画图======
# 1.画直线
# 1）pygame.draw.line(画在哪,颜色,起点,终点,线宽=1)
pygame.draw.line(window,(255,0,0),(0,20),(200,20),5)

# 2）pygame.draw.lines(画在哪,线的颜色,是否闭合,点列表,线宽=1)
points = [(10,200),(100,20),(220,350),(300,120)]
pygame.draw.lines(window,(0,255,0),True,points,4)

# 2.画圆
# pygame.draw.circle(画在哪,颜色,圆心坐标,半径,线宽=0)
pygame.draw.circle(window,(0,0,255),(200,200),80,1)

# 3.画矩形
# pygame.draw.rect(画在哪,颜色,矩形范围,线宽=0)
# 矩形范围:(x坐标,y坐标,宽,高)
pygame.draw.rect(window,(255,255,0),(10,250,200,100),3)

# 4.画椭圆
# pygame.draw.ellipse(画在哪,颜色,矩形范围,线宽=0)
pygame.draw.ellipse(window,(0,255,255),(10,250,200,100),3)

# 5.画弧线 - 椭圆的一部分
# pygame.draw.arc(画在哪,颜色,矩形范围,起始弧度,终止弧度,线宽=1)
pygame.draw.arc(window,(0,0,0),(10,250,200,100),0,pi/2,2)

# 6.画多边形
# pygame.draw.polygon(画在哪,颜色,点列表,线宽=0)
points = [(300,300),(200,380),(420,500)]
pygame.draw.polygon(window,(220,120,30),points,2)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()