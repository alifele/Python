import pygame as pg
from pygame.locals import *
import sys
from pygame import gfxdraw
import numpy as np
from perlin_noise import generate_perlin_noise_2d

global life_time
life_time = 500


#
# ██████   ██████   ██████ ██   ██ ███████ ████████
# ██   ██ ██    ██ ██      ██  ██  ██         ██
# ██████  ██    ██ ██      █████   █████      ██
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


    def reset_x_v(self):
        self.x = width/2
        self.y = height-50
        self.vx = 10 * (np.random.randn())
        self.vy = 10 * (np.random.randn())-5


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
            self.n_rockets = 50
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
            self.fitness()
            self.cross_over()




    def fitness(self):
        for rock in self.rocket_list:
            rock.calc_fittness(self.target.center)

        sum_of_fit = 0
        for rock in self.rocket_list:
            sum_of_fit += rock.fitness

        for rock in self.rocket_list:
            rock.fitness /= sum_of_fit

        self.accum_list = []
        self.accum_list.append(self.rocket_list[0].fitness)
        for rock in self.rocket_list[1:]:
            self.accum_list.append(self.accum_list[-1]+rock.fitness)

    def cross_over(self):
        mutation_rate = 0.05
        for i in range(int(self.n_rockets/3)):
            rand = np.random.random(2)
            rock1_ind = np.argmax(rand[0] < self.accum_list)
            rock2_ind = np.argmax(rand[1] < self.accum_list)

            gen1_x = self.rocket_list[rock1_ind].forcex.copy()
            gen1_y = self.rocket_list[rock1_ind].forcey.copy()

            gen2_x = self.rocket_list[rock2_ind].forcex.copy()
            gen2_y = self.rocket_list[rock2_ind].forcey.copy()


            cross_over_rand1 = np.random.randint(life_time)
            cross_over_rand2 = np.random.randint(life_time)

            new_gen1_x = gen1_x[:cross_over_rand1].tolist() + gen2_x[cross_over_rand1:].tolist()
            new_gen1_x = np.array(new_gen1_x)
            new_gen1_y = gen1_y[:cross_over_rand2].tolist() + gen2_y[cross_over_rand2:].tolist()
            new_gen1_y = np.array(new_gen1_y)

            new_gen2_x = gen2_x[:cross_over_rand1].tolist() + gen1_x[cross_over_rand1:].tolist()
            new_gen2_x = np.array(new_gen2_x)
            new_gen2_y = gen2_y[:cross_over_rand2].tolist() + gen1_y[cross_over_rand2:].tolist()
            new_gen2_y = np.array(new_gen2_y)


            self.rocket_list[rock1_ind].forcex = new_gen1_x
            self.rocket_list[rock1_ind].forcey = new_gen1_y

            self.rocket_list[rock2_ind].forcex = new_gen2_x
            self.rocket_list[rock2_ind].forcey = new_gen2_y




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
