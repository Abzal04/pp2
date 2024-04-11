import pygame as pg
from pygame.locals import *

pg.init()
screen=pg.display.set_mode((1200,800))
screen2=pg.Surface(screen.get_size())
menu=pg.Surface((80,800))
menu.fill((255,255,255))
pg.display.set_caption("Paint")
WHITE=(255,255,255)
BLACK=(0,0,0)
FPS=60
clock=pg.time.Clock()
run=True

#Rectangle
pg.draw.rect(menu,BLACK,(10, 10,60, 100),3)
#Circle
pg.draw.circle(menu,BLACK,(40, 160),radius=30,width=3)
#Eraser
pg.draw.rect(menu,BLACK,(15, 210,30, 50))
pg.draw.rect(menu,(255,0,0),(45,210,20,50))
#Color selection
pg.draw.rect(menu,(255,0,0),(15, 270,50, 50))
pg.draw.rect(menu,(0,255,0),(15, 330,50, 50))
pg.draw.rect(menu,(0,0,255),(15, 390,50, 50))
#Equilateral Triangle
pg.draw.lines(menu,BLACK,True,[(15, 500),(40, 450),(65,500)],3)
#Right Triangle
pg.draw.lines(menu,BLACK,True,[(15, 520),(15, 580),(70, 580)],3)
#Rhombus
pg.draw.polygon(menu,BLACK,[(40, 600),(10, 640),(40, 680),(70, 640)],3)
#Square
pg.draw.rect(menu,BLACK,(15,700,50,50),width=3)


def rectangle(screen):
    pos_x,pos_y=x,y
    width=x2-x
    height=y2-y
    if x2<x:
        pos_x=x2
        width=x-x2
    if y2<y:
        pos_y=y2
        height=y-y2
    pg.draw.rect(screen,colors[current],(pos_x,pos_y,width,height),3)

def circle(screen):
    pg.draw.circle(screen,colors[current],(x,y),radius=(((x2-x)**2+(y2-y)**2)**0.5),width=3)

def square(screen):
    pos_x=x2
    pos_y=y2
    width=x2-x
    height=y2-y
    if x2<x:
        pos_x=x
        width=x-x2
    if y2<y:
        pos_y=y
        height=y-y2
    pg.draw.rect(screen,colors[current],(pos_x,pos_y,width,height),3)

def right_triangle(screen):
    pg.draw.lines(screen, colors[current],True,[(x2,y2),(x2+60,y2),(x2,y2-60)],3)

def equilateral_triangle(screen):
    pg.draw.lines(screen,colors[current],True,[(x2,y2),(x2+60,y2),(x2+30,y2-60)],3)

def rhombus(screen):
    pg.draw.polygon(screen,colors[current],[(x2,y2),(x2+25,y2+50),(x2+50,y2),(x2+25,y2-50)],3)

def eraser(screen):
    pg.draw.rect(screen2,BLACK,(x2,y2,50,50))

colors={"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
current="red"
objects={"rect":rectangle,"circle":circle,"eraser":eraser,"square": square,
        "eq_tr":equilateral_triangle,"right_tr":right_triangle,"rhombus":rhombus}
current_object="rect"
x,y,x2,y2=0,0,0,0

while run:
    for event in pg.event.get():
        if event.type==QUIT:
            run=False
        if event.type==MOUSEBUTTONDOWN:
            x,y=pg.mouse.get_pos()
            if 0<=x<=80 and 0<=y<=800:
                if y<100:
                    current_object="rect"
                elif y<190:
                    current_object="circle"
                elif y<260:
                    current_object="eraser"
                elif y<320:
                    current="red"
                elif y<380:
                    current="green"
                elif y<440:
                    current="blue"
                elif y<500:
                    current_object="eq_tr"
                elif y<580:
                    current_object="right_tr"
                elif y<640:
                    current_object="rhombus"
                elif y<750:
                    current_object="square"
        if pg.mouse.get_pressed() ==(1,0,0):
            x2,y2=pg.mouse.get_pos()
            screen.blit(screen2, (0, 0))
            objects[current_object](screen)
            screen.blit(menu,(0,0))
            pg.display.flip()
        if event.type==MOUSEBUTTONUP:
            objects[current_object](screen2)
    screen.blit(menu,(0,0))
    pg.display.flip()
    clock.tick(60)
