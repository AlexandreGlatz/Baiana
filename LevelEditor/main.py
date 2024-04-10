import pygame
from editorClasses import *
from textButton import *
from tools import *
from camera import *


pygame.font.init()
pygame.init()

screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "Level Editor")
screen.CreateWindow()
screen.SetBgColor(WHITE)

palette = Palette(pygame.image.load("assets/backgrounds/bleu-ciel-540-ceradel-sans-plomb-20-grammes.png"))
palette.CreateLists(screen)
palette.DisplayPalette(screen, palette.GetObjectList()[0])
palette.GetCategoryButtons()[0].SetColor(BROWN)
currentPaletteIndex = 0
selectedPalette = 0
selectedTile = -1
camera = Camera()
levelList = ImportLevel('level1')
print(levelList)
while True:
    mousePos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                palette.ExportLevel('level1')
                pygame.quit()

            if event.key == pygame.K_LCTRL:
                palette.SetLockOnGrid(True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                palette.SetLockOnGrid(False)

        for i in range(len(palette.GetCategoryButtons())):
            if palette.GetCategoryButtons()[i].IsHover(mousePos, screen):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    palette.GetCategoryButtons()[i].OnClick()
                    currentPaletteIndex = i

        for tileButtons in palette.GetTileButtonFromCategory(currentPaletteIndex):
            if tileButtons.IsHover(mousePos, screen):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    selectedPalette = tileButtons.GetPalette()
                    selectedTile = tileButtons.GetTile()
                    tileButtons.OnClick(screen)

        palette.UpdateCurrentBg(screen)

        palette.UnselectButtons(currentPaletteIndex, selectedTile, screen)
        palette.TilePreview(screen, selectedPalette, selectedTile, mousePos, camera)

        if pygame.key.get_pressed()[pygame.K_q]:
            camera.CameraMove(-10)

        if pygame.key.get_pressed()[pygame.K_d]:
            camera.CameraMove(10)

        if mousePos[0] < 1520 + camera.GetCameraX() - palette.GetTileSize():
            if pygame.mouse.get_pressed()[0]:
                palette.PlaceTile(selectedPalette, selectedTile, mousePos, camera)

        for i in range(len(palette.GetPlacedTiles())):
            screen.window.blit(palette.GetPlacedTiles()[i][0], (palette.GetPlacedTiles()[i][1][0] - camera.GetCameraX(),
                                                                palette.GetPlacedTiles()[i][1][1]))

    palette.DisplayPalette(screen, palette.GetObjectList()[currentPaletteIndex])

    pygame.display.flip()
