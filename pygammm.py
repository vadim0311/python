import pygame
import random as rnd
pygame.init()
sc = pygame.display.set_mode((1000,1000))

col1 = 255, 0, 0
col2 = 255, 255, 0
col2 = 255, 255, 255

while True:
    sc.fill((0, 0, 0))
    pygame.draw.rect(sc, col1, (0,500, 10,10))
    pygame.draw.rect(sc, col2, (500,0, 10,10))
    
    pygame.display.flip()



    

        






