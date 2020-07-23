import pygame
from pygame.locals import *
from pygame import gfxdraw
from landscape import generate
import numpy as np
import copy

def transfer_pos(pos):
    pos[0] = (pos[0]-320)/16
    pos[1] = (pos[1]-240)/(-12)
    return pos

URL = 'land.png'
C1 = 0.1
C2 = 0.1
W = 0.5
n_particles = 50

def find_best_place(Particles, Global_best_place):
    for particle in Particles:
        particle.global_calc = 1
        if particle.best_place[1] < Global_best_place[1]:
            #print('hey')
            Global_best_place = [np.random.random(2),1000]
            Global_best_place[1] = generate(*transfer_pos(Global_best_place[0]))
            #Global_best_place = copy.deepcopy(particle.best_place)
    return Global_best_place

def transfer_x(x):
    return (x-320)/16

def transfer_y(y):
    return (y-240)/(-12)




class Sketch:

    def setup(self):
        #self.screen = pygame.display.set_mode(self.land.shape)
        self.screen = pygame.display.set_mode((640,480))
        self.land = pygame.image.load(URL).convert()
        #self.screen.fill((15,50,70))
        self.partice = Particle(self.screen.get_width()/2, self.screen.get_height()/2, self.screen)
        self.particles = []
        self.n = n_particles
        for i in range(self.n):
            self.particles.append(Particle(np.random.randint((self.screen.get_width())),
                                           np.random.randint((self.screen.get_height())), self.screen))



        self.Global_best_place = [np.random.random(2),1000]
        print(self.Global_best_place)
        self.Global_best_place[1] = generate(*transfer_pos(self.Global_best_place[0]))

    def draw(self):
        self.screen.blit(self.land,(0,0))
        for elem in self.particles:
            #import pdb; pdb.set_trace()
            self.Global_best_place=find_best_place(self.particles, self.Global_best_place)
            elem.update_vel()
            elem.move()
            elem.drawIt()
            print(Global_best_place)
        pygame.display.update()



class Particle:
    def __init__(self,x,y,screen):
        self.pos = np.array([x,y])
        self.screen = screen
        self.color = (255,0,0)
        self.size = 8
        self.global_calc = 0

        self.best_place = [self.pos, 1000]
        self.best_place[1] = self.clac_score(self.best_place[0])
        self.vel = np.random.random(2)


    def drawIt(self):
        gfxdraw.filled_circle(self.screen,int(self.pos[0]), int(self.pos[1]),self.size, (0,0,0))
        gfxdraw.filled_circle(self.screen,int(self.pos[0]), int(self.pos[1]),self.size-2, (255,0,0))


    def move(self):
        #rand = (np.random.random(2)-0.5)*5
        #self.pos = self.pos +  rand
        self.pos = self.pos + self.vel


        val = self.clac_score(transfer_pos(self.pos))
        if val < self.best_place[1]:
            self.best_place[1] = val
            self.best_place[0] = self.pos

        self.pos[0] = self.pos[0]%self.screen.get_width()
        self.pos[1] = self.pos[1]%self.screen.get_height()



    def clac_score(self, pos):
        return generate(*pos)

    def update_vel(self):

        try:
            self.global_calc == 0
        except ArithmeticError:
            print('please calculate the global best place by calling find_best_place function')
            raise ValueError

        phi_1 = np.random.random()
        phi_2 = np.random.random()
        self.vel = W*self.vel + phi_1*C1*(self.best_place[0]-self.pos)+ phi_2*C2*(Global_best_place[0]-self.pos)

        self.global_calc = 0









if __name__ == "__main__":
    import main
