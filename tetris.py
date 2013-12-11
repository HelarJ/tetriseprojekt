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
        self.algnex = 0  #mänguväljaku keskel asuv punkt, millest plokid tulevad välja
        self.algney = 4
        self.x = self.algnex
        self.y = self.algney
        self.punane = pygame.image.load(os.path.join("andmed", "punane.png"))
        self.sinine = pygame.image.load(os.path.join("andmed", "sinine.png"))
        self.kollane = pygame.image.load(os.path.join("andmed", "kollane.png"))
        self.roheline = pygame.image.load(os.path.join("andmed", "roheline.png"))
        self.roosa = pygame.image.load(os.path.join("andmed", "roosa.png"))
        self.oranz = pygame.image.load(os.path.join("andmed", "oranz.png"))
        self.helesinine = pygame.image.load(os.path.join("andmed", "helesinine.png"))
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
        self.järgmineKlots = []
        self.vaja_uus_klots = False
        self.skoor = 0

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
        for i in range(22):
            rida = []
            for j in range(10):
                rida.append(0)
            self.maatriks.append(rida)

    def võta_värv(self, kuju):
        if kuju == "O":
            return self.sinine
        if kuju == "I":
            return self.punane
        if kuju == "S":
            return self.helesinine
        if kuju == "Z":
            return self.roheline
        if kuju == "L":
            return self.oranz
        if kuju == "J":
            return self.roosa
        if kuju == "T":
            return self.kollane


    def teeUusKlots(self):
        #teeb random uue random rotationis klotsi
        #returnib klots, mis on dictionary võtmetega kuju, rotation, x, y (värv ka äkki?)
        #
        klots = 0
        kuju = choice(list(self.shapes.keys()))
        klots = {"kuju": kuju,
                 "asend": self.shapes[kuju][0],
                 "x": self.algnex,
                 "y": self.algney,
                 "värv": self.võta_värv(kuju)}

        return klots

    def lisaKlotsMaatriksisse(self):
        #vist ei tööta
        koordinaat = False
        #print(self.klots)
        for self.x in range(4):
            for self.y in range(4):
                #print(self.klots)
                koordinaat = self.klots["asend"][self.y][self.x]
                #print(koordinaat)
                #print(self.klots["asend"][y][x])
                #print(self.shapes[self.klots["kuju"]][koordinaadid])
                #print(self.klots["x"])
                #print(self.klots["y"])
                if koordinaat != 0:
                    try:
                        self.maatriks[self.x + self.klots["x"]][self.y + self.klots["y"]] = self.klots["värv"]
                    except IndexError:
                        self.äärPõhi = True
                        self.vaja_uus_klots = True

        #kui klots paika saab, lisatakse maatriksisse
        #tuleb gameloopis kusagil välja kutsuda!

    def kontrolli_ridu(self):
        täis = False
        for rida in range(10):
            arv = 0
            for element in range(9):
                 if self.maatriks[rida][element] != 0:
                     arv += 1
            if arv == 10:
                self.skoor += 100
                for abi in range(rida-1, 0, -1):
                    self.maatriks[rida] = self.maatriks[rida+1]


    def joonista_maatriks(self):
        #teised klotsid ka vaja lisada
        #print(self.maatriks)
        self.kontrolli_ridu()
        j = 0
        for rida in self.maatriks:
            #print(rida)
            i = 0
            arv = 0
            for element in rida:

                if element != 0:

                    self.aken.blit(element, (250 + (i * 30), 20 + (j * 30)))
                if element == 0:  #Temporary, maatriksi sisu näitamiseks
                    self.aken.blit(self.hall, (250 + (i * 30), 20 + (j * 30)))
                i += 1
            j +=  1

    def joonista_järgmine_klots(self):
        #klotside algseid asenedid tuleb muuta et normaalsem oleks
        j = 0
        for self.x in range(4):
            i = 0
            for self.y in range(4):
                koordinaat = self.järgmineKlots["asend"][self.y][self.x]
                if koordinaat != 0:
                    self.aken.blit(self.järgmineKlots["värv"], (65 + (i * 30), 230 + (j * 30)))
                i += 1
            j += 1

    def liigutaplokk(self, suund):
        #vaja muuta et liigutaks kõiki klotse, mitte ainult kuupi
        #self.is_valid_position()
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
        try:
            self.maatriks[self.x + self.klots["x"]][1+ self.y + self.klots["y"]] = self.klots["värv"]
        except IndexError:
            self.äärPõhi = True
            self.vaja_uus_klots = True


        #if self.x > 8:
        #    self.äärP = True
        #if self.x < (self.algnex - 5):
        #    self.äärV = True
        #if self.y >= 21:
        #    self.äärPõhi = True
        #    self.vaja_uus_klots = True
        #print(self.y)
        #if self.y < 21:
        #    self.vaja_uus_klots = False




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
            self.klots = self.järgmineKlots
            self.järgmineKlots = self.teeUusKlots()
            print(self.klots)
            print(self.järgmineKlots)
            self.vaja_uus_klots = False
        self.lisaKlotsMaatriksisse()
        self.joonista_maatriks()
        self.joonista_järgmine_klots()
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

        self.klots = self.teeUusKlots()
        self.järgmineKlots = self.teeUusKlots()
        print(self.klots)
        print(self.järgmineKlots)


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

