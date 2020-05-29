import pygame as pg
from pygame.locals import *
from sys import exit
import numpy as np


class Rocket:
    def __init__(self, x, y, screen, color_):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color_

    def draw(self):
        pg.draw.rect(self.screen, pg.Color(self.color),(self.x, self.y, 1,1))

    def move(self):
        self.x += 2*np.random.random() - 1
        self.y += 2*np.random.random() - 1



class Game:
    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 800
        self.screen = pg.display.set_mode((self.width,self.height),0,32)
        self.screen.fill((50,120,0))

        self.rocket_list = []
        colors = ['red', 'blue', 'black', 'yellow', 'white']
        for i in range(5):
            self.rocket_list.append(Rocket(self.width/2,self.height/2,self.screen, colors[i] ))


    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    exit()



            for elem in self.rocket_list:
                elem.draw()
                elem.move()

            self.update_screen()


    def update_screen(self):
        pg.display.update()
        #self.screen.fill((0,130,0))




game = Game()
game.run()
