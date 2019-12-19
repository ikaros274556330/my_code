"""__author:吴佩隆__"""
import pygame

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('动画')
# ======游戏首页的静态页面======
x,y = 100,50
pygame.draw.circle(window,(0,255,0),(x,y),50)

pygame.display.flip()
num = 0

speed = 2


while True:

    # ======动画页面自动刷新======
    # 改变球圆心的y值
    num += 1
    if num % 10000 == 0:
    # pygame.time.delay(100)
        pygame.draw.circle(window, (255, 255, 255), (x, y), 50)
        y += speed
        if y > 600 -50:
            y = 600 -50
            speed = -speed
        elif y < 50:
            y = 50
            speed = -speed
        pygame.draw.circle(window, (0, 255, 0), (x, y), 50)
        pygame.display.update()


    for event in pygame.event.get():
        # ======事件驱动程序======
        if event.type == pygame.QUIT:
            exit()