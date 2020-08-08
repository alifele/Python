import pygame
from pygame.locals import *
from pygame import gfxdraw
from landscape import generate
import numpy as np
import copy


def transfer_pos(poos):  # will transfer from (0:640,0:480) into (-20:20,-20:20)
    pos = copy.deepcopy(poos)
    pos[0] = (pos[0]-320)/16
    pos[1] = (pos[1]-240)/(-12)
    return pos

URL = 'land.png'
C1 = 0.6
C2 = 0.5
W = 0.8
n_particles = 100


#update_cof(C1,C2,W)

def find_best_place(Particles, Global_best_place):
    Global_best_place = copy.deepcopy(Global_best_place)
    for particle in Particles:
        # Global_best_place = [[np.random.randint(640),
        #                                np.random.randint(480)],1000]
        #print(particle.best_place[1])
        if particle.best_place[1] < Global_best_place[1]:
            #self.Global_best_place = [[np.random.randint((self.screen.get_width())),
            #                               np.random.randint((self.screen.get_height()))],1000]
            Global_best_place[0] = copy.deepcopy(particle.best_place[0])
            Global_best_place[1] = generate(*transfer_pos(copy.deepcopy(Global_best_place[0])))
    return Global_best_place


class Sketch:

    def setup(self):

    #import pdb; pdb.set_trace()

        self.screen = pygame.display.set_mode((640,480))
        self.land = pygame.image.load(URL).convert()
        self.particles = []
        self.n = n_particles
        for i in range(self.n):
            self.particles.append(Particle(np.random.randint((self.screen.get_width())),
                                           np.random.randint((self.screen.get_height())), self.screen))



        # self.Global_best_place = [[np.random.randint((self.screen.get_width())),
        #                                np.random.randint((self.screen.get_height()))],1000]

        self.Global_best_place = [self.particles[0].pos, 1000]
        self.Global_best_place[1] = generate(*transfer_pos(self.Global_best_place[0]))


        #self.Global_best = copy.deepcopy(self.particle[np.random.randint(n_particles)])

    def draw(self):
        self.screen.blit(self.land,(0,0))
        #self.Global_best_place=find_best_place(self.particles, self.Global_best_place)
        for elem in self.particles:
            elem.update_vel(self.Global_best_place, C1,C2,W)
            elem.move()
            elem.drawIt()


        self.Global_best_place=find_best_place(self.particles, self.Global_best_place)
        pygame.display.update()

        #import pdb; pdb.set_trace()




class Particle:
    def __init__(self,x,y,screen):
        self.pos = np.array([x,y])
        self.screen = screen
        self.color = (255,0,0)
        self.size = 8
        self.global_calc = 0

        self.best_place =copy.deepcopy([self.pos, 1000])
        self.best_place[1] = self.clac_score(self.best_place[0])
        self.vel = np.random.random(2)
        self.coeff = 1


    def drawIt(self):
        gfxdraw.filled_circle(self.screen,int(self.pos[0]), int(self.pos[1]),self.size, (0,0,0))
        gfxdraw.filled_circle(self.screen,int(self.pos[0]), int(self.pos[1]),self.size-2, (255,0,0))


    def move(self):
        self.pos = self.pos + self.vel
        self.pos[0] = self.pos[0]%self.screen.get_width()
        self.pos[1] = self.pos[1]%self.screen.get_height()

        val = self.clac_score(transfer_pos(self.pos))
        if  val < self.best_place[1] :
            self.best_place[1] = val
            self.best_place[0] = copy.deepcopy(self.pos)





    def clac_score(self, pos):
        return generate(*pos)

    def update_vel(self, Global_best_place,C1,C2,W):
        #
        # try:
        #     self.global_calc == 0
        # except ArithmeticError:
        #     raise ValueError

        phi_1 = np.random.random()
        phi_2 = np.random.random()
        self.coeff *= 0.994
        C1 *= self.coeff
        C2 *= self.coeff
        W *= self.coeff
        self.vel = W*self.vel + phi_1*C1*(self.best_place[0]-self.pos)+ phi_2*C2*(Global_best_place[0]-self.pos)

        #print(C1)
        #update_cof()









if __name__ == "__main__":
    import main
