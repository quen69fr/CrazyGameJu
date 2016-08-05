# -*- coding: utf-8 -*-
__author__ = 'Juliette , Manu'

from outils import *

class Elastique ():
    def __init__(self):
        self.x = X_ELASTIQUE_REPOS
        self.y = Y_ELASTIQUE_REPOS
        self.vitesse_lancement_x = 0
        self.vitesse_lancement_y = 0

    def afficher(self, screen):
        pygame.draw.line(screen,NOIR,[X_ATTACHE_ELASTIQUE_1,Y_ATTACHE_ELASTIQUE_1],[self.x,self.y],11)
        pygame.draw.line(screen,NOIR,[X_ATTACHE_ELASTIQUE_2,Y_ATTACHE_ELASTIQUE_2],[self.x,self.y],11)

    def tirer(self,x_tir,y_tir):
        self.x = x_tir
        self.y = y_tir
        self.vitesse_lancement_x = 0
        self.vitesse_lancement_y = 0

    def lacher(self):
        if (self.x==X_ELASTIQUE_REPOS and self.y==Y_ELASTIQUE_REPOS):
            pass
        else:
            if self.vitesse_lancement_x!=0 or self.vitesse_lancement_y!=0:
                # on a déjà calculé la vitesse de lancement
                pass
            else:
                # on doit calculer la vitesse de lancement
                self.vitesse_lancement_x = (X_ELASTIQUE_REPOS-self.x)*K_ELASTIQUE
                self.vitesse_lancement_y = (Y_ELASTIQUE_REPOS-self.y)*K_ELASTIQUE
                print("vx",self.vitesse_lancement_x,"vy",self.vitesse_lancement_y)


            if abs(X_ELASTIQUE_REPOS-self.x)>abs(self.vitesse_lancement_x):
                self.x = self.x+self.vitesse_lancement_x
            else:
                self.x=X_ELASTIQUE_REPOS



            if abs(Y_ELASTIQUE_REPOS-self.y)>abs(self.vitesse_lancement_y):
                self.y = self.y+self.vitesse_lancement_y
            else:
                self.y=Y_ELASTIQUE_REPOS

    def estAuRepos(self):
        return (self.x==X_ELASTIQUE_REPOS and self.y==Y_ELASTIQUE_REPOS)




