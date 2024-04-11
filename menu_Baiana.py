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
        draw_text("Baiana", big_font, BLACK, screen, WIDTH // 2, HEIGHT // 4)

        # Calcul des positions des options en fonction de la taille de la fenêtre
        option_y = HEIGHT // 2
        option_spacing = HEIGHT // 12
        option_width = WIDTH // 3
        option_height = HEIGHT // 15

        # Affichage des options
        chapitres_rect = pygame.Rect((WIDTH - option_width) // 2, option_y, option_width, option_height)
        pygame.draw.rect(screen, BLACK, chapitres_rect)
        draw_text("Chapitres", font, WHITE, screen, (WIDTH - option_width) // 2 + option_width // 2,
                  option_y + option_height // 2)

        quitter_rect = pygame.Rect((WIDTH - option_width) // 2, option_y + 2 * option_spacing, option_width,
                                   option_height)
        pygame.draw.rect(screen, BLACK, quitter_rect)
        draw_text("Quitter", font, WHITE, screen, (WIDTH - option_width) // 2 + option_width // 2,
                  option_y + 2 * option_spacing + option_height // 2)

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
        draw_text("Chapitres", big_font, BLACK, screen, WIDTH // 2, HEIGHT // 3 + HEIGHT // 5)

        # Calcul des positions des options en fonction de la taille de la fenêtre
        option_y = HEIGHT // 3 + HEIGHT // 5 + HEIGHT // 20
        option_spacing = HEIGHT // 20
        option_width = WIDTH // 3
        option_height = HEIGHT // 15

        # Affichage des chapitres
        for i in range(1, 6):
            chapter_rect = pygame.Rect((WIDTH - option_width) // 2, option_y, option_width, option_height)
            pygame.draw.rect(screen, BLACK, chapter_rect)
            draw_text(f"Chapitre {i}", font, WHITE, screen, (WIDTH - option_width) // 2 + option_width // 2,
                      option_y + option_height // 2)
            option_y += option_spacing

        # Affichage du bouton "Retour"
        retour_rect = pygame.Rect((WIDTH - option_width) // 2, option_y + option_spacing, option_width, option_height)
        pygame.draw.rect(screen, BLACK, retour_rect)
        draw_text("Retour", font, WHITE, screen, (WIDTH - option_width) // 2 + option_width // 2,
                  option_y + option_spacing + option_height // 2)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Ajoutez ici le code pour traiter la sélection du chapitre ou le retour en arrière
                for i in range(1, 6):
                    chapter_rect = pygame.Rect((WIDTH - option_width) // 2,
                                               HEIGHT // 3 + HEIGHT // 5 + HEIGHT // 20 + (i - 1) * option_spacing,
                                               option_width, option_height)
                    if chapter_rect.collidepoint(mouse_pos):
                        print(f"Lancement du chapitre {i}...")
                        # Ajoutez ici le code pour démarrer le chapitre correspondant
                        return i
                if retour_rect.collidepoint(mouse_pos):
                    return  # Retour au menu principal


# Lancement du menu principal
