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
        self.algnex = 4  #mänguväljaku keskel asuv punkt, millest plokid tulevad välja
        self.algney = 0
        self.x = self.algnex
        self.y = self.algney
        self.punane = pygame.image.load(os.path.join("andmed", "punane.png"))
        self.sinine = pygame.image.load(os.path.join("andmed", "sinine.png"))
        self.hall = pygame.image.load(os.path.join("andmed", "hall.png"))
        self.taust = pygame.image.load(os.path.join("andmed", "TetrisTaust.png"))
        self.äärP = False
        self.äärV = False
        self.äärPõhi = False
        self.fpsClock = pygame.time.Clock()
        self.kiirus = 15  #mida väiksem seda kiirem
        self.i = 0
        self.maatriks = []  #mänguväljaku representation
        self.klots = []

        #ajutine
        self.vaja_uus_klots = False
        #

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
        #

        kuju = choice(list(self.shapes.keys()))
        self.klots = {"kuju": kuju,
                 "asend": self.shapes[kuju][0],
                 "x": self.algnex,
                 "y": self.algney,
                 "värv": self.punane}
        print(self.klots)
    def lisaKlotsMaatriksisse(self):
        #vist ei tööta
        koordinaat = False
        #print(self.klots)
        for x in range(4):
            for y in range(4):
                #print(self.klots)
                koordinaat = self.klots["asend"][y][x]
                #print(koordinaat)
                #print(self.klots["asend"][y][x])
                #print(self.shapes[self.klots["kuju"]][koordinaadid])
                #print(self.klots["x"])
                #print(self.klots["y"])
                if koordinaat != 0:
                    self.maatriks[x + self.klots["x"]][y + self.klots["y"]] = self.klots["värv"]

        #kui klots paika saab, lisatakse maatriksisse
        #tuleb gameloopis kusagil välja kutsuda!

    def kasTäisRida(self, maatriks, y):
        a = True

    def kustutaTäisRida(self, maatriks):
        a = True
        return a
        #kustutab kõik täis read
        #liigutab kõik mis nende peal on alla
        #returnib mitu rida kustutati


    def joonista_maatriks(self):
        #teised klotsid ka vaja lisada
        print(self.maatriks)
        for rida in self.maatriks:
            i = 0
            for element in rida:
                if element != 0:

                    self.aken.blit(element, (250 + (self.klots["y"] *30), 20 + (self.klots["x"] * 30)))
                i += 1




    def liigutaplokk(self, suund):
        #vaja muuta et liigutaks kõiki klotse, mitte ainult kuupi
        self.is_valid_position()
        if suund == ("alla"):
            if not self.äärPõhi:
                self.klots["x"] += 1
                #self.y += 1

        if suund == ("paremale"):
            if not self.äärP and not self.äärPõhi:
                self.klots["y"] += 1

        if suund == ("vasakule"):
            if not self.äärV and not self.äärPõhi:
                self.klots["y"] -= 1

        #self.lisaKlotsMaatriksisse()
        self.äärP = False
        self.äärV = False
        self.äärPõhi = False

    #muuda et kontrolliks ka alumist serva
    #muuda et kontrolliks teisi klotse (kontrrolli maatriksit)
    def is_valid_position(self):
        #kui valid pos siis return True
        #print(self.x)
        if self.x > (self.algnex + 4):
            self.äärP = True
        if self.x < (self.algnex - 5):
            self.äärV = True
        if self.y >= 21:
            self.äärPõhi = True
            self.vaja_uus_klots = True
        print(self.y)
        if self.y < 21:
            self.vaja_uus_klots = False




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
        #self.aken.fill(pygame.Color(100, 100, 100))  #Kogu taust
        self.aken.blit(self.taust, (0,0))
        #pygame.draw.rect(self.aken, pygame.Color(20, 20, 20), (250, 20, 300, 660))  #Mänguväljaku taust
        if self.i == self.kiirus:
            self.liigutaplokk("alla")
            self.i = 0
        if self.vaja_uus_klots:
            print("wut wuuuuut")
            self.teeUusKlots()
        self.lisaKlotsMaatriksisse()
        self.joonista_maatriks()
        self.i += 1

    def muusika(self):
        pygame.mixer.music.load(os.path.join('andmed', 'tetrisA.wav'))
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

        self.teeUusKlots()

        while True:
            #if self.vaja_uus_klots:
                #self.klots = self.teeUusKlots()

                #kui enam ei mahu siis mäng läbi
                #if not is_valid_position(self, maatriks, kukkuv_klots):
                #    return
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

