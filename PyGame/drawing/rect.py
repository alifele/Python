import pygame
from pygame.locals import *
from sys import exit



from random import *

pygame.init()

screen = pygame.display.set_mode((400,400),0,32)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    x,y = pygame.mouse.get_pos()
    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,255,0),(x,y,20,30), 0 )

    pygame.display.update()
