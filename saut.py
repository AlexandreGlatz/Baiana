import pygame
import sys

pygame.init()

wind_size = (800, 600)
screen = pygame.display.set_mode(wind_size)
pygame.display.set_caption('saut mdrr ca rebondit')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

player_pos = [400, 500]
jump_speed = -20
gravity = 1
in_jump = False
y_speed = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not in_jump:
                in_jump = True
                y_speed = jump_speed

    if in_jump:
        player_pos[1] += y_speed
        y_speed += gravity

        if player_pos[1] > 500:
            player_pos[1] = 500
            in_jump = False
            y_speed = 0

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (*player_pos, 50, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
