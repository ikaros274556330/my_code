"""__author:吴佩隆__"""
import pygame
from random import *

pygame.init()
window = pygame.display.set_mode((600,400))
window.fill((0,0,0))
pygame.display.set_caption('坦克大战')

font1 = pygame.font.Font('img/bb.ttf',60)
title = font1.render('坦克大战 1990',True,(255,0,0))

player1 = font1.render('1 PLAYER',True,(255,255,255))
player1_new = pygame.transform.rotozoom(player1,0,0.4)

player2 = font1.render('2 PLAYER',True,(255,255,255))
player2_new = pygame.transform.rotozoom(player2,0,0.4)

exit_game = font1.render('EXIT GAME',True,(255,255,255))
exit_game_new = pygame.transform.rotozoom(exit_game,0,0.4)


image1 = pygame.image.load('tanksucai\90坦克大战全套素材\pic\Icon-ldpi.png')


window.blit(title,(100,0))
window.blit(player1_new,(220,150))
window.blit(player2_new,(220,180))
window.blit(exit_game_new,(220,300))
window.blit(image1,(180,147))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
