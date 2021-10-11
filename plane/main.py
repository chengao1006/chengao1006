#-*-coding：UTF-8 -*-
import pygame
import time
from plane_sprites import *



pygame.init()

screen = pygame.display.set_mode((480,852))             #窗口建立、时钟建立
clock = pygame.time.Clock()

bg = pygame.image.load('./images/background.png')       #图片加载
hero1 = pygame.image.load('./images/hero1.png')
gameover = pygame.image.load('./images/game_over.png')

screen.blit(bg,(0,0))                                   #初始界面绘制
screen.blit(hero1,(188,720))

hero1_rect = pygame.Rect(188,720,102,126)               #矩形位置定义
gameover_rect = pygame.Rect(100,300,300,41)


enemy1 = GameSprite('./images/enemy1.png')#敌机
enemy_group = pygame.sprite.Group(enemy1)


while True:                                             #游戏开始循环
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    
    hero1_rect.y -= 1
    screen.blit(bg,(0,0))
    screen.blit(hero1,hero1_rect)
    
   
    enemy_group.update()
    enemy_group.draw(screen)
    
    pygame.display.update()





pygame.quit()