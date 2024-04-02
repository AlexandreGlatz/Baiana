import pygame
import sys

pygame.init()

taille_fenetre = (800, 600)
ecran = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption('saut mdrr ca rebondit')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

position_joueur = [400, 500]
vitesse_saut = -20
gravite = 1
en_saut = False
vitesse_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not en_saut:
                en_saut = True
                vitesse_y = vitesse_saut

    if en_saut:
        position_joueur[1] += vitesse_y
        vitesse_y += gravite

        if position_joueur[1] > 500:
            position_joueur[1] = 500
            en_saut = False
            vitesse_y = 0

    ecran.fill(BLACK)
    pygame.draw.rect(ecran, WHITE, (*position_joueur, 50, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
