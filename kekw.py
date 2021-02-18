import pygame as pg
import random as rnd

pg.init()
sc = pg.display.set_mode((600,600))

def screen():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

col1 = rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)
col2 = rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)
col3 = rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)

x = rnd.randint(100,300)
y = rnd.randint(100,300)
xw = rnd.randint(10,300)
yw = rnd.randint(10,300)

x2 = rnd.randint(100,300)
y2 = rnd.randint(100,300)
r = rnd.randint(0,100)


def move2():
    global x2, y2, r
    x2 += 1
    y2 += 1
    if x2 == 600:
        x2 = -r
    

while True:
    screen()
    sc.fill((col1))
    pg.draw.circle(sc, col3, (x2,y2), r)
    pg.draw.rect(sc, col2, (x,y,xw,yw))
    pg.display.update()
    move2()
    