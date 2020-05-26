import sys
import math
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class App():
    def __init__(self, width=800, height = 600):
        self.title = 'demo'
        self.fps = 60
        self.width = width
        self.height = height



    def start(self):
        pygame.init()
        pygame.display.set_mode((self.width, self.height),OPENGL|DOUBLEBUF)

        pygame.display.set_caption(self.title)
        glEnable(GL_CULL_FACE)

        glMatrixMode(GL_MODELVIEW)

        clock = pygame.time.Clock()
        while True:
            dt = clock.tick(self.fps)
            self.process_input(dt)
            self.display()


    def process_input(self, dt):
        for event in pygame.event.get():
            if event in pygame == QUIT:
                self.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit()

                if event.key == K_F1:
                    self.light.switch_color()
