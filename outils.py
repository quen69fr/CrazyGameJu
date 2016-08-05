# -*- coding: utf-8 -*-
__author__ = 'Juliette , Manu'

import pygame
import math

# SCREEN sera une "surface de dessin"
LARGEUR = 1400
HAUTEUR = 800

FPS = 60                 # nombre d'image par seconde
DELAY = 1               # vitesse du jeu

NOIR =  (  0,   0,   0)
BLANC = (255, 255, 255)
BLEU =  (  0,   0, 255)
VERT =  (  0, 255,   0)
ROUGE = (255,   0,   0)
JAUNE = (255, 255,   0)

GRAVITE = 0.40
Y_SOL = 780
V_MIN = 1

BIRD_ETAT_ATTENTE = 0
BIRD_ETAT_ELASTIQUE = 1
BIRD_ETAT_LIBRE = 2



# tous les fichiets IMAGES
IMAGE_BIRD1 = pygame.image.load("images/bird1.gif")
IMAGE_BIRD2 = pygame.image.load("images/bird2.gif")
IMAGE_BIRD3 = pygame.image.load("images/bird3.gif")
IMAGE_BIRD4 = pygame.image.load("images/bird4.gif")
IMAGE_BIRD5 = pygame.image.load("images/bird5.gif")
IMAGE_FRONDE = pygame.image.load("images/fronde.gif")
IMAGE_FOND = pygame.image.load("images/fond.png")
IMAGE_COCHON = pygame.image.load("images/cochon.png")
IMAGE_ANGRY_BIRD = pygame.image.load("images/angry_bird.png")
IMAGE_AUTEURS =  pygame.image.load("images/auteur.png")
IMAGE_BIGBIRD = pygame.image.load("images/bigbird.png")

X_ATTACHE_ELASTIQUE_1 = 243
Y_ATTACHE_ELASTIQUE_1 = Y_SOL-175

X_ATTACHE_ELASTIQUE_2 = X_ATTACHE_ELASTIQUE_1+52
Y_ATTACHE_ELASTIQUE_2 = Y_ATTACHE_ELASTIQUE_1+5

X_ELASTIQUE_REPOS = (X_ATTACHE_ELASTIQUE_1+X_ATTACHE_ELASTIQUE_2)/2
Y_ELASTIQUE_REPOS = (Y_ATTACHE_ELASTIQUE_1+Y_ATTACHE_ELASTIQUE_2)/2+10

K_ELASTIQUE = 0.15




def intersection(objet1,objet2):
    '''
    :param objet1: doit contenir des attributs (x,y) du coin en haut à gauche et rayon
    :param objet2: doit contenir des attributs (x,y) du coin en haut à gauche et rayon
    :return: Réponds True si les objets se croisent.
    '''
    r1 = objet1.rayon
    r2 = objet2.rayon
    x1 = objet1.x
    x2 = objet2.x
    y1 = objet1.y
    y2 = objet2.y

    distance = math.sqrt( (x1+r1-x2-r2)**2 + (y1+r1-y2-r2)**2 )
    if distance <= r1+r2:
        return True
    else:
        return False
