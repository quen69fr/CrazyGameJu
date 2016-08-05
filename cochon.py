# -*- coding: utf-8 -*-
__author__ = 'Juliette , Manu'

from outils import *

class Cochon():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.image = IMAGE_COCHON
        self.rayon = int(self.image.get_width()/2)

    def afficher(self, screen):
           screen.blit(self.image,(self.x,self.y))
