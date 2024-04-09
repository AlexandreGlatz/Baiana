import pygame
import sys

pygame.init()

# Définition des constantes
WIDTH, HEIGHT = 500, 500
player_cube_width, player_cube_height = 60, 60
bullet_speed, bullet_interval = 5, 30

# Création de la fenêtre
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cube Tirant")

# Position du carré rouge (ennemi) au centre en haut
enemy_cube_width = 60
enemy_cube_height = 60
enemy_cube_x = (WIDTH - enemy_cube_width) // 2
enemy_cube_y = 0

# Position du cube blanc (joueur) initial
player_cube_x = (WIDTH - player_cube_width) // 2
player_cube_y = HEIGHT - player_cube_height

# Vitesse de déplacement du cube blanc
player_cube_vel = 5

# Initialisation des variables de tir
bullet_timer = 0
bullet_list = []

clock = pygame.time.Clock()
FPS = 60

class Bullet:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.vel = vel

    def move(self):
        self.rect.y += self.vel

running = True

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement du cube joueur (blanc) avec les touches q et d
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        player_cube_x -= player_cube_vel
    if keys[pygame.K_d]:
        player_cube_x += player_cube_vel

    # Limitation du déplacement du cube joueur pour qu'il reste dans la fenêtre
    if player_cube_x < 0:
        player_cube_x = 0
    elif player_cube_x + player_cube_width > WIDTH:
        player_cube_x = WIDTH - player_cube_width

    # Gestion du tir
    bullet_timer += 1
    if bullet_timer >= bullet_interval:
        new_bullet = Bullet(enemy_cube_x + enemy_cube_width // 2, enemy_cube_y + enemy_cube_height // 2, bullet_speed)
        bullet_list.append(new_bullet)
        bullet_timer = 0

    # Mise à jour de la position des balles
    for bullet in bullet_list:
        bullet.move()

        # Supprimer les balles qui sortent de l'écran
        if bullet.rect.y > HEIGHT:
            bullet_list.remove(bullet)

    # Effacement de l'écran
    win.fill((0, 0, 0))

    # Dessin des éléments
    pygame.draw.rect(win, (255, 255, 255), (player_cube_x, player_cube_y, player_cube_width, player_cube_height)) # Cube joueur (blanc)
    pygame.draw.rect(win, (255, 0, 0), (enemy_cube_x, enemy_cube_y, enemy_cube_width, enemy_cube_height)) # Cube ennemi (rouge)
    for bullet in bullet_list:
        pygame.draw.rect(win, (0, 255, 0), bullet.rect) # Balles (vertes)

    pygame.display.update()

pygame.quit()
sys.exit()
