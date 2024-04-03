import pygame
import sys

pygame.init()

win = pygame.display.set_mode((500, 500))

x = 50
y = 50
width = 60
height = 60
vel = 300  

clock = pygame.time.Clock()
FPS = 60

running = True

def jump():
    global y, y_speed, in_jump
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
        y += y_speed
        y_speed += gravity
        if y > 500:
            y = 500
            in_jump = False
            y_speed = 0

    x += vel * dt

    if x + width > 500:
        vel = -vel
        x = 500 - width

    if x < 0:
        vel = abs(vel)
        x = 0

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
sys.exit()