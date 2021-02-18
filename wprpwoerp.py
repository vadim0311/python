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
w1 = 100
x = 1

# if x <= 100 and i == 1:
#         x += 1
#     if x >= 100:
#         i = 0
#         x -= 1

while True:
    screen()
    scr1.fill((255, 255, 255))
    pg.draw.circle(scr1, col, (x1, y1), w1, w1,)
    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN]:
        y1 += 3
    if keys[pg.K_UP]:
        y1 -= 3
    if keys[pg.K_RIGHT]:
        x1 += 3
    if keys[pg.K_LEFT]:
        x1 -= 3
    if keys[pg.K_w]:
        w1 += 3
    if keys[pg.K_s]:
        w1 -= 3
    pg.display.update()
    
