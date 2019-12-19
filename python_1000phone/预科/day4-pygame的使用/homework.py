"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
w,h = 400,600
window = pygame.display.set_mode((w,h))
window.fill((255,255,255))
pygame.display.set_caption('2048')

font = pygame.font.Font('./sucai/bb.ttf', 30)

class Block:
    def __init__(self,window,where,empyt):
        self.window = window
        self.where = where
        self.empty = empyt
        self.now = choice(self.where)
        self.lag = 75
        self.x,self.y = self.now[0],self.now[1]
        self.num = choice([2,4])

    def show(self):
        pygame.draw.rect(self.window, (230, 230,0),self.now, 0)
        block_num = font.render(str(self.num), True, (255, 255, 255))
        window.blit(block_num, (self.x+15, self.y))

    def move_up(self):
        time_speed = 1
        if self.y > 300:
            while self.lag > 0:
                if time_speed % 10000 == 0:
                    pygame.draw.rect(self.window, (200, 200, 200),(self.x,self.y,70,70), 0)
                    block_num = font.render(str(self.num), True, (255, 255, 255))
                    window.blit(block_num, (self.x + 15, self.y))
                    self.y -= 1
                    pygame.draw.rect(self.window, (230, 230, 0),(self.x,self.y,70,70) , 0)
                    block_num = font.render(str(self.num), True, (255, 255, 255))
                    window.blit(block_num, (self.x + 15, self.y))
                    self.lag -=1
                    pygame.display.update()
                time_speed +=1
            self.lag = 75
            self.num *= 2








where_list = [(55,285,70,70),(130,285,70,70),(205,285,70,70),(280,285,70,70),
              (55,360,70,70),(130,360,70,70),(205,360,70,70),(280,360,70,70),
              (55,435,70,70),(130,435,70,70),(205,435,70,70),(280,435,70,70),
              (55,510,70,70),(130,510,70,70),(205,510,70,70),(280,510,70,70)]

empty_list = []
f = 0
pygame.draw.rect(window,(200,200,200),(50,280,300,300),0)
pygame.draw.rect(window,(200,200,0),(20,20,140,140),0)
text_2048 = font.render('2048',True,(255,255,255))
window.blit(text_2048,(60,70))
pygame.draw.rect(window,(200,200,200),(180,20,100,60),0)
text_hit = font.render(str(f),True,(255,255,255))
window.blit(text_hit,(220,30))
pygame.draw.rect(window,(200,200,200),(290,20,100,60),0)
pygame.draw.rect(window,(200,200,0),(180,120,100,40),0)
text_exit = font.render('退出',True,(255,255,255))
window.blit(text_exit,(200,120))
pygame.draw.rect(window,(200,200,0),(290,120,100,40),0)
text_newgame = font.render('新游戏',True,(255,255,255))
window.blit(text_newgame,(290,120))

all_block = []
block_1 = Block(window,where_list,empty_list)
all_block.append(block_1)

for i in all_block:
    i.show()
    pygame.display.update()



pygame.display.flip()
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if 180<x<280 and 120<y<160:
                exit()
            elif 290 < x < 390 and 120 < y < 160:
                pygame.draw.rect(window, (200, 200, 200), (180, 20, 100, 60), 0)
                f = 0
                text_hit = font.render(str(f), True, (255, 255, 255))
                window.blit(text_hit, (220, 30))
                pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if 180 < x < 280 and 120 < y < 160:
                pygame.draw.rect(window, (255,255, 0), (180, 120, 100, 40), 0)
                text_new = font.render('退出', True, (255,255,255))
                window.blit(text_exit, (200, 120))
                pygame.display.update()
            elif 290<x<390 and 120<y<160:
                pygame.draw.rect(window, (255, 255, 0), (290, 120, 100, 40), 0)
                text_newgame = font.render('新游戏', True, (255, 255, 255))
                window.blit(text_newgame, (290, 120))
                pygame.display.update()
            else:
                pygame.draw.rect(window, (200, 200, 0), (180, 120, 100, 40), 0)
                pygame.draw.rect(window, (200, 200, 0), (290, 120, 100, 40), 0)
                text_new = font.render('退出', True, (255,255,255))
                text_newgame = font.render('新游戏', True, (255, 255, 255))
                window.blit(text_exit, (200, 120))
                window.blit(text_newgame, (290, 120))
                pygame.display.update()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.draw.rect(window, (200, 200, 200), (180, 20, 100, 60), 0)
                f += 1
                for i in all_block:
                    i.move_up()
                new_block = Block(window,where_list,empty_list)
                new_block.show()
                text_hit = font.render(str(f), True, (255, 255, 255))
                window.blit(text_hit, (220, 30))
                pygame.display.update()
                all_block.append(new_block)

