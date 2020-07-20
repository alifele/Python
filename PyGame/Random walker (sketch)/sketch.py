import pygame
from pygame.locals import *
import numpy as np


class Sketch:

    def setup(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((15,50,70))
        #self.particle = Particle(self.screen.get_width()/2,self.screen.get_height()/2,self.screen)
        self.particles = []
        self.n_particles = 150
        for i in range(self.n_particles):
            self.particles.append(Particle(self.screen.get_width()/2,self.screen.get_height()/2,self.screen))



    def draw(self):
        for elem in self.particles:
            elem.move()
            elem.drawIt()




class Particle:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.x_ = self.x
        self.y_ = self.y
        self.screen = screen
        self.color = np.random.randint(256, size=3)

    def move(self):
        self.x_ = self.x
        self.y_ = self.y
        self.x += (np.random.random()-0.5)*5
        self.y += (np.random.random()-0.5)*5


    def drawIt(self):
        pygame.draw.line(self.screen, self.color, (self.x_, self.y_), (self.x, self.y))
        #pygame.draw.rect(self.screen, (40,161,151), (self.x, self.y, 10, 10))
        pygame.display.update()
