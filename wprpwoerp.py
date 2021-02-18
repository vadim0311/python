import pygame as pg
import random as rnd 
pg.init()
scr1 = pg.display.set_mode((600, 600))
def screen():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
col = (0, 0, 0)
i = 1
x1 = 300
y1 = 300
w1 = 10
x = 1


def draw():
    scr1.fill((0, 255, 255))
    pg.draw.rect(scr1, (255, 255, 0), (100, 100, 400, 400))
    pg.draw.rect(scr1, (255, 0, 0), (200, 200, 200, 200))
    pg.draw.circle(scr1, col, (x1, y1), w1, w1,)
    pg.display.update() 

    

while True:
    screen()
    draw()
    keys = pg.key.get_pressed()
    if y1 > 500 or y1 < 100 or x1 < 100 or x1 > 500:
        col = (255, 0, 255)
        w1 = 10
        if keys[pg.K_DOWN]:
            y1 += 5
        if keys[pg.K_UP]:
            y1 -= 5 
        if keys[pg.K_RIGHT]:
            x1 += 5
        if keys[pg.K_LEFT]:
            x1 -= 5
    elif y1 > 400 or y1 < 200 or x1 < 200 or x1 > 400:
        w1 = 20
        col = (255, 0, 0)
        if keys[pg.K_DOWN]:
            y1 += 3
        if keys[pg.K_UP]:
            y1 -= 3 
        if keys[pg.K_RIGHT]:
            x1 += 3
        if keys[pg.K_LEFT]:
            x1 -= 3
    else:
        w1 = 30
        col = (0, 0, 0)
        if keys[pg.K_DOWN]:
            y1 += 1
        if keys[pg.K_UP]:
            y1 -= 1 
        if keys[pg.K_RIGHT]:
            x1 += 1
        if keys[pg.K_LEFT]:
            x1 -= 1
    if x1 >= 600 + w1:
        x1 = 0
    if x1 <= 0:
        x1 = 600
    if y1 >= 600 + w1:
        y1 == 0
    if y1 <= 0:
        y1 = 600 
    if not(keys[pg.K_UP] or keys[pg.K_LEFT] or keys[pg.K_RIGHT] or keys[pg.K_DOWN]):
        if y1 > 300:
            y1 -= 3
        if x1 > 300:
            x1 -= 3
        if y1 < 300:
            y1 += 3
        if x1 < 300:
            x1 += 3
    
    
