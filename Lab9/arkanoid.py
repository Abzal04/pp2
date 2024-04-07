import pygame 
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)
is_paused=False

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#unbreakable bricks
brick_list=[pygame.Rect(10+120*i,60,100,50) for i in range(10)]
RED=(255,0,0)

#Bonus Bricks
bonus_bricks = [pygame.Rect(160, 50 + 70 * 2, 100, 50), pygame.Rect(850, 50 + 70 * 1, 100, 50)]

#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('/Users/abzalkabdoldaev/Desktop/PP2 Labs/Lab9/music/catch (1).mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (3,6)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(3,6)] 

#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#Increasing speed within time
INC_SPEED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED,1000)
INC_PADDLE_WIDTH = pygame.USEREVENT + 2
pygame.time.set_timer(INC_PADDLE_WIDTH, 1000)

#Pause
pause_font=pygame.font.SysFont('comicsansms',80)
pause_text=pause_font.render('Paused',True,(255,255,255))
pauseRect=pause_text.get_rect()
pauseRect.center=(W//2,H//2-300)
is_paused=False
dark_mode=pygame.Surface((W,H),pygame.SRCALPHA)
dark_mode.fill((0,0,0,128))

#Settings/ Change
settings_font=pygame.font.SysFont("comicsansms",80)
settings_text=settings_font.render("You can change:",True,(255,255,255))
settings_rect=settings_text.get_rect()
settings_rect.center=(W//2,H//2-200)
turn_on=False

#Size of a ball
ballSize_font=pygame.font.SysFont("comicsansms",60)
ballSize_text=ballSize_font.render("Ball Size",True,(255,255,255))
ballSize_rect=ballSize_text.get_rect()
ballSize_rect.center=(W//2-300,H//2)

plus_sign_font=pygame.font.SysFont("comicsansms",30)
plus_sign_text=plus_sign_font.render("+",True,(255,255,255))
plus_sign_rect=plus_sign_text.get_rect()
plus_sign_rect.center=(W//2-200,H//2+300)

minus_sign_font=pygame.font.SysFont("comicsansms",30)
minus_sign_text=minus_sign_font.render("-",True,(255,255,255))
minus_sign_rect=minus_sign_text.get_rect()
minus_sign_rect.center=(W//2-400,H//2+300)

num=pygame.font.SysFont("comicsansms",40)
num_text=num.render(str(ballRadius),True,(255,255,255))
num_rect=num_text.get_rect()
num_rect.center=(W//2-300,H//2+300)


#Speed of a ball
sball_font=pygame.font.SysFont("comicsansms",60)
sball_text=sball_font.render("Speed of a ball",True,(255,255,255))
sball_rect=sball_text.get_rect()
sball_rect.center=(W//2-300,H//2+200)

pluss_sign_font=pygame.font.SysFont("comicsansms",30)
pluss_sign_text=pluss_sign_font.render("+",True,(255,255,255))
pluss_sign_rect=pluss_sign_text.get_rect()

minuss_sign_font=pygame.font.SysFont("comicsansms",30)
minuss_sign_text=minuss_sign_font.render("-",True,(255,255,255))
minuss_sign_rect=minuss_sign_text.get_rect()

nums=pygame.font.SysFont("comicsansms",40)
nums_text=nums.render(str(ballSpeed),True,(255,255,255))
nums_rect=nums_text.get_rect()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type==INC_SPEED:
            ballSpeed+=0.5
        elif event.type==INC_PADDLE_WIDTH:
            paddleW-=0.5
            paddle = pygame.Rect(paddle.x, paddle.y, paddleW, paddleH)
        #Pause
        elif event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_p:
                is_paused=not is_paused



        
    screen.fill(bg)
    if not is_paused:
        [pygame.draw.rect(screen, color_list[color], block)
         for color, block in enumerate (block_list)] #drawing blocks
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
        # print(next(enumerate (block_list)))

        # Drawing unbreakable bricks
        for brick in brick_list:
            pygame.draw.rect(screen, RED, brick)

        #Draawing bonus bricks
        for brick in bonus_bricks:
            pygame.draw.rect(screen, (255, 215, 0), brick)
    
        #Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        #Collision left 
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        #Collision top
        if ball.centery < ballRadius + 50: 
            dy = -dy
        #Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dy= - dy

        #Collision blocks
        hitIndex = ball.collidelist(block_list)

        #Collision of unbreakable bricks
        for brick in brick_list:
            if ball.colliderect(brick):
                dx, dy = detect_collision(dx, dy, ball, brick)

        #Collision of bonus brick
        for bonus in bonus_bricks:
            if ball.colliderect(bonus):
                dx, dy = detect_collision(dx, dy, ball, bonus)
                game_score += 100
                bonus_bricks.remove(bonus)


        if hitIndex != -1:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            game_score += 1
            collision_sound.play()
        
        #Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)
    
        #Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif not len(block_list):
            screen.fill((255,255, 255))
            screen.blit(wintext, wintextRect)

        #Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
    
    else: #SHow it when is_paused:
        screen.blit(dark_mode,(0,0))
        screen.blit(pause_text,pauseRect)
        screen.blit(ballSize_text,ballSize_rect)
        screen.blit(settings_text,settings_rect)

    pygame.display.flip()
    clock.tick(FPS)