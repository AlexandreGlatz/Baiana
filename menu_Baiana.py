import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Résolution par défaut
screensize = pygame.display.set_mode().get_size()
WIDTH = screensize[0]
HEIGHT = screensize[1]


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('asset/menu principal.png', [0, 0])
# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuration de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Pygame")

# Charger les images
title_img = pygame.image.load("asset/episode 1 baiana.png")
chapitres_button_img = pygame.image.load("asset/_ chapitres.png")
quitter_button_img = pygame.image.load("asset/_ retour au bureau.png")
retour_button_img = pygame.image.load("asset/_ RETOUR.png")
chapitre1_img = pygame.image.load("asset/_ CHapitre 1.png")
chapitre2_img = pygame.image.load("asset/_ CHapitre 2.png")
chapitre3_img = pygame.image.load("asset/_ CHapitre 3.png")
chapitre4_img = pygame.image.load("asset/_ CHapitre 4.png")
chapitre5_img = pygame.image.load("asset/_ CHapitre 5.png")

# Font
font = pygame.font.SysFont(None, 50)
big_font = pygame.font.SysFont(None, 80)


# Fonction pour afficher du texte
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


# Fonction principale du menu
def main_menu():
    while True:
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # Affichage du titre
        screen.blit(title_img, ((WIDTH - title_img.get_width()) // 2, HEIGHT // 4))

        # Affichage des images des boutons
        screen.blit(chapitres_button_img, ((WIDTH - chapitres_button_img.get_width()) // 2, HEIGHT // 2))
        screen.blit(quitter_button_img,
                    ((WIDTH - quitter_button_img.get_width()) // 2, HEIGHT // 2 + 2 * (HEIGHT // 12)))

        # Calcul des positions des options en fonction de la taille de la fenêtre
        option_y = HEIGHT // 2
        option_spacing = HEIGHT // 12
        option_width = WIDTH // 3
        option_height = HEIGHT // 15

        # Affichage des options
        chapitres_rect = pygame.Rect((WIDTH - option_width) // 2, option_y, option_width, option_height)

        quitter_rect = pygame.Rect((WIDTH - option_width) // 2, option_y + 2 * option_spacing, option_width,
                                   option_height)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if chapitres_rect.collidepoint(mouse_pos):
                    return chapitres_menu()  # Si l'utilisateur clique sur "Chapitres", afficher le sous-menu des
                    # chapitres
                elif quitter_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


# Sous-menu des chapitres

def chapitres_menu():
    while True:
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # Affichage du titre
        screen.blit(chapitres_button_img, ((WIDTH - chapitres_button_img.get_width()) // 2, HEIGHT // 3))

        # Affichage des images des chapitres
        chapitres_images = [chapitre1_img, chapitre2_img, chapitre3_img, chapitre4_img, chapitre5_img]
        y_position = HEIGHT // 3 + HEIGHT // 5 + HEIGHT // 20
        for i, chapitre_img in enumerate(chapitres_images):
            screen.blit(chapitre_img, ((WIDTH - chapitre_img.get_width()) // 2, y_position))
            y_position += chapitre_img.get_height() + HEIGHT // 20

        # Affichage de l'image du bouton "Retour"
        screen.blit(retour_button_img, ((WIDTH - retour_button_img.get_width()) // 2, y_position + HEIGHT // 20))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Ajoutez ici le code pour traiter la sélection du chapitre ou le retour en arrière
                for i, chapitre_img in enumerate(chapitres_images):
                    chapitre_rect = chapitre_img.get_rect(topleft=((WIDTH - chapitre_img.get_width()) // 2,
                                                                   HEIGHT // 3 + HEIGHT // 5 + HEIGHT // 20 + i *
                                                                   (chapitre_img.get_height() + HEIGHT // 20)))
                    if chapitre_rect.collidepoint(mouse_pos):
                        print(f"Lancement du chapitre {i + 1}...")
                        return i + 1
                        # Ajoutez ici le code pour démarrer le chapitre correspondant
                if retour_button_img.get_rect(
                        topleft=((WIDTH - retour_button_img.get_width()) // 2, y_position + HEIGHT // 20)).collidepoint(
                        mouse_pos):
                    return  # Retour au menu principal


# Lancement du menu principal
