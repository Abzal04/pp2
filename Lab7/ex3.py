import pygame
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Red_ball")
done=False
x=220
y=220
radius=25
clock=pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y = max(radius, y - 20)
    if pressed[pygame.K_DOWN]: y = min(screen.get_height() - radius, y + 20)
    if pressed[pygame.K_LEFT]: x = max(radius, x - 20)
    if pressed[pygame.K_RIGHT]: x = min(screen.get_width() - radius, x + 20)
    screen.fill((255,255,255))

    ball=pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    pygame.display.flip()
    clock.tick(60)
