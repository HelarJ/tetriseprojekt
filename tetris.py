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

    def nupuvajutus(self, nupp):  #abifunktsioon nupuvajutuste kontrolliks
        if nupp == K_ESCAPE:
            pygame.event.post(pygame.event.Event(QUIT))
            #Väljub programmist

    def joonista(self):  #abifunktsioon kaadri joonistamiseks
        self.screen.fill(pygame.Color(200, 200, 200))  #Kogu taust
        pygame.draw.rect(self.screen, pygame.Color(20, 20, 20), (160, 20, 300, 680))  #Mänguväljaku taust

    def muusika(self):
        pygame.mixer.music.load('tetrisA.mp3')
        pygame.mixer.music.play(loops=100)
        #does not loop very well

    def põhikordus(self):
        self.muusika()
        fpsClock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.nupuvajutus(event.key)

            self.joonista()
            pygame.display.update()  #joonistab kõik ekraanile
            fpsClock.tick(30)  #mäng jookseb 30FPS


põhiaken = TetrisPõhi()
põhiaken.põhikordus()

