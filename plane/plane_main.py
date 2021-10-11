#-*-coding：UTF-8 -*-

import pygame
import time
from plane_sprites import *


class PlaneGame():
    
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)         #游戏窗口
        self.clock = pygame.time.Clock()
        self.create()
        pygame.time.set_timer(CREAT_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,200)
        
     
    def create(self):    
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)
        
        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.pause = GameSprite("C:/Users/A/Downloads/chengao1006/plane/images/game_pause_nor.png",0)
        self.pause.rect.x = SCREEN_RECT.width - self.pause.rect.width - 20
        self.pause.rect.y += 20
        self.pause_group = pygame.sprite.Group(self.pause)
        
        self.resume = GameSprite("C:/Users/A/Downloads/chengao1006/plane/images/game_resume_nor.png",0)
        self.resume.rect.x = SCREEN_RECT.width - self.resume.rect.width - 20
        self.resume.rect.y += 20
        self.resume_group = pygame.sprite.Group(self.resume)

        self.edown1 = GameSprite("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down1.png",0)
        self.edown2 = GameSprite("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down2.png",0)
        self.edown3 = GameSprite("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down3.png",0)
        self.edown4 = GameSprite("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down4.png",0)
        self.edown = False
    
    def event_handler(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.gameover()
            elif event.type == CREAT_ENEMY_EVENT:
                self.enemy = Enemy()
                self.enemy_group.add(self.enemy)
            elif event.type == HERO_FIRE_EVENT and keys[pygame.K_j]:
                self.hero.fire()


        if keys[pygame.K_d]:
            self.hero.speed = 2
                        
        elif keys[pygame.K_a]:
            self.hero.speed = -2
            
        elif keys[pygame.K_w]:
            self.hero.yspeed = -2
            
        elif keys[pygame.K_s]:
            self.hero.yspeed = 2
                    
        else:
            self.hero.speed = 0
            self.hero.yspeed = 0
    
    def collide_check(self):
        enemy_die_flag = pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        hero_die_flag = pygame.sprite.groupcollide(self.hero_group,self.enemy_group,True,True)
        if len(hero_die_flag)>0:
            pass
        if len(enemy_die_flag)>0:
            self.edown1.rect = self.enemy.die_rect
            self.edown = pygame.sprite.Group(self.edown1)
            
            


    def update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)        
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)  
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)
        self.pause_group.draw(self.screen)
        
        if self.edown:
            self.edown.draw(self.screen)
    
    def start(self):
        C = True
        while C:
            self.clock.tick(FRAME)
            self.event_handler()
            self.collide_check()
            self.update_sprites()
            pygame.display.update()
            

    @staticmethod
    def gameover():
        pygame.quit()
        exit()



if __name__ == '__main__':

    pygame.init()
    
    game = PlaneGame()
    
    game.start()