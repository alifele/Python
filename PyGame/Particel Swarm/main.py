import pygame
from pygame.locals import *
from sys import exit
from sketch import Sketch

pygame.init()
sketch = Sketch()
sketch.setup()
clock = pygame.time.Clock()
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    sketch.draw()
