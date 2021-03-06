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
        self.väikefont = pygame.font.SysFont("monospace", 10)
        self.suurfont = pygame.font.SysFont("monospace", 100)
        self.pööre = 0
        self.loonimi = 0
        self.skoorid = [0, 100, 300, 600, 1000]


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

        klots = 0
        kuju = choice(list(self.shapes.keys()))
        klots = {"kuju": kuju,
                 "asend": self.shapes[kuju][0],
                 "x": self.algnex,
                 "y": self.algney,
                 "värv": self.võta_värv(kuju)}

        return klots


    def lisaKlotsMaatriksisse(self):
        koordinaat = False
        for self.y in range(4):
            for self.x in range(4):
                koordinaat = self.klots["asend"][self.y][self.x]
                if koordinaat != 0:
                    self.maatriks[self.y + self.klots["y"]][self.x + self.klots["x"]] = self.klots["värv"]


    def on_täis_rida(self, rida):
        for element in range(1, 11):
            if self.maatriks[rida][element] == 0:
                return False
        return True

    def kontrolli_ridu(self):
        eemald_ridu = 0
        y = 21
        while y >= 0:
            if self.on_täis_rida(y):
                for nihuta_alla_y in range(y, 0, -1):
                    for x in range(1, 11):
                        self.maatriks[nihuta_alla_y][x] = self.maatriks[nihuta_alla_y - 1][x]
                for x in range(1, 11):
                    self.maatriks[0][x] = 0
                eemald_ridu += 1
            else:
                y -= 1

        self.skoor += self.skoorid[eemald_ridu]
        self.kiirus = 15 - int(self.skoor/1000)



    def joonista_maatriks(self):
        j = 0

        for rida in self.maatriks:
            i = 0

            for element in rida:
                if element == 'äär':
                    "something"

                elif element != 0:
                    self.aken.blit(element, (220 + (i * 30), 20 + (j * 30)))
                i += 1
            j +=  1


    def pööra_klots(self):
        self.kustutaeelmine()
        self.pööre += 1
        self.is_valid_position()
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
        self.is_valid_position()

        if not self.vaja_uus_klots and not self.äärPõhi:
            self.kustutaeelmine()

        if suund == ("alla"):
            if not self.äärPõhi:
                self.klots["y"] += 1

        if suund == ("paremale"):
            if not self.äärP:
                self.klots["x"] += 1

        if suund == ("vasakule"):
            if not self.äärV:
                self.klots["x"] -= 1

        self.äärP = False
        self.äärV = False
        self.äärPõhi = False
        self.eelmine = self.klots

    #Don't look..
    def is_valid_position(self):
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


    def näita_teksti(self, tekst, tekst2 = ""):
        pause = self.suurfont.render(tekst, 1, (255, 255, 255))
        unpause = self.font.render(tekst2, 1, (255, 255, 255))
        self.aken.blit(pause, (200, 350))
        self.aken.blit(unpause, (270, 450))
        lõpp = False
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_p:
                        lõpp = True
                        break

            if lõpp == True:
                break
            pygame.display.update()
            self.fpsClock.tick()


    def nupuvajutus(self, nupp):
        if nupp == K_ESCAPE:
            pygame.event.post(pygame.event.Event(QUIT))
            #Väljub programmist

        if nupp == K_p:
            pygame.mixer.music.pause()
            self.aken.fill(pygame.Color(0, 0, 0))
            self.näita_teksti("Paused", "Jätkamiseks vajuta P")
            pygame.mixer.music.unpause()
        if nupp == K_LEFT:
            self.liigutaplokk("vasakule")

        if nupp == K_RIGHT:
            self.liigutaplokk("paremale")

        if nupp == K_DOWN:
            self.liigutaplokk("alla")

        if nupp == K_UP:
            self.pööra_klots()

        if nupp == K_n:
            eelmine = self.loonimi
            self.loonimi = choice(self.nimed)
            while eelmine == self.loonimi:
                self.loonimi = choice(self.nimed)
            pygame.mixer.music.fadeout(100)
            pygame.mixer.music.load(os.path.join('andmed', self.loonimi))
            pygame.mixer.music.play(0, 0.0)


    def joonista(self):
        self.aken.blit(self.taust, (0,0))

        if self.i == self.kiirus:
            self.liigutaplokk("alla")
            self.i = 0

        if self.vaja_uus_klots:
            self.klots = self.järgmineKlots
            self.järgmineKlots = self.teeUusKlots()
            self.eelmine = self.klots
            self.kontrolli_ridu()
            self.vaja_uus_klots = False


        if self.klots["x"] == self.algnex and self.klots["y"] == self.algney:
            self.is_valid_position()
            if self.äärPõhi:
                self.aken.fill(pygame.Color(0, 0, 0))
                self.näita_teksti("Game over!", "Väljumiseks vajuta ESC")


        self.lisaKlotsMaatriksisse()
        self.joonista_maatriks()
        self.joonista_järgmine_klots()
        self.i += 1

        järgminetekst = self.font.render("Järgmine plokk", 1, (255, 255, 255))
        self.aken.blit(järgminetekst, (45, 200))

        skoor = self.font.render("Skoor = " + str(self.skoor), 1, (255, 255, 255))
        self.aken.blit(skoor, (70, 360))

        loonimetekst = self.font.render(self.loonimi, 1, (255, 255, 255))
        self.aken.blit(loonimetekst, (1, 1))

        ülestekst = self.väikefont.render("Üles nool: pööra klotsi", 1, (255, 255, 255))
        self.aken.blit(ülestekst, (555, 260))

        allatekst = self.väikefont.render("Alla nool: kiirenda kukkumist", 1, (255, 255, 255))
        self.aken.blit(allatekst, (555, 240))

        vasakuletekst = self.väikefont.render("Vasakule nool: liiguta klotsi vasakule", 1, (255, 255, 255))
        self.aken.blit(vasakuletekst, (555, 220))

        paremaletekst = self.väikefont.render("Paremale nool: liiguta klotsi paremale", 1, (255, 255, 255))
        self.aken.blit(paremaletekst, (555, 200))

        Ntekst = self.väikefont.render("N Täht: järgmine lugu", 1, (255, 255, 255))
        self.aken.blit(Ntekst, (555, 320))

        pausetekst = self.väikefont.render("P Nupp: pause", 1, (255, 255, 255))
        self.aken.blit(pausetekst, (555, 280))

        exittekst = self.väikefont.render("ESC Nupp: välju programmist", 1, (255, 255, 255))
        self.aken.blit(exittekst, (555, 300))


    def muusika(self):
        self.nimed = []
        self.nimed.append("Doctor P - Tetris.ogg")
        self.nimed.append("Smooth McGroove - Theme 'A' Acapella.ogg")
        self.nimed.append("Smooth McGroove - Theme 'B' Acapella.ogg")
        self.nimed.append("Tetris A Original.ogg")
        self.nimed.append("BassHunter - Tetris.ogg")
        self.nimed.append("London Philharmonic Orchestra and Andrew Skeet -  Tetris Theme.ogg")
        self.nimed.append("DaCav5 - Tetris.ogg")
        self.loonimi = choice(self.nimed)

        pygame.mixer.music.load(os.path.join('andmed', self.loonimi))
        pygame.mixer.music.play(-1, 0.0)


    def põhikordus(self):
        self.muusika()
        self.tühiplats()
        self.klots = self.teeUusKlots()
        self.järgmineKlots = self.teeUusKlots()
        self.eelmine = self.klots
        pygame.key.set_repeat(150, 50)

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

