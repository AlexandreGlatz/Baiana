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
    fullscreen = False
    
    while True:
        screen.fill(WHITE)
        
        # Affichage du titre
        draw_text("Baiana", big_font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        
        # Calcul des positions des options en fonction de la taille de la fenêtre
        option_y = HEIGHT // 2
        option_spacing = HEIGHT // 12
        option_width = WIDTH // 3
        option_height = HEIGHT // 15
        
        # Affichage des options
        jouer_rect = pygame.Rect((WIDTH - option_width) // 2, option_y, option_width, option_height)
        pygame.draw.rect(screen, BLACK, jouer_rect)
        draw_text("Jouer", font, WHITE, screen, (WIDTH - option_width) // 2 + option_width // 2, option_y + option_height // 2)
        
        quitter_rect = pygame.Rect((WIDTH - option_width) // 2, option_y + 2 * option_spacing, option_width, option_height)
        pygame.draw.rect(screen, BLACK, quitter_rect)
        draw_text("Quitter", font, WHITE, screen, (WIDTH - option_width) // 2 + option_width // 2, option_y + 2 * option_spacing + option_height // 2)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if jouer_rect.collidepoint(mouse_pos):
                    print("Lancement du jeu...")
                elif quitter_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


# Lancement du menu principal
main_menu()