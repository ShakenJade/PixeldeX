"""
12/11/2019
premiere version de l'import general
deve : Mahli
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources fichiers, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'eviter et de cibler les problemes qui pourraient-etre liés a
tel ou tel import.
"""
def Fpx1211importGeneral():
    try:
        import sys
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module sys")
    try:
        import random
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module random")
            metaD = "fail"
    try:
        import math
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module math")
            metaD = "fail"
    try:
        import os
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module os")
            metaD = "fail"
    try:
        import getopt
        metaD = "succes"
    except ImportError:  
            print("Impossible de charger le module getopt")
            metaD = "fail"
    try:          
        import pygame
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module pygame")
            metaD = "fail"
    try:          
        import numpy as np
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module numpy")
            metaD = "fail"
    try:          
        import simpleaudio as sa
        metaD = "succes"
    except ImportError:
            print("Impossible de charger le module simpleaudio")
            metaD = "fail"
    return metaD
"""
24/01/2020
premiere version de Saundoefekuto litteralement bruitage.
deve : Mahli,Cloe
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources fichiers audio, qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'eviter et de cibler les problemes qui pourraient-etre liés a
tel ou tel selection de son puis de le jouer en stereo avec le volume donné.
NB:ne prend en compte que les fichier .wav.
Il est recommander de n'utiliser cette fonction que pour les objets d'environnements.
Cette fonction ne fonctionne que si le mixer a été initialiser avec 2 channels.
"""
def Fpx2401Saundoefekuto(name,,vX,vY):
    soundFx = pygame.mixer.Sound(str(name)+'.wav')
    channelFx = soundFx.play()
    if vX > 1:
        vX = 1
    else:
        vX = vX
    if vY > 1:
        vY = 1
    else:
        vY = vY
    try:
        channel.set_volume(vX, vY)
        MetaD = ["succes"]
    except AttributeError:
        MetaD = ["succes","attribut error"]
"""
17/01/2020
premiere version de variablesStatic
deve : Mahli
concu initialement pour l'architecture general c'est fonction est une fonction
de gestion des ressources statique , qui ne prend que tres peux sur le cpu et le
gpu.
Elle a pour but d'englober des variables qui serront utiliser par tous les deves.
"""
def Fpx1701variablesStatics():
    pi = np.pi
"""
12/11/2019
premiere version de loadImages
deve : Mahli
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type gestion des ressources fichiers,
car n'affiche rien.
Pour l'instant ne prend en charge que les .png car possedent une opacitée , elle
traduit neanmoins tout arguments en str.
Elle a pour but d'avoir une meilleur gestion et traduction que celle des
librairies pygames.
notes:Dans de futures versions il est prevu de rajouter des options de gestion de
taille , de post-traitements , de rotations par fonctions surcharger.
"""
def Fpx1211loadImages(acces):
    try:
        img = pygame.image.load(str(acces+".png"))
        metaD = ["succes"]
    except pygame.error:
        img = "error"
        metaD = ["fail"]
        print("impossible de charger l'image png",str(acces))
    return img , metaD
"""
12/11/2019
2e version de loadImages
deve : Mahli
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type gestion des ressources fichiers,
car n'affiche rien.
Pour l'instant ne prend en charge que les .png car possedent une opacitée , elle
traduit neanmoins tout arguments en str.
Elle a pour but d'avoir une meilleur gestion et traduction que celle des
librairies pygames.
notes:Dans de futures versions il est prevu de rajouter des options de post-traitements.
"""
def Fpx0401loadImages(acces,scale):
    try:
        img = pygame.image.load(str(acces+".png"))
        if scale[0] == 0 or scale[1] == 0:
            img = img
            metaD = ["succes"]
        else:
            img = pygame.transform.scale(img,(scale[0],scale[1]))
            metaD = ["succes",str(scale)]
    except pygame.error:
        img = "error"
        metaD = ["fail"]
        print("impossible de charger l'image png",str(acces))
    return img , metaD
"""
12/11/2019
premiere version de createWindow
deve : Mahli
concu initialement pour l'architecture grapique d'un niveau d'abstraction bas.
c'est fonction est une fonction de type graphique.
Pour l'instant ne permet de creer que 2 types de fenetres.
Elle a pour but d'avoir une meilleur gestion de la creation de fenetres.
notes:dans de futures versions il serra possible d'y isserrer des images dans le titres.
"""
def Gpx1211createWindow(typeW,H,L,titl):
    if typeW == "F"or "f":
        Wind =pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        metaD = [("fullscreen" , "title="+str(titl))]
    else:
        Wind =pygame.display.set_mode((L,H))
        metaD = [(str(L) , "x" , str(H) , "title="+str(titl))]
    pygame.dysplay.set_caption(str(titl))
    return Wind,metaD
"""
Saundoefekuto
"""
class Phiggs:
    def __init__(self):
        return 0
    def pi():
        return 3.14
    pi = staticmethod(pi)
    
    
