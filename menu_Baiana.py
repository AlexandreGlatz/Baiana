import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Résolution par défaut
WIDTH, HEIGHT = 1920, 1080

# Récupération de la taille de l'écran
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

# Utilisation de la résolution de l'écran pour le plein écran
FULLSCREEN_SIZE = (1920, 1080)

# Classe pour l'arrière-plan
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# Initialisation de l'arrière-plan
BackGround = Background('menu_principal.png', [0,0])

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuration de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Pygame")

# Charger les images des boutons
title_img = pygame.image.load("episode_1_baiana.png")
chapitres_button_img = pygame.image.load("_chapitres.png")
quitter_button_img = pygame.image.load("_retour_au_bureau.png")
retour_button_img = pygame.image.load("_retour.png")
chapitre1_img = pygame.image.load("_chapitre_1.png")
chapitre2_img = pygame.image.load("_chapitre_2.png")
chapitre3_img = pygame.image.load("_chapitre_3.png")
chapitre4_img = pygame.image.load("_chapitre_4.png")
chapitre5_img = pygame.image.load("_chapitre_5.png")
credits_button_img = pygame.image.load("_credits.png")

# Charger l'image pour les crédits déroulants
credits_image = pygame.image.load("credit_baiana.png")
# Adapter la taille de l'image à la fenêtre
credits_image = pygame.transform.scale(credits_image, (WIDTH, HEIGHT))

# Font
font = pygame.font.SysFont(None, 50)
big_font = pygame.font.SysFont(None, 80)

# Fonction pour afficher du texte
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Menu principal
def main_menu():
    while True:
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # Affichage du titre
        screen.blit(title_img, ((WIDTH - title_img.get_width()) // 2, HEIGHT // 4))

        # Affichage des boutons
        screen.blit(chapitres_button_img, ((WIDTH - chapitres_button_img.get_width()) // 2, HEIGHT // 2))
        screen.blit(quitter_button_img, ((WIDTH - quitter_button_img.get_width()) // 2, HEIGHT // 2 + 2 * (HEIGHT // 12)))
        screen.blit(credits_button_img, ((WIDTH - credits_button_img.get_width()) // 2, HEIGHT // 2 + (HEIGHT // 12)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if chapitres_button_img.get_rect(topleft=((WIDTH - chapitres_button_img.get_width()) // 2, HEIGHT // 2)).collidepoint(mouse_pos):
                    chapitres_menu()
                elif quitter_button_img.get_rect(topleft=((WIDTH - quitter_button_img.get_width()) // 2, HEIGHT // 2 + 2 * (HEIGHT // 12))).collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                elif credits_button_img.get_rect(topleft=((WIDTH - credits_button_img.get_width()) // 2, HEIGHT // 2 + (HEIGHT // 12))).collidepoint(mouse_pos):
                    credits_menu()

# Menu des chapitres
def chapitres_menu():
    while True:
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # Affichage des boutons des chapitres
        chapitres_images = [chapitre1_img, chapitre2_img, chapitre3_img, chapitre4_img, chapitre5_img]
        y_position = HEIGHT // 3 + HEIGHT // 5 + HEIGHT // 20
        for i, chapitre_img in enumerate(chapitres_images):
            screen.blit(chapitre_img, ((WIDTH - chapitre_img.get_width()) // 2, y_position))
            y_position += chapitre_img.get_height() + HEIGHT // 20

        # Bouton retour
        screen.blit(retour_button_img, ((WIDTH - retour_button_img.get_width()) // 2, y_position + HEIGHT // 20))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, chapitre_img in enumerate(chapitres_images):
                    chapitre_rect = chapitre_img.get_rect(topleft=((WIDTH - chapitre_img.get_width()) // 2, HEIGHT // 3 + HEIGHT // 5 + HEIGHT // 20 + i * (chapitre_img.get_height() + HEIGHT // 20)))
                    if chapitre_rect.collidepoint(mouse_pos):
                        print(f"Lancement du chapitre {i + 1}...")
                if retour_button_img.get_rect(topleft=((WIDTH - retour_button_img.get_width()) // 2, y_position + HEIGHT // 20)).collidepoint(mouse_pos):
                    return

# Menu de crédit
def credits_menu():
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)  # Arrière-plan pour les crédits

    # Affichage de l'image déroulante
    screen.blit(credits_image, (0, 0))

    # Bouton retour
    screen.blit(retour_button_img, ((WIDTH - retour_button_img.get_width()) // 2, HEIGHT - retour_button_img.get_height() - 20))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if retour_button_img.get_rect(topleft=((WIDTH - retour_button_img.get_width()) // 2, HEIGHT - retour_button_img.get_height() - 20)).collidepoint(mouse_pos):
                    return

# Lancement du menu principal
main_menu()
