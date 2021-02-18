import pygame as pg 
import random as rnd
pg.init()

scr = pg.display.set_mode((500, 500))

col1 = rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)

def screen():
     for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
def draw():
    scr.fill((rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)))
    pg.draw.line(scr, (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)), (0,0), (500,500), 100)
    pg.draw.line(scr, (rnd.randint(0,255),rnd.randint(0,255),rnd.randint(0,255)), (500,0), (0,500), 100)
    pg.display.update()

while True:
    screen()
    draw()
