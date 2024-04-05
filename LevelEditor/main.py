import pygame
from editorClasses import *
pygame.font.init()
pygame.init()
SCREEN_WIDTH: int = 1920
SCREEN_HEIGHT: int = 1080

screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "Level Editor")
screen.CreateWindow()
screen.SetBgColor(WHITE)

palette = Palette()
palette.CreateLists(screen)
palette.DisplayPalette(screen, palette.objects[3])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    pygame.display.update()

