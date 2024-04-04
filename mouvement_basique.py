import pygame
import sys

pygame.init()

win_width, win_height = 500, 500
win = pygame.display.set_mode((win_width, win_height))

player_cube_width, player_cube_height = 60, 60
player_cube_vel = 300

enemy_cube_width, enemy_cube_height = 60, 60
enemy_cube_vel = 100

player_cube = pygame.Rect((win_width - player_cube_width) // 2, win_height - player_cube_height, player_cube_width, player_cube_height)
enemy_cube = pygame.Rect((win_width - enemy_cube_width) // 2, 20, enemy_cube_width, enemy_cube_height)

bullet_speed = 500
bullet_interval = 2
bullet_timer = 0

bullet_list = []

clock = pygame.time.Clock()
FPS = 60

class Bullet:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.vel = vel

    def move(self, dt):
        self.rect.y += self.vel * dt
running = True

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_cube.x -= player_cube_vel * dt

    if keys[pygame.K_RIGHT]:
        player_cube.x += player_cube_vel * dt

    bullet_timer += dt
    if bullet_timer >= bullet_interval:
        new_bullet = Bullet(enemy_cube.x + enemy_cube_width // 2, enemy_cube.y + enemy_cube_height, bullet_speed)
        bullet_list.append(new_bullet)
        bullet_timer = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), player_cube)
    pygame.draw.rect(win, (255, 0, 0), enemy_cube)

    for bullet in bullet_list:
        bullet.move(dt)
        pygame.draw.rect(win, (0, 255, 0), bullet.rect)

        # Supprimer les balles qui sortent de l'écran
        if bullet.rect.y < 0 or bullet.rect.y > win_height:
            bullet_list.remove(bullet)

    pygame.display.update()

pygame.quit()
sys.exit()
