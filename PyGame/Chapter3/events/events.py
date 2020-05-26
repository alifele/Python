from pygame.locals import *
from sys import exit
import pygame

back = 'events/images.jpeg'

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)

background = pygame.image.load(back).convert()

x,y = 0,0
dx, dy = 0,0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                dx = -1
            if event.key == K_RIGHT:
                dx = +1
            if event.key == K_DOWN:
                dy = -1
            if event.key == K_UP:
                dy = +1

        if event.type == KEYUP:
            if event.key == K_LEFT:
                dx = 0
            if event.key == K_RIGHT:
                dx = 0
            if event.key == K_DOWN:
                dy = 0
            if event.key == K_UP:
                dy = 0


        x += dx
        y += dy

        screen.fill((0,0,0))
        screen.blit(background,(x,y))


        pygame.display.update()
