import pygame as pg
from pygame.locals import *
import sys
from pygame import gfxdraw
import numpy as np
from perlin_noise import generate_perlin_noise_2d
import pdb
import matplotlib.pyplot as plt

global life_time
life_time = 250
n_rockets = 80
cross_over_ratio = 0.5
mutation_ratio = 0.1
mutation_rate = 0.5
golden_transfer_ratio = 0.2




#
# ██████   ██████   ██████ ██   ██ ███████ ████████
# ██   ██ ██    ██ ██      ██  ██  ██         ██
#  ██████  ██    ██ ██      █████   █████      ██
# ██   ██ ██    ██ ██      ██  ██  ██         ██
# ██   ██  ██████   ██████ ██   ██ ███████    ██




class Rocket:
    def __init__(self, x, y ,screen,noise1, noise2):
        self.x = x
        self.y = y
        self.vx = 0 * (np.random.randn())
        self.vy = 0 * (np.random.randn())-5
        #self.forcex = 150*(np.random.randn(life_time))
        #self.forcey = 150*(np.random.randn(life_time))
        self.forcex = noise1 # numpy array
        self.forcey = noise2 # numpy array



        self.screen = screen
        self.freez = False
        self.fitness = 0
        self.fitness_norm = 0


    def reset_x_v(self):
        self.x = width/2
        self.y = height-50
        self.vx = 0 * (np.random.randn())
        self.vy = 0 * (np.random.randn())-5


    def draw(self):
        gfxdraw.filled_circle(self.screen,int(self.x),int(self.y),1, (114, 214, 202))
        # I used the above function to reduce the aliasing in the drawn circle

    def move(self,frame,dt):

        if self.freez == False:
            self.vx += self.forcex[frame]*dt
            self.vy += self.forcey[frame]*dt

            self.x += self.vx*dt
            self.y += self.vy*dt

    def calc_fittness(self, target_center):
        self.fitness = 1/((self.dist((self.x, self.y), target_center))+1)


    def dist(self, A,B):
        return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5


#
# ████████  █████  ██████   ██████  ███████ ████████
#    ██    ██   ██ ██   ██ ██       ██         ██
#    ██    ███████ ██████  ██   ███ █████      ██
#    ██    ██   ██ ██   ██ ██    ██ ██         ██
#    ██    ██   ██ ██   ██  ██████  ███████    ██

class Target:
    def __init__(self, screen):
        self.screen = screen
        self.w = 120
        self.h = 20
        self.marg = 20
        self.center = (width/2, self.h)
        self.corners = [(width/2-self.w/2, self.marg-self.h/2)
                       ,(width/2+self.w/2, self.marg-self.h/2)
                       ,(width/2+self.w/2, self.marg+self.h/2)
                       ,(width/2-self.w/2, self.marg+self.h/2)]

    def draw(self):
        pg.draw.rect(self.screen, pg.Color('red'), (width/2-self.w/2, self.marg-self.h/2, self.w,self.h))


#
#  ██████   █████  ███    ███ ███████
# ██       ██   ██ ████  ████ ██
# ██   ███ ███████ ██ ████ ██ █████
# ██    ██ ██   ██ ██  ██  ██ ██
#  ██████  ██   ██ ██      ██ ███████

class Game:
    def __init__(self, width, height, flag = None):

        self.width = width
        self.height = height
        self.flag = flag
        self.initailize()
        self.init_rockets()
        self.target = Target(self.screen)

    def initailize(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((self.width, self.height), 0,32)
        self.screen.fill((47, 73, 97))
        if self.flag == 'first_round':
            self.generate_noise()


    def init_rockets(self):
        if self.flag == 'first_round':
            self.n_rockets = n_rockets
            self.rocket_list = []
            for i in range(self.n_rockets):
                noise1 = 150*(self.noises1[i*life_time:(i+1)*life_time])
                noise2 = 150*(self.noises2[i*life_time:(i+1)*life_time])
                self.rocket_list.append(Rocket(width/2, height-50,self.screen,noise1, noise2))
        else:
            for rock in self.rocket_list:
                rock.reset_x_v()



    def generate_noise(self):
        self.noises1 = generate_perlin_noise_2d((256,256), (16, 16)).reshape(-1)
        self.noises2 = generate_perlin_noise_2d((256,256), (16, 16)).reshape(-1)


    def run_generation(self):
        self.__init__(width, height, flag='no_first_round')
        for frame in range(life_time):
            dt = self.clock.tick(30)/1000
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            for i in range(self.n_rockets):
                self.wall_collide()
                self.rocket_list[i].move(frame,dt)
                self.rocket_list[i].draw()

            self.target.draw()
            self.update_screen()


    def run(self):
        while True:
            self.run_generation()

            self.new_rock_list = []
            self.fitness()
            self.golden_transfer()
            self.cross_over()
            self.mutate()
            self.random_transfer()

            print(len(self.rocket_list))

            self.rocket_list = self.new_rock_list.copy()


    def random_transfer(self):
        n = len(self.rocket_list) - len(self.new_rock_list)

        for i in range(n):
            rand = np.random.random()
            rock = self.rocket_list[rand]
            self.new_rock_list.append(Rocket(width/2, height-50,self.screen, rock.forcex.copy(), rock.forcey.copy()))





    def fitness(self):
        for rock in self.rocket_list:
            rock.calc_fittness(self.target.center)


        self.rockets_score_list = []
        for i, elem in enumerate(self.rocket_list):
            self.rockets_score_list.append([elem.fitness,i,elem.fitness,-1]) # third is for normal_score, fourth is for accum
        self.rockets_score_list = np.array(self.rockets_score_list)


        self.rockets_score_list = self.rockets_score_list[self.rockets_score_list[:,0].argsort()][::-1]

        sum_of_fit = self.rockets_score_list[:,0].sum()
        self.rockets_score_list[:,2] /= sum_of_fit


        self.rockets_score_list[0,3] = self.rockets_score_list[0,2]
        for i in range(1, len(self.rockets_score_list)):
            self.rockets_score_list[i,3]=self.rockets_score_list[i-1,3]+self.rockets_score_list[i,2]


    def mutate(self):
        for i in range(int(mutation_ratio*n_rockets)):


            rand = np.random.random(2)
            rock_ind = np.argmax(rand[0] < self.rockets_score_list[:,3])


            gen1_x = self.rocket_list[rock_ind].forcex.copy()
            gen1_y = self.rocket_list[rock_ind].forcey.copy()

            rand_ind1 = np.random.randint(len(gen1_x), size=int(mutation_rate*len(gen1_x))+1)
            rand_ind2 = np.random.randint(len(gen1_x), size=int(mutation_rate*len(gen1_x))+1)

            gen1_x[rand_ind1] = np.random.random(len(rand_ind1)) * gen1_x[0]
            gen1_y[rand_ind2] = np.random.random(len(rand_ind1)) * gen1_y[0]



            self.new_rock_list.append(Rocket(width/2, height-50,self.screen, gen1_x.copy(), gen1_y.copy()))





    def golden_transfer(self):
        for i in range(int(golden_transfer_ratio * n_rockets)):
            elem = int(self.rockets_score_list[i,1])
            rocket = self.rocket_list[elem]
            self.new_rock_list.append(Rocket(width/2, height-50,self.screen,rocket.forcex.copy(), rocket.forcey.copy()))






    def cross_over(self):
        for i in range(int(n_rockets*cross_over_ratio)):

            rand = np.random.random(2)
            rock1_ind = np.argmax(rand[0] < self.rockets_score_list[:,3])
            rock2_ind = np.argmax(rand[1] < self.rockets_score_list[:,3])


            gen1_x = self.rocket_list[rock1_ind].forcex.copy()
            gen1_y = self.rocket_list[rock1_ind].forcey.copy()

            gen2_x = self.rocket_list[rock2_ind].forcex.copy()
            gen2_y = self.rocket_list[rock2_ind].forcey.copy()


            cross_over_rand1 = np.random.randint(life_time)
            cross_over_rand2 = np.random.randint(life_time)

            temp1 = gen1_x[cross_over_rand1:].copy()
            gen1_x[cross_over_rand1:] = gen2_x[cross_over_rand1:].copy()
            gen2_x[cross_over_rand1:] = temp1.copy()


            temp1 = gen1_y[cross_over_rand2:].copy()
            gen1_y[cross_over_rand2:] = gen2_y[cross_over_rand2:].copy()
            gen2_y[cross_over_rand2:] = temp1.copy()

            self.new_rock_list.append(Rocket(width/2, height-50,self.screen,gen1_x.copy(), gen1_y.copy()))
            self.new_rock_list.append(Rocket(width/2, height-50,self.screen,gen2_x.copy(), gen2_y.copy()))




    def update_screen(self):
        pg.display.update()
        #self.screen.fill((47, 73, 97))



    def wall_collide(self):
        for rock in self.rocket_list:
            if rock.freez == False:
                if rock.x > width or rock.y > height or rock.x<0 or rock.y<0:
                    rock.freez = True

                if rock.x > self.target.corners[0][0] and rock.x < self.target.corners[1][0] and rock.y>self.target.corners[0][1] and rock.y<self.target.corners[2][1]:
                    rock.freez = True







#
# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████

if __name__ == "__main__":
    width = 800
    height = 600
    game = Game(width, height, flag ='first_round')
    game.run()
