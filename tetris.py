import os
import sys
import pygame
from pygame.locals import *


class TetrisPõhi:
    def __init__(self):
        pygame.init()
        self.laius = 800
        self.kõrgus = 700
        self.aken = pygame.display.set_mode((self.laius, self.kõrgus))
        self.kuup = 30
        self.algnex = 400 #mänguväljaku keskel asuv punkt, millest plokid tulevad välja
        self.algney = 20
        self.x = self.algnex
        self.y = self.algney
        self.äärP = False
        self.äärV = False

    def joonistakuup(self):
        pygame.draw.rect(self.aken, pygame.Color(200,20,20), (self.x, self.y, self.kuup, self.kuup))
        pygame.draw.rect(self.aken, pygame.Color(100,100,100), (self.x+2, self.y+2, self.kuup-4, self.kuup-4))

    def liigutaplokk(self, suund):
        if suund == ("alla"):
            if self.y < 650:
                self.y += self.kuup
        self.onäär()
        if suund == ("paremale"):
            if not self.äärP:
                self.x += self.kuup
        if suund == ("vasakule"):
            if not self.äärV:
                self.x -= self.kuup
        self.äärP = False
        self.äärV = False

    def onäär(self):
        print(self.x)
        if self.x > (self.algnex+110):
            self.äärP = True
        if self.x < (self.algnex-120):
            self.äärV = True

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
        pygame.draw.rect(self.aken, pygame.Color(20, 20, 20), (250, 20, 300, 660))  #Mänguväljaku taust
        self.liigutaplokk("alla")
        self.joonistakuup()

    def muusika(self):
        pygame.mixer.music.load('tetrisA.mp3')
        pygame.mixer.music.play(loops=100)
        #does not loop very well

    def põhikordus(self):
        #self.muusika()
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

