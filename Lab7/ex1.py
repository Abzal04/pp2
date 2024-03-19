import pygame
import time
import datetime
import math

pygame.init()
WIDTH=1000
HEIGHT=1000
middle = WIDTH//2 , HEIGHT//2
RADIUS = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Clock")

sec = pygame.image.load("left.png").convert_alpha()
minute = pygame.image.load("right.png").convert_alpha()
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectmin.center = rectmin.center = middle

background = pygame.image.load("mickey.jpg")
done =True

angle1 = 0
angle2 = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    this_time = datetime.datetime.now()
    minuteTime = this_time.minute
    secondTime = this_time.second

    angle1 = -minuteTime*6 
    leg1 = pygame.transform.rotate(minute, angle1)
    rect1 = leg1.get_rect()
    rect1.center = rectmin.center

    angle2 = -secondTime*6 
    leg2 = pygame.transform.rotate(sec, angle2)
    rect2 = leg2.get_rect()
    rect2.center = rectsec.center

    screen.blit(background, (0, 0))
    screen.blit(leg1, rect1)
    screen.blit(leg2, rect2)

    pygame.display.flip()
    clock.tick(60)