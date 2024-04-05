import pygame
import sys
import math
import pymunk

pygame.init()

wind_size = (800, 600)
screen = pygame.display.set_mode(wind_size)
pygame.display.set_caption('Saut mdrr ça rebondit')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

try:
    font = pygame.font.Font('Daydream.ttf', 25)
except FileNotFoundError:
    font = pygame.font.SysFont(None, 25)

#settings
player_pos = [400, 500]
player_speed = 5
jump_speed = -20
gravity = 1
in_jump = False
y_speed = 0
score = 0
score_pos = [25, 25]
on_vine = False
vine_pos = [600, 200]
vine_height = 200
angle = 0
swing_speed = 0.1
f_pressed = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not on_vine:
        if keys[pygame.K_q]:
            player_pos[0] -= player_speed
        if keys[pygame.K_d]:
            player_pos[0] += player_speed
        if keys[pygame.K_SPACE] and not in_jump:
            y_speed = jump_speed
            in_jump = True

    if keys[pygame.K_f] and not f_pressed:
        f_pressed = True
        if not on_vine and abs(player_pos[0] + 25 - vine_pos[0]) < 10 and player_pos[1] < vine_pos[1] + vine_height and player_pos[1] > vine_pos[1]:
            on_vine = True
            in_jump = False
            y_speed = 0
        elif on_vine:
            on_vine = False
            in_jump = True
    elif not keys[pygame.K_f]:
        f_pressed = False

    if on_vine:
        if keys[pygame.K_q]:
            angle -= swing_speed
        if keys[pygame.K_d]:
            angle += swing_speed
        player_pos[0] = vine_pos[0] + math.sin(angle) * 100 - 25
        player_pos[1] = vine_pos[1] + (vine_height / 2) + (math.cos(angle) * 100) - 25

    #wall jump activate :
    #if player_pos[0] > vine_pos[0] + math.sin(angle)*100 - 50 or player_pos[1] > vine_pos[1] + (vine_height / 2) + (math.cos(angle) * 100) - 50 :
        #on_vine = False

    if in_jump and not on_vine:
        player_pos[1] += y_speed
        y_speed += gravity
        if player_pos[1] >= 500:
            player_pos[1] = 500
            in_jump = False
            y_speed = 0

    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, (vine_pos[0] - 5, vine_pos[1], 10, vine_height))
    pygame.draw.rect(screen, WHITE, (*player_pos, 50, 50))

    score_text = font.render(f'Score: {score}', True, GREEN)
    screen.blit(score_text, score_pos)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
