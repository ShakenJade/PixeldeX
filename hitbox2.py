import pygame
Reso = (600,600)

pygame.init()
launche = True

pygame.display.set_caption("hitbox_test")
Wind = pygame.display.set_mode(Reso)

Img1 = pygame.image.load("Img1.png")
Img2 = pygame.image.load("Img2.png")
Img3 = pygame.image.load("Img3.png")
Img4 = pygame.image.load("Img4.png")

SuGr = (64,64,64)
Wind.fill(SuGr)

coord1 = ((0,0))
coord2 = ((110,0))

#rect1 = R1.move((0,0))

"""
-importation de l'image
-creation de variables de coordonnée
-changement de positions de l'image a partir des variables
-affichage de l'image a partir des variables de deplacements
-creation du rect a partir de l'image
"""
while launche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launche = False
            
    Wind.fill(SuGr)
    Wind.blit(Img1,coord1)
    
    Wind.blit(Img2,coord2)
    R1 = Img1.get_rect()
    R2 = Img2.get_rect()
    pygame.display.flip()
    print(R2.colliderect(R1))
    try:
        pygame.image.save(Wind, "screenshot.jpeg")
    except:
        print("save done")
