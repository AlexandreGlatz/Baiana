import pygame
import sys

pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

player_cube_width, player_cube_height = 38, 62
player_cube_vel = 300

enemy_cube_width, enemy_cube_height = 60, 60
enemy_cube_vel = 100

# Définir le rectangle de l'ennemi
enemy_cube = pygame.Rect((win_width - enemy_cube_width) // 2, 20, enemy_cube_width, enemy_cube_height)

bullet_speed = 500
bullet_interval = 2
bullet_timer = 0

bullet_list = []

clock = pygame.time.Clock()
FPS = 60
running = True

spritesheet = pygame.image.load("main_character-Sheet.png")

class Bullet:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.vel = vel

    def move(self, dt):
        self.rect.y += self.vel * dt

print("Chargement du spritesheet:", spritesheet.get_size())  # Vérifier si le spritesheet est correctement chargé

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_frame = 0
        self.animation_speed = 0.1
        self.frames = []  
        self.extract_frames()  

    def extract_frames(self):
        for i in range(6):  
            frame = spritesheet.subsurface(pygame.Rect(i * player_cube_width, 0, player_cube_width, player_cube_height))
            frame = pygame.transform.scale(frame, (player_cube_width, player_cube_height))  
            self.frames.append(frame)

    def update(self):
        self.current_frame = (self.current_frame + self.animation_speed) % len(self.frames)

    def draw(self, surface):
        surface.blit(self.frames[int(self.current_frame)], (self.x, self.y))




# Définir les coordonnées initiales du joueur
player = Player((win_width - player_cube_width) // 2, win_height - player_cube_height)

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    ##### MOUVEMENT ######
    if keys[pygame.K_LEFT]:
        player.x -= player_cube_vel * dt

    if keys[pygame.K_RIGHT]:
        player.x += player_cube_vel * dt

    player.update()  # Mettre à jour l'animation du joueur

    bullet_timer += dt
    if bullet_timer >= bullet_interval:
        new_bullet = Bullet(enemy_cube.x + enemy_cube_width // 2, enemy_cube.y + enemy_cube_height, bullet_speed)
        bullet_list.append(new_bullet)
        bullet_timer = 0

    win.fill((0, 0, 0))  # Effacer l'écran

    player.draw(win)  # Dessiner le joueur

    pygame.draw.rect(win, (255, 0, 0), enemy_cube)

    for bullet in bullet_list:
        bullet.move(dt)
        pygame.draw.rect(win, (0, 255, 0), bullet.rect)

        if bullet.rect.y < 0 or bullet.rect.y > win_height:
            bullet_list.remove(bullet)

    pygame.display.update()

pygame.quit()
sys.exit()
