import pygame as pg
from pygame.locals import *
from sys import exit
import numpy as np

import numpy as np


global width, height
width, height = 800, 800



class Circle:
    def __init__(self, x, y, speedx, speedy, screen, color_):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.screen = screen
        self.color = color_

    def draw(self):
        pg.draw.circle(self.screen, pg.Color(self.color), (int(self.x)%width, int(self.y)%height), 10)

    def move(self, dt):
        self.x += self.speedx*dt
        self.y += self.speedy*dt



class Game:
    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 800

        self.screen = pg.display.set_mode((self.width, self.height))
        self.screen.fill((50, 210, 0))
        self.clock = pg.time.Clock()



        self.circle = Circle(self.width, self.height,
                            300, 300, self.screen, 'white')


    def run(self):
        while True:
            time_passed = self.clock.tick(10)
            dt = time_passed/1000.0
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.image.save(self.screen, 'ali.jpg')
                    pg.quit()
                    exit()


            self.circle.draw()
            self.circle.move(dt)
            self.update_screen()


    def update_screen(self):
        pg.display.update()
        self.screen.fill((0,130, 0))


game = Game()
game.run()
