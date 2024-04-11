import pygame
import os
import glob
from textButton import *
from TileButton import *
from screen import *
import json

SCREEN_WIDTH: int = 1920
SCREEN_HEIGHT: int = 1080
BROWN: [int] = (163, 85, 49, 255)


class Palette:
    def __init__(self, baseBg):
        self.tileSize = 20
        self.tileScale = (self.tileSize, self.tileSize)
        self.objects = []
        self.paletteButtons: [] = []
        self.currentBg = baseBg
        self.placedTiles = []
        self.lockOnGrid = False
        self.gameObjects = []

    def CreateLists(self, screen):
        i = 0
        x = 1520
        y = 0
        height = 20
        width = 100
        for folder in glob.glob('assets/*/'):
            j = 0
            self.objects.append([])
            tileX = 1520 + 25
            tileY = self.tileSize * 2
            for filename in glob.glob(folder + '*.png'):

                image = pygame.image.load(filename)
                self.objects[i].append(TileButton(tileX, tileY, self.tileSize, self.tileSize, i, j, image, filename))
                j += 1
                tileX += self.tileSize * 2
                if j % 4 == 0:
                    tileY += self.tileSize * 2
                    tileX = 1520 + 25

            self.paletteButtons.append(TextButton(DARKBROWN, x, y, width, height,
                                                  folder.split("\\")[1], 15,
                                                  self, screen, i))
            if x + width >= SCREEN_WIDTH:
                x = 0
                y += height
            i += 1
            x += width

    def GetObjectList(self):
        return self.objects

    def GetCategoryButtons(self):
        return self.paletteButtons

    def GetTileSize(self):
        return self.tileSize

    def GetTileButtonFromCategory(self, category):
        return self.objects[category]

    def GetPaletteButtons(self):
        return self.paletteButtons

    def GetCurrentBg(self):
        return self.currentBg

    def GetPlacedTiles(self):
        return self.placedTiles

    def SetLockOnGrid(self, lock):
        self.lockOnGrid = lock

    def DisplayPalette(self, screen: Screen, paletteToDisplay):
        backgroundRect = (1520, 0, 400, 1080)
        pygame.draw.rect(screen.window, BROWN, backgroundRect)
        y = 0
        x = 0
        for i in self.paletteButtons:
            i.DisplayCategoryButtons(screen)

        '''for i in range(len(paletteToDisplay)):
            if i % 4 == 0:
                y += self.tileSize * 2
                x = 0
            screen.window.blit(paletteToDisplay[i], (25 + 1520 + self.tileSize * 2 * x, y))
            x += 1'''
        for i in paletteToDisplay:
            i.DisplayTileButton(screen)

    def UnselectButtons(self, currentPaletteIndex, selectedTile, screen):
        for i in self.GetCategoryButtons()[:currentPaletteIndex] + self.GetCategoryButtons()[
                                                                   currentPaletteIndex + 1:]:
            self.GetCategoryButtons()[currentPaletteIndex].SetColor(DARKBROWN)

        for tileButton in (self.GetTileButtonFromCategory(currentPaletteIndex)[:selectedTile] +
                           self.GetTileButtonFromCategory(currentPaletteIndex)[selectedTile + 1:]):
            tileButton.UnClick(screen)

    def PlaceTile(self, selectedPalette, selectedTile, mousePos, camera):
        isSolid = False
        size = self.objects[selectedPalette][selectedTile].GetImageWidth()
        if self.lockOnGrid:
            posX = ((mousePos[0] + camera.GetCameraX()) // size) * size
            posY = (mousePos[1] // size) * size - 70
        else:
            posX = mousePos[0] + camera.GetCameraX()
            posY = mousePos[1]

        if selectedPalette == 0:
            self.currentBg = self.objects[selectedPalette][selectedTile].baseImage
        elif selectedPalette == 3:
            self.placedTiles.append([self.objects[selectedPalette][selectedTile].baseImage,
                                     (posX, posY)])
            if selectedPalette == 3:
                isSolid = True

            self.gameObjects.append([self.objects[selectedPalette][selectedTile].GetImageFile(),
                                     posX, posY - 60, isSolid, 0.4])
        else:
            self.placedTiles.append([self.objects[selectedPalette][selectedTile].image,
                                     (posX, posY)])
            if selectedPalette == 3:
                isSolid = True

            self.gameObjects.append([self.objects[selectedPalette][selectedTile].GetImageFile(),
                                     posX, posY - 60, isSolid, 0.4])

    def TilePreview(self, screen, selectedPalette, selectedTile, mousePos, camera):
        size = self.objects[selectedPalette][selectedTile].GetImageWidth()
        if self.lockOnGrid:
            posX = (mousePos[0] // size) * size
            posY = (mousePos[1] // size) * size - 60
        else:
            posX = mousePos[0]
            posY = mousePos[1]

        if selectedPalette == 3:
            screen.window.blit(self.objects[selectedPalette][selectedTile].baseImage, (posX, posY))

        elif not selectedPalette == 0 and mousePos[0] < 1520 + camera.GetCameraX():
            screen.window.blit(self.objects[selectedPalette][selectedTile].image, (posX, posY))

    def UpdateCurrentBg(self, screen):
        screen.window.blit(self.currentBg, (0, 0))

    def ExportLevel(self, levelName):
        with open(levelName + '.json', 'w') as f:
            json.dump(self.gameObjects, f)

    def Cancel(self):
        if len(self.placedTiles) != 0:
            self.placedTiles.pop()
            self.gameObjects.pop()
