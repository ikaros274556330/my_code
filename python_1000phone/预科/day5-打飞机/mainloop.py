"""__author:吴佩隆__"""
import pygame
from tool import Color
from math import pi

W_WIDTH = 400
W_HEIGHT = 600
IMG_BASE_URL = './plane/image/'
window = pygame.display.set_mode((W_WIDTH,W_HEIGHT))

# 游戏主页面
def main_page():
    # 1.背景图
    bg_image = pygame.image.load(IMG_BASE_URL+'background.png')
    bg_image = pygame.transform.scale(bg_image,(W_WIDTH,W_HEIGHT))
    window.blit(bg_image,(0,0))
    # 2.显示logo
    logo_image = pygame.image.load(IMG_BASE_URL+'shoot_copyright.png')
    lw,lh = logo_image.get_size()
    nw = W_WIDTH*2/3
    scale = nw/lw
    logo_image = pygame.transform.rotozoom(logo_image,0,scale)
    x = W_WIDTH/2 - nw/2
    window.blit(logo_image,(x,150))
    # 3.显示按钮
    btn_h = 50
    btn_w = 250
    btn_x = 80
    btn_y = 400
    line_width = 1
    font_size = 20
    text = '开始游戏'
    # 1)画弧线1
    rect1 = (btn_x,btn_y,btn_h,btn_h)
    pygame.draw.arc(window,Color.black,rect1,pi/2,pi*3/2,line_width)
    rect2 = (btn_x+btn_w-btn_h,btn_y,btn_h,btn_h)
    pygame.draw.arc(window, Color.black, rect2, pi*3/2, pi/2, line_width)
    # 2)画直线
    line1_x1,line_y1 = btn_x+btn_h/2,btn_y
    line1_x2,line1_y2 = btn_x+btn_w-btn_h/2,btn_y
    pygame.draw.line(window,Color.black,(line1_x1,line_y1),(line1_x2,line1_y2),line_width)

    line2_x1, line2_y1 = btn_x + btn_h / 2, btn_y + btn_h
    line2_x2, line2_y2 = btn_x +btn_w - btn_h/2,btn_y+btn_h
    pygame.draw.line(window, Color.black, (line2_x1, line2_y1), (line2_x2, line2_y2),line_width)

    font = pygame.font.Font('./plane/bb.ttf',font_size)
    text_obj = font.render(text,True,Color.black)
    tw,th = text_obj.get_size()
    t_x, t_y = btn_x+btn_w/2 - tw/2, btn_y+btn_h/2 - th/2
    window.blit(text_obj,(t_x,t_y))


    pygame.display.update()


# 游戏最小系统
def game_sys():
    pygame.init()
    window.fill(Color.white)
    pygame.display.set_caption('飞机大战')
    pygame.display.flip()

    # 1.显示游戏主页面
    main_page()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


if __name__ == '__main__':
    game_sys()