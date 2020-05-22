from pygame.locals import *
from sys import exit
import pygame
import time



pygame.init()
screen = pygame.display.set_mode((800,600), 0,32)

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

        print(event)



    pygame.display.update()
