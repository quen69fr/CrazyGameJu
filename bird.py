# -*- coding: utf-8 -*-
__author__ = 'Juliette , Manu'

from outils import *

class Bird():

    def __init__(self,x,y,vx,vy,type):
        self.x = x
        self.y = y
        self.type = type
        self.vitesse_x = vx
        self.vitesse_y = vy

        self.etat = BIRD_ETAT_ATTENTE

        if type == 2:
            self.image = IMAGE_BIRD2
        elif type == 3:
            self.image = IMAGE_BIRD3
        elif type == 4:
            self.image = IMAGE_BIRD4
        elif type == 5:
            self.image = IMAGE_BIRD5
        else:
            self.image = IMAGE_BIRD1

        self.hauteur = self.image.get_height()
        self.largeur = self.image.get_width()
        self.rayon = int(self.largeur/2)


    def afficher(self, screen):
        screen.blit(self.image,(self.x,self.y))


    def lancer(self,vx,vy):
        self.etat = BIRD_ETAT_LIBRE
        self.vitesse_x=vx
        self.vitesse_y=vy

    def mettreElastique(self,elastique):
        self.etat=BIRD_ETAT_ELASTIQUE
        self.elastique = elastique


    def deplacer(self):
        if self.etat==BIRD_ETAT_LIBRE:
            if self.y+self.hauteur <= Y_SOL:
                self.x = self.x+self.vitesse_x
                self.y = self.y+self.vitesse_y
                self.vitesse_y=self.vitesse_y + GRAVITE
            else:
                if self.vitesse_y>V_MIN:
                    self.vitesse_y = -self.vitesse_y/3
                    self.y = Y_SOL-self.hauteur
                else:
                    self.vitesse_y = 0
                if self.vitesse_x>V_MIN:
                    self.vitesse_x = self.vitesse_x/3
                else:
                    self.vitesse_x = 0
        elif self.etat==BIRD_ETAT_ELASTIQUE:
            self.x = self.elastique.x - self.largeur + 35
            self.y = self.elastique.y - self.hauteur + 20


