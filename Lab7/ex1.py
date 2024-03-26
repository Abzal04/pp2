import pygame
import datetime


pygame.init()
WIDTH=800
HEIGHT=800
middle = WIDTH/2 , HEIGHT/2
RADIUS = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Clock")

sec = pygame.image.load("/Users/abzalkabdoldaev/Desktop/left.png")
sec.set_colorkey((255,255,255))
minute = pygame.image.load("/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab7/right.png")
minute.set_colorkey((255,255,255))
rectsec = sec.get_rect()
rectmin = minute.get_rect()
rectmin.center = middle
rectsec.center=middle

background = pygame.image.load("/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab7/mickey.png")
done =False

angle1 = 0
angle2 = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    this_time = datetime.datetime.now()
    minuteTime = this_time.minute
    secondTime = this_time.second

    angle1 = -minuteTime*6 
    right = pygame.transform.rotate(minute, angle1)
    rect1 = right.get_rect()
    rect1.center = rectmin.center

    angle2 = -secondTime*6 
    left = pygame.transform.rotate(sec, angle2)
    rect2 = left.get_rect()
    rect2.center = rectsec.center

    screen.blit(background, (0, 0))
    screen.blit(right, rect1)
    screen.blit(left, rect2)

    pygame.display.flip()
    clock.tick(60)