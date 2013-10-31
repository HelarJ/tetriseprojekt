import os
import sys
import pygame
from pygame.locals import *


class TetrisPõhi:
    def __init__(self, width=480, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def põhikordus(self):
        pygame.mixer.music.load('tetrisA.mp3')
        pygame.mixer.music.play(loops=100)
        #does not loop very well

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


põhiaken = TetrisPõhi()
põhiaken.põhikordus()

