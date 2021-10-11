import random
import pygame
from pygame.sprite import spritecollide

#变量常量定义
SCREEN_RECT = pygame.Rect(0,0,480,852) #矩形对象
FRAME = 60 #帧率
CREAT_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
ENEMY_DOWN_EVENT = pygame.USEREVENT + 2
#HERO_DOWN_EVENT = pygame.USEREVENT + 3
a = 0
class GameSprite(pygame.sprite.Sprite):
    
    
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y+=self.speed

class Background(GameSprite):
    
    def __init__(self,replace=False):
        super().__init__("C:/Users/A/Downloads/chengao1006/plane/images/background.png")
        if replace:
            self.rect.y = -self.rect.height
    
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):


    def __init__(self):
        super().__init__("C:/Users/A/Downloads/chengao1006/plane/images/enemy1.png")
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        self.rect.x = random.randint(0,423)
        
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.die_rect = self.rect

    def enemy_die(self):

        self.down1_image = pygame.image.load("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down1.png")
        self.down2_image = pygame.image.load("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down2.png")
        self.down3_image = pygame.image.load("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down3.png")
        self.down4_image = pygame.image.load("C:/Users/A/Downloads/chengao1006/plane/images/enemy1_down4.png")
        self.list = [self.down1_image,self.down1_image,self.down1_image,self.down1_image]

class Hero(GameSprite):

    def __init__(self):
        super().__init__("C:/Users/A/Downloads/chengao1006/plane/images/hero1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-20
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.yspeed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
        if self.rect.y < 0:
            self.rect.y = 0

    def fire(self):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y - 10
        bullet.rect.centerx = self.rect.centerx
        self.bullet_group.add(bullet)

    def hero_die(self):
        pass

class Bullet(GameSprite):

    
    def __init__(self):
        super().__init__("C:/Users/A/Downloads/chengao1006/plane/images/bullet1.png",-5)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass

