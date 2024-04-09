import pygame
import sys

pygame.init()

win = pygame.display.set_mode((500, 500))

player_cube_x = 400
player_cube_y = 400
player_cube_width = 60
player_cube_height = 60
player_cube_vel = 300

enemy_cube_x = 50
enemy_cube_y = 50
enemy_cube_width = 60
enemy_cube_height = 60
enemy_cube_vel = 100

bullet_speed = 5
bullet_interval = 30
bullet_timer = 0

bullet_list = []

clock = pygame.time.Clock()
FPS = 60

class Bullet:
    def __init__(self, x, y, vel):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.vel = vel

    def move(self):
        self.rect.x += self.vel

running = True

def jump():
    global player_cube_y, y_speed, in_jump
    if not in_jump:
        in_jump = True
        y_speed = jump_speed

jump_speed = -20
gravity = 1
in_jump = False
y_speed = 0

while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    if in_jump:
        player_cube_y += y_speed
        y_speed += gravity
        if player_cube_y > 500:
            player_cube_y = 500
            in_jump = False
            y_speed = 0

    player_cube_x += player_cube_vel * dt

    if player_cube_x + player_cube_width > 500:
        player_cube_vel = -player_cube_vel
        player_cube_x = 500 - player_cube_width

    if player_cube_x < 0:
        player_cube_vel = abs(player_cube_vel)
        player_cube_x = 0

    bullet_timer += 1
    if bullet_timer >= bullet_interval:
        new_bullet = Bullet(enemy_cube_x + enemy_cube_width // 2, enemy_cube_y + enemy_cube_height // 2, bullet_speed)
        bullet_list.append(new_bullet)
        bullet_timer = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (player_cube_x, player_cube_y, player_cube_width, player_cube_height))
    pygame.draw.rect(win, (255, 0, 0), (enemy_cube_x, enemy_cube_y, enemy_cube_width, enemy_cube_height))

    for bullet in bullet_list:
        bullet.move()
        pygame.draw.rect(win, (0, 255, 0), bullet.rect)

        # Supprimer les balles qui sortent de l'écran
        if bullet.rect.x < 0 or bullet.rect.x > 500:
            bullet_list.remove(bullet)

    pygame.display.update()

pygame.quit()
sys.exit()
