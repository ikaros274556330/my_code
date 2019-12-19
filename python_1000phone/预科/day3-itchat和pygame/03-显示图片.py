"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('显示图片')

# =========显示图片=========
# 1.加载图片
# pygame.image.load(图片地址) - 返回类型是surface图片对象
image1 = pygame.image.load('./img/tel.png')
# 2.显示图片
# 窗口对象.blit(显示对象，坐标)
window.blit(image1,(100,0))

# 3.获取图片大小
# 图片对象.get_size()
w1,h1 = image1.get_size()
# print(w1,h1)
window.blit(image1,(400-w1,600-h1))

image2 = pygame.image.load('./img/sun.png')
w2,h2 = image2.get_size()

x2 = 200 - w2/2
y2 = 300 - h2/2
window.blit(image2,(x2,y2))

# 4.图片的缩放和旋转
# 1)缩放
# pygame.transform.scale(缩放对象，目标大小)-返回缩放之后的对象
new_image2 = pygame.transform.scale(image2,(80,80))
window.blit(new_image2,(0,0))

# 2)比例旋转缩放:
# pygame.transform.rotozoom(缩放对象，旋转角度，缩放比例)
new_image2 = pygame.transform.rotozoom(image2,0,0.2)
window.blit(new_image2,(0,100))

new_image2 = pygame.transform.rotozoom(image2,90,1)
window.blit(new_image2,(0,400))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()