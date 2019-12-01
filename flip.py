import pygame
Reso = (600,600)

pygame.init()
launche = True

pygame.display.set_caption("SgCsF")
Wind = pygame.display.set_mode(Reso)

EntityImg = pygame.image.load("Entity1.png")
SuGr = (64,64,64)

Wind.fill(SuGr)
EntityImg = pygame.transform.scale(EntityImg,(300,300))

EntityImg = pygame.transform.flip(EntityImg,True,False)
#EntityImg = pygame.transform.rotate(EntityImg,70)

R = EntityImg.get_rect()
rect = R.move((0,0))

while launche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launche = False
            
    Wind.fill(SuGr)
    x = 300

    Wind.blit(EntityImg,rect)
    pygame.display.flip()
