import pygame
import sys

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

player_pos = [400, 500]
jump_speed = -20
gravity = 1
in_jump = False
y_speed = 0
score = 0
score_pos = [25, 25]

camera_offset_x = 0
camera_offset_y = 0

try:
    bg = pygame.image.load('photo-montagne-vallee-blanche-chamonix-mont-blanc.jpg')
except FileNotFoundError:
    bg = pygame.Surface(wind_size)
    bg.fill(GREY)

def Show_score():
    score_display = font.render(str(score), True, GREEN)
    screen.blit(score_display, (score_pos[0] + camera_offset_x, score_pos[1] + camera_offset_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not in_jump:
                score += 1
                in_jump = True
                y_speed = jump_speed

    if in_jump:
        player_pos[1] += y_speed
        y_speed += gravity

        if player_pos[1] > 500:
            player_pos[1] = 500
            in_jump = False
            y_speed = 0

    camera_offset_x = wind_size[0] // 2 - player_pos[0]
    camera_offset_y = wind_size[1] // 2 - player_pos[1]

    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, BLACK, [player_pos[0] + camera_offset_x, player_pos[1] + camera_offset_y, 50, 50])
    pygame.draw.rect(screen, GREY, [score_pos[0] + camera_offset_x, score_pos[1] + camera_offset_y, 150, 50], border_radius=10)
    Show_score()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()