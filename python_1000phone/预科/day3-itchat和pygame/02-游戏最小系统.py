"""__author:吴佩隆__"""
import pygame
# 1.初始化游戏
pygame.init()

# 2.创建游戏窗口
# 1）创建窗口
# pygame.display.set_mode((宽度，高度)) - 返回一个surface类型的窗口对象
window = pygame.display.set_mode((400,600))
# 2)设置窗口背景颜色
# 窗口对象.fill(颜色)
window.fill((255,0,0))

# 3）设置窗口标题
# pygame.display.set_caption(标题)
pygame.display.set_caption('贪吃蛇')

# 第一次刷新页面（只要对界面的显示进行修改，都需要执行这个方法或者update来刷新页面才会有效）
pygame.display.flip()

# 3.让游戏一直处于运行状态
# flag = True
while True:
    # 4.检测事件
    for event in pygame.event.get():
        # 检测关闭按钮被点击的事件
        if event.type == pygame.QUIT:
            # 退出程序
            exit()
            # flag = False