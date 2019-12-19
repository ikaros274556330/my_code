"""__author__=余婷"""
import pygame
pygame.init()
from tool import Color, Button
from math import pi
from plane import Plane,W_WIDTH,W_HEIGHT,Enemy


IMG_BASE_URL = './plane/image/'
window = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
page = 1  #1->游戏首页  2->游戏页面  3->游戏暂停页面
hero = Plane(150,450,IMG_BASE_URL+'hero1.png')
font = pygame.font.Font('./plane/bb.ttf',20)

sound_bullet = pygame.mixer.Sound('./plane/sound/bullet.wav')

def game_start():
    global page
    page = 2
    # print('游戏开始了')
    # 1.显示背景
    bg_image = pygame.image.load(IMG_BASE_URL + 'background.png')
    bg_image = pygame.transform.scale(bg_image, (W_WIDTH, W_HEIGHT))
    window.blit(bg_image, (0, 0))


    # 2.显示飞机
    # hero.show(window)

    # 3.显示分数
    text_obj = font.render('分数: %d' % hero.score,True,Color.black)
    window.blit(text_obj,(10,10))




    # pygame.display.update()

def btn_action():
    print('游戏退出')
    exit()

# 游戏主页面
def main_page():
    # 1.背景图
    bg_image = pygame.image.load(IMG_BASE_URL+'background.png')
    bg_image = pygame.transform.scale(bg_image, (W_WIDTH, W_HEIGHT))
    window.blit(bg_image, (0, 0))
    # 2.显示logo
    logo_image = pygame.image.load(IMG_BASE_URL+'shoot_copyright.png')
    lw, lh = logo_image.get_size()
    nw = W_WIDTH * 2 / 3
    scale = nw / lw
    logo_image = pygame.transform.rotozoom(logo_image, 0, scale)
    x = W_WIDTH/2 - nw/2
    window.blit(logo_image, (x, 150))

    # 3.显示按钮
    global start_btn
    start_btn = Button(80, 400, 250, 50, '开始游戏')
    start_btn.click_action = game_start
    start_btn.show(window)

    global btn2
    btn2 = Button(80, 500, 250, 50, '退出游戏')
    btn2.click_action = btn_action
    btn2.show(window)

    # btn3 = Button(0, 0, 100, 30, '确定', font_size=20, color=(255, 0, 0))
    # btn3.show(window)


    pygame.display.update()

# 游戏最小系统
def game_sys():
    window.fill(Color.white)
    pygame.display.set_caption('飞机大战')
    pygame.display.flip()

    # 1.显示游戏主页面
    main_page()

    num = 1
    while True:
        if page == 2:
            game_start()
            hero.show(window)

            if num % 10 == 0:
                hero.shoot()
            num += 1

            if num % 20 ==0:
                Enemy.appear()

            if num % 1 ==0:
                Enemy.move_enemy(window)

            hero.show_bullet(window)


            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 首页的点击事件
                if page == 1:
                    hero.move(window, event.pos)
                    start_btn.click(event.pos)
                    btn2.click(event.pos)

            elif event.type == pygame.MOUSEMOTION:
                if page == 2:
                    hero.move(window, event.pos)

if __name__ == '__main__':
    game_sys()



