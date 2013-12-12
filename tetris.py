import os
import sys
import pygame
from pygame.locals import *
from random import *


class TetrisPõhi:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Helari ja Karli Tetrise projekt ULTRA POWERFUL EXTREME EDITION 2000")
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
        self.kollane = pygame.image.load(os.path.join("andmed", "kollane.png"))
        self.roheline = pygame.image.load(os.path.join("andmed", "roheline.png"))
        self.roosa = pygame.image.load(os.path.join("andmed", "roosa.png"))
        self.oranz = pygame.image.load(os.path.join("andmed", "oranz.png"))
        self.helesinine = pygame.image.load(os.path.join("andmed", "helesinine.png"))
        self.hall = pygame.image.load(os.path.join("andmed", "hall.png"))
        self.must = pygame.image.load(os.path.join("andmed", "must.png"))
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
        self.eelmine = 0
        self.font = pygame.font.SysFont("monospace", 20)
        self.pööre = 0


        #kõik klotside kujud ja nende asendid
        self.O_shape = [[(1, 1, 0, 0),
                    (1, 1, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.I_shape = [[(1, 1, 1, 1),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(1, 0, 0, 0),
                    (1, 0, 0, 0),
                    (1, 0, 0, 0),
                    (1, 0, 0, 0)]]

        self.S_shape = [[(0, 1, 1, 0),
                    (1, 1, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(1, 0, 0, 0),
                    (1, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)]]

        self.Z_shape = [[(1, 1, 0, 0),
                    (0, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (1, 1, 0, 0),
                    (1, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.J_shape = [[(1, 0, 0, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                        #äärt ei taju
                   [(1, 1, 0, 0),
                    (1, 0, 0, 0),
                    (1, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (1, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(1, 1, 1, 0),
                    (0, 0, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.L_shape = [[(1, 1, 1, 0),
                    (1, 0, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(1, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(1, 0, 0, 0),
                    (1, 0, 0, 0),
                    (1, 1, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 0, 1, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.T_shape = [[(1, 1, 1, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (1, 1, 0, 0),
                    (0, 1, 0, 0),
                    (0, 0, 0, 0)],
                   #äärt ei taju
                   [(1, 0, 0, 0),
                    (1, 1, 0, 0),
                    (1, 0, 0, 0),
                    (0, 0, 0, 0)],
                   [(0, 1, 0, 0),
                    (1, 1, 1, 0),
                    (0, 0, 0, 0),
                    (0, 0, 0, 0)]]

        self.shapes = {
                  "O": self.O_shape,
                  "I": self.I_shape,
                  "S": self.S_shape,
                  "Z": self.Z_shape,
                  "J": self.J_shape,
                  "L": self.L_shape,
                  "T": self.T_shape
                }

    def tühiplats(self):
        for i in range(22):
            rida = []
            for j in range(12):
                rida.append(0)
            self.maatriks.append(rida)
        for rida in self.maatriks:
            rida[0] = 'äär'
            rida[-1] = 'äär'
        self.maatriks.append(['äär', 'äär', 'äär', 'äär', 'äär', 'äär', 'äär', 'äär', 'äär', 'äär', 'äär', 'äär'])
        #print(self.maatriks)
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
        for self.y in range(4):
            for self.x in range(4):
                #print(self.klots)
                koordinaat = self.klots["asend"][self.y][self.x]
                #print(koordinaat)
                #print(self.klots["asend"][y][x])
                #print(self.shapes[self.klots["kuju"]][koordinaadid])
                #print(self.klots["x"])
                #print(self.klots["y"])
                if koordinaat != 0:
                    self.maatriks[self.y + self.klots["y"]][self.x + self.klots["x"]] = self.klots["värv"]

        #kui klots paika saab, lisatakse maatriksisse
        #tuleb gameloopis kusagil välja kutsuda!

    def on_täis_rida(self, rida):
        for element in range(10):
            if self.maatriks[rida][element] == 0:
                return False

        return True

    def kontrolli_ridu(self):
        """arv = 0
        for rida in range(22):
            arv = 0
            for element in range(10):
                 if self.maatriks[rida][element] != 0:
                     arv += 1
            if arv == 10:
                print("something something")
                self.skoor += 100
                for abi in range(rida-1, 0, -1):
                    self.maatriks[rida] = self.maatriks[rida-1]"""

        eemald_ridu = 0
        y = 21
        while y >= 0:
            if self.on_täis_rida(y):
                for nihuta_alla_y in range(y, 0, -1):
                    for x in range(10):
                        self.maatriks[nihuta_alla_y][x] = self.maatriks[nihuta_alla_y - 1][x]
                for x in range(10):
                    self.maatriks[0][x] = 0
                eemald_ridu += 1
            else:
                y -= 1

        self.skoor += eemald_ridu * 100


    def joonista_maatriks(self):
        #teised klotsid ka vaja lisada
        #print(self.maatriks)

        j = 0
        for rida in self.maatriks:
            #print(rida)
            i = 0
            arv = 0
            for element in rida:
                if element == 'äär':
                    self.aken.blit(self.must, (250 + (i * 30), 20 + (j * 30)))

                elif element != 0:

                    self.aken.blit(element, (250 + (i * 30), 20 + (j * 30)))
                if element == 0:  #Temporary, maatriksi sisu näitamiseks
                    self.aken.blit(self.hall, (250 + (i * 30), 20 + (j * 30)))
                i += 1
            j +=  1

    def pööra_klots(self):
        self.kustutaeelmine()
        self.pööre += 1
        self.is_valid_position()
        print(self.äärV)
        print(self.äärP)
        if not self.äärV and not self.äärP and not self.äärPõhi:
            try:
                self.klots["asend"] = self.shapes[self.klots["kuju"]][self.pööre]
            except IndexError:
                self.pööre = 0
                self.klots["asend"] = self.shapes[self.klots["kuju"]][self.pööre]
        else:
            self.pööre -= 1
            self.klots["asend"] = self.shapes[self.klots["kuju"]][self.pööre]

    def joonista_järgmine_klots(self):
        #klotside algseid asenedid tuleb muuta et normaalsem oleks
        j = 0
        for self.y in range(4):
            i = 0
            for self.x in range(4):
                koordinaat = self.järgmineKlots["asend"][self.y][self.x]
                if koordinaat != 0:
                    self.aken.blit(self.järgmineKlots["värv"], (65 + (i * 30), 260 + (j * 30)))
                i += 1
            j += 1

    def kustutaeelmine(self):
        for self.y in range(4):
            for self.x in range(4):
                koordinaat = self.eelmine["asend"][self.y][self.x]
                if koordinaat != 0:
                    self.maatriks[self.y + self.eelmine["y"]][self.x + self.eelmine["x"]] = 0

    def liigutaplokk(self, suund):
        #vaja muuta et liigutaks kõiki klotse, mitte ainult kuupi


        self.is_valid_position()

        if not self.vaja_uus_klots or (self.x == self.algnex and self.y == self.algney):
            self.kustutaeelmine()



        if suund == ("alla"):
            if not self.äärPõhi:
                self.klots["y"] += 1
                #self.maatriks[self.klots["x"]]

        if suund == ("paremale"):
            if not self.äärP and not self.äärPõhi:
                self.klots["x"] += 1

        if suund == ("vasakule"):
            if not self.äärV and not self.äärPõhi:
                self.klots["x"] -= 1

        #self.lisaKlotsMaatriksisse()
        self.äärP = False
        self.äärV = False
        self.äärPõhi = False
        self.eelmine = self.klots


    def is_valid_position(self):
        #a = True

        #kontrollib kas vasak äär
        #kontrollib kas parem äär
        #kontrollib kas seal juba on klots

        if self.klots["kuju"] == "O":
            if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                self.äärP = True
            if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                self.äärV = True
            if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                self.äärP = True
            if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                self.äärV = True
            if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                self.äärPõhi = True
                self.vaja_uus_klots = True
            if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                self.äärPõhi = True
                self.vaja_uus_klots = True





        elif self.klots["kuju"] == "I":
            if self.klots["asend"] == self.shapes["I"][0]:
                #print("adjfholw")
                if self.maatriks[self.klots["y"]][self.klots["x"]+4] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+3] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["I"][1]:
                #print("saaaa")
                if self.maatriks[self.klots["y"]][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+4][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True



        elif self.klots["kuju"] == "S":
            if self.klots["asend"] == self.shapes["S"][0]:
                #print("siii")
                if self.maatriks[self.klots["y"]][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True



            elif self.klots["asend"] == self.shapes["S"][1]:
                #print("mooooooo")
                if self.maatriks[self.klots["y"]][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True


        elif self.klots["kuju"] == "Z":
            if self.klots["asend"] == self.shapes["Z"][0]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["Z"][1]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True


        elif self.klots["kuju"] == "L":
            if self.klots["asend"] == self.shapes["L"][0]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["L"][1]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["L"][2]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["L"][3]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]+1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True



        elif self.klots["kuju"] == "J":
            if self.klots["asend"] == self.shapes["J"][0]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["J"][1]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["J"][2]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["J"][3]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True


        elif self.klots["kuju"] == "T":
            if self.klots["asend"] == self.shapes["T"][0]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["T"][1]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["T"][2]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+1] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+3][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

            elif self.klots["asend"] == self.shapes["T"][3]:
                if self.maatriks[self.klots["y"]][self.klots["x"]+2] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]][self.klots["x"]] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]+3] != 0:
                    self.äärP = True
                if self.maatriks[self.klots["y"]+1][self.klots["x"]-1] != 0:
                    self.äärV = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+1] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True
                if self.maatriks[self.klots["y"]+2][self.klots["x"]+2] != 0:
                    self.äärPõhi = True
                    self.vaja_uus_klots = True

    def tee_tekst(self, tekst, font, värv):
        pind = font.render(tekst, True, värv)
        return pind, pind.get_rect()


    def näita_teksti(self, tekst):
            teksti_pind, teksti_kast = self.tee_tekst(tekst, pygame.font.Font("freesansbold.ttf", 100), self.oranz)
            teksti_kast.center = (400, 350)
            pygame.display.blit(teksti_pind, teksti_kast)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    while event.key == K_ESCAPE:
                        pygame.display.update()
                        self.fpsClock.tick()

    def nupuvajutus(self, nupp):  #abifunktsioon nupuvajutuste kontrolliks
        if nupp == K_ESCAPE:
            #pygame.event.post(pygame.event.Event(QUIT))
            #Väljub programmist
            #not anymore

            self.aken.fill(pygame.Color(0, 0, 0))
            #pygame.music.stop()
            #pausi kood:
            self.näita_teksti("Paused")

            #edasi kood:
            self.muusika()

        if nupp == K_LEFT:
            self.liigutaplokk("vasakule")
        if nupp == K_RIGHT:
            self.liigutaplokk("paremale")
        if nupp == K_DOWN:

            self.liigutaplokk("alla")
        if nupp == K_UP:
            self.pööra_klots()


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
            self.eelmine = self.klots
            #print(self.järgmineKlots)
            self.kontrolli_ridu()
            self.vaja_uus_klots = False
        self.lisaKlotsMaatriksisse()
        self.joonista_maatriks()
        self.joonista_järgmine_klots()
        self.i += 1

        järgminetekst = self.font.render("Järgmine plokk", 20, (255, 255, 255))
        self.aken.blit(järgminetekst, (45, 200))
        skoor = self.font.render("Skoor = " + str(self.skoor), 1, (255, 255, 255))
        self.aken.blit(skoor, (70, 360))

    def muusika(self):
        nimed = []
        nimed.append( 'tetrisA.mp3')
        nimed.append("Tetris - Theme 'A' Acapella.mp3")
        nimed.append("Tetris - Theme 'B' Acapella.mp3")
        pygame.mixer.music.load(os.path.join('andmed', choice(nimed)))
        pygame.mixer.music.play(-1, 1.0)
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
        self.eelmine = self.klots
        #print(self.klots)
        #print(self.järgmineKlots)
        pygame.key.set_repeat(50, 50)

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

