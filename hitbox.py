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

R1 = Img1.get_rect()
R2 = Img2.get_rect()
R3 = Img3.get_rect()
R4 = Img4.get_rect()
rect1 = R1.move((0,0))
rect2 = R2.move((110,0))
rect3 = R3.move((10,70))
rect4 = R4.move((60,60))

print(R2.colliderect(R1))
"""
-importation de l'image
-creation du rect a partir de l'image
-creation de variable de positions
-affichage de l'image a partir des variables de deplacements
-transformation du screen en image
"""
while launche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launche = False
            
    Wind.fill(SuGr)
    Wind.blit(Img1,rect1)
    
    Wind.blit(Img2,rect2)
    Wind.blit(Img3,rect3)
    Wind.blit(Img4,rect4)
    pygame.display.flip()
    print(bool(R2.colliderect(R1)))
    try:
        pygame.image.save(Wind, "screenshot.jpeg")
    except:
        print("save done")
