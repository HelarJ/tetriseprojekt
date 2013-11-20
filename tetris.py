import os
import sys
import pygame
from pygame.locals import *
from random import *


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
        self.maatriks = [] #mänguväljaku representation

        #kõik klotside kujud ja nende asendid
        self.O_shape = [[(0, 0, 0, 0),
                    (0, 1, 1, 0),
                    (0, 1, 1, 0),
                    (0, 0, 0, 0)]]

        self.I_shape = [[(0, 0, 0, 0),
                    (1, 1, 1, 1),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 1, 0, 0)]]

        self.S_shape = [[(0, 0, 0, 0),
                    (0, 1, 1, 0),
                    (1, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (0, 1, 1, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 0)]]

        self.Z_shape = [[(0, 0, 0, 0),
                    (0, 1, 1, 0),
                    (0, 0, 1, 1),
                    (0, 0, 0, 0)],
                   [(0, 0, 1, 0),
                    (0, 1, 1, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)]]

        self.J_shape = [[(0, 0, 0, 0),
                    (1, 0, 0, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 1, 0),
                    (0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (1, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 0, 0, 0),
                    (1, 1, 1, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 0)]]

        self.L_shape = [[(0, 0, 0, 0),
                    (0, 0, 0, 0),
                    (1, 1, 1, 0),
                    (1, 0, 0, 0)],
                   [(1, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 1, 1, 0),
                    (0, 0, 0, 0)],
                   [(0, 0, 1, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.T_shape = [[(0, 0, 0, 0),
                    (0, 0, 0, 0),
                    (1, 1, 1, 0),
                    (0, 1, 0, 0)],
                   [(0, 1, 0, 0),
                    (1, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (0, 1, 1, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.shapes = {"O": self.O_shape,
                  "I": self.I_shape,
                  "S": self.S_shape,
                  "Z": self.Z_shape,
                  "J": self.J_shape,
                  "L": self.L_shape,
                  "T": self.T_shape}

    def tühiplats(self):
        for i in range(21):
            rida = []
            for j in range(9):
                rida.append(0)
            self.maatriks.append(rida)


    def teeUusKlots(self):
        #teeb random uue random rotationis klotsi
        #returnib klots, mis on dictionary võtmetega kuju, rotation, x, y (värv ka äkki?)

        kuju = choice(list(self.shapes.keys()))
        klots = {"kuju": kuju,
                 "asend": randint(0, len(self.shapes[kuju])-1),
                 self.x: self.algnex,
                 self.y: self.algney}
        return klots

    def lisaKlotsMaatriksisse(self):

        #kui klots paika saab, lisatakse maatriksisse
        #tuleb gameloopis kusagil välja kutsuda!

    def kustutaTäisRida(self):

        #kustutab kõik täis read
        #liigutab kõik mis nende peal on alla
        #returnib mitu rida kustutati


    def joonista_klots(self):
        #teised klotsid ka vaja lisada
        self.aken.blit(self.sinine, (self.x, self.y))


    def liigutaplokk(self, suund):
        #vaja muuta et liigutaks kõiki klotse, mitte ainult kuupi
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

    #muuda et kontrolliks ka alumist serva
    #muuda et kontrolliks teisi klotse (kontrrolli maatriksit)
    def onäär(self):
        #print(self.x)
        if self.x > (self.algnex + 110):
            self.äärP = True
        if self.x < (self.algnex - 120):
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
        self.joonista_klots()
        self.i += 1

    def muusika(self):
        pygame.mixer.music.load(os.path.join('andmed', 'tetrisA.mp3'))
        pygame.mixer.music.play(-1, 0.0)
        #does not loop very well
        #tried to change loop behaviour to no avail, media playeris loobib samamoodi väikse pausiga
        #viskasin documentationile pilgu peale, no obv way to fix this
        # -1 tähendab et infinite loop ja 0.0 näitab sekundites kust järgmist loopi alustada
        #okei, paistab et see paus ongi pygame viga teatud failide puhul
        #mono wawid peaks väidetavalt toimima

        #maybe replace with afro circus

    def põhikordus(self):
        self.muusika()
        self.tühiplats()

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

