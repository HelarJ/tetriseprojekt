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
        self.punane = pygame.image.load(os.path.join("andmed", "punane.png"))
        self.sinine = pygame.image.load(os.path.join("andmed", "sinine.png"))
        self.hall = pygame.image.load(os.path.join("andmed", "hall.png"))
        self.äärP = False
        self.äärV = False
        self.fpsClock = pygame.time.Clock()
        self.kiirus = 15 #mida väiksem seda kiirem
        self.i = 0

    def joonistakuup(self):
        self.aken.blit(self.sinine, (self.x, self.y))

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
        if nupp == K_DOWN:
            self.liigutaplokk("alla")

    def joonista(self):  #abifunktsioon kaadri joonistamiseks
        self.aken.fill(pygame.Color(100, 100, 100))  #Kogu taust
        pygame.draw.rect(self.aken, pygame.Color(20, 20, 20), (250, 20, 300, 660))  #Mänguväljaku taust
        if self.i == self.kiirus:
            self.liigutaplokk("alla")
            self.i = 0
        self.joonistakuup()
        self.i+=1

    def muusika(self):
        pygame.mixer.music.load(os.path.join('andmed','tetrisA.mp3'))
        pygame.mixer.music.play(loops=100)
        #does not loop very well

    def põhikordus(self):
        #self.muusika()


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.nupuvajutus(event.key)

            self.joonista()
            pygame.display.update()  #joonistab kõik ekraanile
            self.fpsClock.tick(30)  #Renderdamise kiirus



põhiaken = TetrisPõhi()
põhiaken.põhikordus()

