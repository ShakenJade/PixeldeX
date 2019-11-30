import pygame
Reso = (600,600)

pygame.init()
launche = True

pygame.display.set_caption("SgCsF")
Wind = pygame.display.set_mode(Reso)

EntityImg = pygame.image.load("Entity.png")
SuGr = (64,64,64)

Wind.fill(SuGr)
EntityImg = pygame.transform.scale(EntityImg,(40,40))

R = EntityImg.get_rect()
rect = R.move((0,0))

x = 0
while launche:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launche = False
            
    Wind.fill(SuGr)
    x += 1

    EntityImg = pygame.transform.scale(EntityImg,(40+x,40+x))
    Wind.blit(EntityImg,rect)
    
    pygame.display.flip()
pygame.quit
