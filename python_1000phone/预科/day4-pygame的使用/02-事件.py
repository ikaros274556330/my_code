"""__author:吴佩隆__"""
import pygame

pygame.init()
window = pygame.display.set_mode((500,700))
window.fill((255,255,255))
pygame.display.set_caption('事件')

pygame.display.flip()
while True:
    # 获取事件
    for event in pygame.event.get():
        # 有事件发生才会进入for循环

        # ======事件检测======
        """
        1.事件类型
        pygame.QUIT - 点击关闭按钮
        
        1)鼠标相关
        pygame.MOUSEBUTTONDOWN - 鼠标按下
        pygame.MOUSEBUTTONUP - 鼠标松开
        pygame.MOUSEMOTION - 鼠标移动
        
        鼠标事件的位置-pos属性
        """

        # 1.检测当前发生的事件是否是点击关闭
        # event的type值会根据事件的类型不同而改变
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('鼠标按下',event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            print('鼠标松开',event.pos)
        elif event.type == pygame.MOUSEMOTION:
            pass
            # print('鼠标移动')

