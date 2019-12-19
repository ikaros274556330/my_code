"""__author:吴佩隆__"""
import pygame

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('显示文字')

# =========显示文字=========
# 1.创建字体对象
# pygame.font.Font(字体文件,字体大小)
font1 = pygame.font.Font('./img/aa.ttf',80)

# 2.根据字体对象创建文件对象
# 字体对象.render(内容,True,文字颜色,文字背景颜色=None) - 返回一个surface对象
text = font1.render('hello',True,(0,0,255))

# 3.显示文字
window.blit(text,(0,0))

# 4.获取文字对象大小
w,h = text.get_size()

# 5.缩放和旋转
new_text = pygame.transform.scale(text,(200,50))
window.blit(new_text,(0,0))

new_text = pygame.transform.rotozoom(text,90,1)
window.blit(new_text,(50,400))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()