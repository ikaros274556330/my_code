"""__author:吴佩隆__"""
import pygame
from random import randint

W_WIDTH = 400
W_HEIGHT = 600

class Enemy:
    enemy_1 = pygame.image.load('./plane/image/enemy1_5.png')
    enemy_2 = pygame.image.load('./plane/image/enemy2.png')
    enemy_3 = pygame.image.load('./plane/image/enemy3_n1.png')

    all_enemy = []
    def __init__(self,x,y,type=1):
        self.x = x
        self.y = y
        if type == 1:
            self.image = Enemy.enemy_1
            self.life = 2
            self.speed = 5
            self.score = 50
        elif type == 2:
            self.image = Enemy.enemy_2
            self.life = 4
            self.speed = 3
            self.score = 100
        elif type == 3:
            self.image = Enemy.enemy_3
            self.life = 8
            self.speed = 1
            self.score = 500

        self.width,self.height = self.image.get_size()

    @classmethod
    def appear(cls):
        # 1.控制敌机类型产生几率
        type = randint(0,100)
        if type <= 80:
            enemy = cls(0,0,1)
        elif 80<type<97:
            enemy = cls(0,0,2)
        else:
            enemy = cls(0,0,3)

        # 2.随机出现的位置
        x = randint(0,W_WIDTH - enemy.width)
        y = -enemy.height
        enemy.x = x
        enemy.y = y

        cls.all_enemy.append(enemy)

    # 显示和移动敌机
    @classmethod
    def move_enemy(cls,surface):
        for enemy in cls.all_enemy[:]:
            # 显示
            surface.blit(enemy.image,(enemy.x,enemy.y))
            # 移动
            enemy.y += enemy.speed
            # 边界检测
            if enemy.y >= W_HEIGHT:
                cls.all_enemy.remove(enemy)


class Bullet:
    type_1 = pygame.image.load('./plane/image/bullet1.png')
    type_2 = pygame.image.load('./plane/image/bullet2.png')
    def __init__(self,x,y,type=1):
        self.x = x
        self.y = y
        if type == 1:
            self.image = Bullet.type_1
            self.atk = 1
        elif type == 2:
            self.image = Bullet.type_2
            self.atk = 3
        self.width,self.height = self.image.get_size()
        self.speed = 7

    def show(self,surface):
        surface.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= self.speed






class Plane:
    def __init__(self,x,y,image):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.width,self.height = self.image.get_size()
        self.score = 0

        self.all_bullet = []

    def show(self,surface):
        surface.blit(self.image,(self.x,self.y))

    def move(self,surface,pos):
        mx,my = pos
        self.x,self.y = mx - int(self.width/2),my-int(self.height/2)

    def shoot(self):
        bullet = Bullet(0,0)
        bx = self.x + self.width/2 - bullet.width/2
        by = self.y - bullet.height - 5
        bullet.x = bx
        bullet.y = by
        self.all_bullet.append(bullet)

        # bullet.show(surface)

    def crash(self,bullet):
        for enemy in Enemy.all_enemy:
            if enemy.x - bullet.width <= bullet.x <= enemy.x +\
                    enemy.width and bullet.y <enemy.y + enemy.height:
                self.all_bullet.remove(bullet)
                enemy.life -= bullet.atk
                if enemy.life <= 0:
                    Enemy.all_enemy.remove(enemy)
                    self.score += enemy.score
                break




    def show_bullet(self,surface):
        for bullet in self.all_bullet[:]:
            bullet.show(surface)
            bullet.move()
            # 删除子弹
            if bullet.y <= -bullet.height - 10:
                self.all_bullet.remove(bullet)
            else:
                # 检测子弹碰撞
                self.crash(bullet)


    # def move_bullet(self):
    #     for bullet in self.all_bullet:
    #         bullet.move()