import random as ra
import pygame

pygame.init()

w = 800
h = 800

x1 = 400
x2 = 0
y1 = 0
y2 = 400

col1 = 0, 0, 255
col2 = 255, 255, 0
col3 = ra.randint(1,255),ra.randint(1,255),ra.randint(1,255)

print(type(col1))

sc = pygame.display.set_mode((w,h))

def screen():
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# for i in range(100):
#     # sc.fill((ra.randint(1,255),ra.randint(1,255),ra.randint(1,255)))
#     pygame.draw.rect(sc, col1, (ra.randint(1,255),ra.randint(1,255), 200,300))
#     pygame.draw.rect(sc, col2, (ra.randint(1,255),ra.randint(1,255), 200,100))
#     pygame.draw.circle(sc, col3, (ra.randint(1,255),ra.randint(1,255)), 50 )
#     pygame.display.update()
def draw():
    sc.fill((0,0,0))
    pygame.draw.rect(sc, col1, (x1,y1, 10,40))
    pygame.draw.rect(sc, col2, (x2,y2, 10,40))
    pygame.display.update()



def move1():
    global x2, y1
    if y1 == 799:
        while x2 != 1:
            x2 -= 1
            y1 -= 1
    else:
        x2 += 1
        y1 += 1


while True:
    screen()
    draw()
    move1()

