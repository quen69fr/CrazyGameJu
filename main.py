# -*- coding: utf-8 -*-
__author__ = 'Juliette , Manu'

from outils import *
from bird import *
from elastique import *
from cochon import *
import os


if __name__=="__main__":

    x = 100
    y = 50

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    pygame.init()
    pygame.display.set_caption("Crazy Game !")
    SCREEN = pygame.display.set_mode((LARGEUR, HAUTEUR))




    listeBird = []
    for i in range(5):
        bird = Bird(20,450-60*i,0,0,i+1)
        listeBird.append(bird)

    elast = Elastique()

    listeCochon = []
    for i in range(5):
        cochon = Cochon(1000+60*i,Y_SOL-50)
        listeCochon.append(cochon)


    numBirdEnCours = -1
    birdEnCours = None


    #listeBird = [bird,bird2,bird3,bird4,bird5]

    bouton_souris_appuye = 0

    x_souris = 0
    y_souris = 0

    while True:

        for event in pygame.event.get():
            #print (event)

            # un clic sur le X de fermeture de fenetre ?
            if event.type==pygame.QUIT:
                    pygame.quit()
                    exit(0)

            if event.type==pygame.KEYDOWN:
                #print(event.key)

                # Q
                if event.key==97:
                    pygame.quit()
                    exit(0)

                #espace
                if event.key==32:
                    if numBirdEnCours<len(listeBird)-1:
                        if birdEnCours==None or birdEnCours.etat!=BIRD_ETAT_ELASTIQUE:
                            numBirdEnCours = numBirdEnCours+1
                            birdEnCours = listeBird[numBirdEnCours]
                            birdEnCours.mettreElastique(elast)



            souris = pygame.mouse.get_pos()
            x_souris = souris[0]
            y_souris = souris[1]


            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                bouton_souris_appuye = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                bouton_souris_appuye = 0





        #SCREEN.fill(0)
        SCREEN.blit(IMAGE_FOND,(0,0))
        elast.afficher(SCREEN)
        SCREEN.blit(IMAGE_FRONDE,(X_ATTACHE_ELASTIQUE_1-10,Y_SOL-IMAGE_FRONDE.get_height()))
        SCREEN.blit(IMAGE_ANGRY_BIRD,(400,50))
        SCREEN.blit(IMAGE_AUTEURS,(1170,60))
        SCREEN.blit(IMAGE_BIGBIRD,(1250,50))

        # on regarde si un oiseau touche un cochon
        for monCochon in listeCochon:
            for monBird in listeBird:
                if intersection(monCochon,monBird):
                    listeCochon.remove(monCochon)
                    print("cool")



        for monCochon in listeCochon:
            monCochon.afficher(SCREEN)
        for monBird in listeBird:
            monBird.afficher(SCREEN)
            monBird.deplacer()
        if x_souris>0 and y_souris>0 and bouton_souris_appuye==1:
            elast.tirer(x_souris,y_souris)
        else:
            if elast.estAuRepos() and birdEnCours!=None:
                if birdEnCours.etat==BIRD_ETAT_ELASTIQUE and (elast.vitesse_lancement_x!=0 or elast.vitesse_lancement_y!=0):
                    birdEnCours.lancer(elast.vitesse_lancement_x,elast.vitesse_lancement_y)
                    elast.vitesse_lancement_x = 0
                    elast.vitesse_lancement_y = 0
            else:
                elast.lacher()

        pygame.display.update()
        pygame.time.Clock().tick(FPS)
