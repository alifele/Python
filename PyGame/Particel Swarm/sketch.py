import pygame
from pygame.locals import *
from pygame import gfxdraw
import landscape
import numpy as np


URL = 'land.png'
class Sketch:

    def setup(self):
        #self.screen = pygame.display.set_mode(self.land.shape)
        self.screen = pygame.display.set_mode((640,480))
        self.land = pygame.image.load(URL).convert()
        #self.screen.fill((15,50,70))
        self.partice = Particle(self.screen.get_width()/2, self.screen.get_height()/2, self.screen)
        self.particles = []
        self.n = 30
        for i in range(self.n):
            self.particles.append(Particle(np.random.randint((self.screen.get_width())),
                                           np.random.randint((self.screen.get_height())), self.screen))



    def draw(self):
        self.screen.blit(self.land,(0,0))
        for elem in self.particles:
            elem.drawIt()
            elem.move()
        pygame.display.update()



class Particle:
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (255,0,0)
        self.size = 8


    def drawIt(self):
        gfxdraw.filled_circle(self.screen,int(self.x), int(self.y),self.size, (0,0,0))
        gfxdraw.filled_circle(self.screen,int(self.x), int(self.y),self.size-2, (255,0,0))


    def move(self):
        rand = (np.random.random(2)-0.5)*5
        self.x += rand[0]
        self.y += rand[1]





if __name__ == "__main__":
    import main
