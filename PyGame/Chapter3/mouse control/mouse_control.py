background_image_filename = 'cern_biology.jpg'
mouse = 'images.jpeg'


import pygame
from pygame.locals import *
import matplotlib.pyplot as plt
from sys import exit


pygame.init()

screen = pygame.display.set_mode((1250,400),RESIZABLE,32)
pygame.display.set_caption("hello there")

background = pygame.image.load(background_image_filename).convert()
mouse_c = pygame.image.load(mouse).convert_alpha()



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


        screen.blit(background, (0,0))



        pygame.display.update()
