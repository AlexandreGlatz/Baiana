import pygame
from editorClasses import *
from textButton import *
from tools import *

pygame.font.init()
pygame.init()

screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "Level Editor")
screen.CreateWindow()
screen.SetBgColor(WHITE)

palette = Palette()
palette.CreateLists(screen)
palette.DisplayPalette(screen, palette.GetObjectList()[0])
palette.GetCategoryButtons()[0].color = BROWN
currentPaletteIndex = 0
selectedPalette = 0
selectedTile = None
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        mousePos = pygame.mouse.get_pos()

        for i in range(len(palette.GetCategoryButtons())):
            if palette.GetCategoryButtons()[i].IsHover(mousePos, screen):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    palette.GetCategoryButtons()[i].OnClick()
                    currentPaletteIndex = i

        for tileButtons in palette.GetDisplayedTileButton(currentPaletteIndex):
            if tileButtons.IsHover(mousePos, screen):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    selectedPalette = tileButtons.GetPalette()
                    selectedTile = tileButtons.GetTile()
                    tileButtons.OnClick(screen)

        if mousePos[0] < 1520 - palette.GetTileSize():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                palette.PlaceTile(screen, palette.GetObjectList()[selectedPalette][selectedTile], mousePos)

    palette.UnselectButtons(currentPaletteIndex)

    pygame.display.update()
