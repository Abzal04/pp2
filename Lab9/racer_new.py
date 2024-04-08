import pygame,sys
from pygame.locals import *
import random,time,os

pygame.init()
FPS=60
clock=pygame.time.Clock()

WHITE = (255,255,255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

WIDTH=400
HEIGHT=600
SPEED=5
SCORE=0
COINS=0

font=pygame.font.SysFont("Verdana",60)
font_small=pygame.font.SysFont("Verdana",20)
game_over=font.render("Game Over",True,BLACK)

SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
SCREEN.fill(WHITE)
pygame.display.set_caption("Racer")

background=pygame.image.load("/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/image/AnimatedStreet.png")

fon_music= pygame.mixer.Sound('/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/music/background.wav')
crash_sound=pygame.mixer.Sound('/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/music/crash.wav')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/image/Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(0,WIDTH-40),0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if(self.rect.top>600):
            SCORE+=1
            self.rect.top=0
            self.rect.center=(random.randint(0,WIDTH-40),0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/image/Enemy.png')
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)
    def move(self):
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed[K_LEFT]:
                self.rect.move_ip(-5,0)
        if pressed[K_RIGHT]:
                self.rect.move_ip(5,0)
            
## COINS
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image=pygame.image.load("/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/image/coins.png")
        self.image=pygame.transform.scale(image,(40,40))
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(0,WIDTH-20),random.randint(30,HEIGHT-20))
    def move(self):
        pass
    def new_coin(self):
        global COINS

        #Randomly generating coins with different weights on the road
        COINS +=random.randint(0,20)

        coins.remove(self)
        self.rect.center=(random.randint(0,WIDTH-20),random.randint(30,HEIGHT-20))
        coins.add(self)
        
P1=Player()
E1=Enemy()
C1=Coins()

enemies=pygame.sprite.Group()
enemies.add(E1)
coins=pygame.sprite.Group()
coins.add(C1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

INC_SPEED=pygame.USEREVENT+1
if SCORE>=30:
    pygame.time.set_timer(INC_SPEED,1000)

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==INC_SPEED:
                    SPEED+=50
    SCREEN.blit(background,(0,0))
    scores=font_small.render(str(SCORE),True,BLACK)
    SCREEN.blit(scores,(10,10))

    ###Coin_scores
    coin_scores=font_small.render(str(COINS),True,BLACK)
    SCREEN.blit(coin_scores,(WIDTH-25,10))
    
    fon_music.play(-1)

    for entity in all_sprites:
        SCREEN.blit(entity.image,entity.rect)
        entity.move()
    
    #If player and coin collide
    if pygame.sprite.spritecollide(P1,coins,dokill=False):
         C1.new_coin()
        
        

    if pygame.sprite.spritecollideany(P1,enemies):
        fon_music.stop()
        crash_sound.play()
        time.sleep(0.5)

        SCREEN.fill(RED)
        SCREEN.blit(game_over,(30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    pygame.display.update()
    clock.tick(FPS)