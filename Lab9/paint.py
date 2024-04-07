import pygame
def main():
    pygame.init()
    W=800
    H=600
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    WHITE= (255,255,255)
    RADIUS= 50
    while True: 
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(30, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]        
        screen.fill((0, 0, 0))
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
       
        pygame.draw.rect(screen,WHITE,(20,50,150,100),2)
        pygame.draw.circle(screen,WHITE,(250,100),RADIUS,2)

        #Square
        pygame.draw.rect(screen,WHITE,(300,200,100,100),2)
        #Right triangle
        pygame.draw.lines(screen,WHITE,True,[[400,50],[400,150],[500,150]],2)
        #Rhombus
        pygame.draw.polygon(screen, WHITE,[[80, 200], [20, 300], [80, 400], [140, 300]], 2)

        #Right Equilateral Triangle
        pygame.draw.lines(screen,WHITE,True,[[W-100,200],[W-200,200],[W-150,120]],2)

        pygame.draw.circle(screen,(255,0,0),(100,500),20,2)
        pygame.draw.circle(screen,(0,255,0),(300,500),20,2)
        pygame.draw.circle(screen,(0,0,255),(500,500),20,2)
        pygame.draw.circle(screen,(255,255,255),(700,500),30,2)
        selected_color=click()
        if selected_color:
            mode=selected_color
        
        pygame.display.flip()
        clock.tick(60)

def click():
    pos=pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()==(1,0,0):
        if pygame.Rect(100,475,50,50).collidepoint(pos):
            return 'red'
        elif pygame.Rect(300,475,50,50).collidepoint(pos):
            return 'green'
        elif pygame.Rect(500,475,50,50).collidepoint(pos):
            return 'blue'
        elif pygame.Rect(700,475,50,50).collidepoint(pos):
            return (0,0,0)
        
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    color=(0,0,0)
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()

