import os
import sys
import pygame
from pygame.locals import *


class TetrisPõhi:
    def __init__(self, laius=480, kõrgus=700):
        pygame.init()
        self.laius = laius
        self.kõrgus = kõrgus
        self.aken = pygame.display.set_mode((self.laius, self.kõrgus))
        self.kuup = 30
        self.algusx = 310
        self.algusy = 20

    def joonistakuup(self):
        pygame.draw.rect(self.aken, pygame.Color(200,20,20), (self.algusx, self.algusy, self.kuup, self.kuup))

    def liigutaplokk(self, suund):
        if suund == ("alla"):
            self.algusy += self.kuup
        if suund == ("paremale"):
            self.algusx += self.kuup
        if suund == ("vasakule"):
            self.algusx -= self.kuup

    def nupuvajutus(self, nupp):  #abifunktsioon nupuvajutuste kontrolliks
        if nupp == K_ESCAPE:
            pygame.event.post(pygame.event.Event(QUIT))
            #Väljub programmist
        if nupp == K_LEFT:
            self.liigutaplokk("vasakule")
        if nupp == K_RIGHT:
            self.liigutaplokk("paremale")

    def joonista(self):  #abifunktsioon kaadri joonistamiseks
        self.aken.fill(pygame.Color(200, 200, 200))  #Kogu taust
        pygame.draw.rect(self.aken, pygame.Color(20, 20, 20), (160, 20, 300, 660))  #Mänguväljaku taust
        self.liigutaplokk("alla")
        self.joonistakuup()

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
            fpsClock.tick(2)  #Renderdamise kiirus


põhiaken = TetrisPõhi()
põhiaken.põhikordus()

