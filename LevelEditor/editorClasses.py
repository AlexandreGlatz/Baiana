import pygame
import os
import glob
from button import *

BROWN: [int] = (163, 85, 49, 255)
WHITE: [int] = (255, 255, 255, 255)
BLACK: [int] = (0, 0, 0, 255)
TRANSPARENT: [int] = (0, 0, 0, 0)


class Screen:
    def __init__(self, width: int, height: int, windowName: str):
        self.width: int = width
        self.height: int = height
        self.window: pygame.display = None
        self.windowName: str = windowName

    def CreateWindow(self):
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.windowName)

    def SetBgColor(self, color):
        self.window.fill(color)


class Palette:
    def __init__(self):
        self.tileSize = 50
        self.tileScale = (self.tileSize, self.tileSize)
        self.objects = []
        self.paletteButtons: [TextButton] = []

    def CreateLists(self, screen):
        i = 0
        j = 0
        x = 1550
        width = 100
        for folder in glob.glob('assets/*/'):
            self.objects.append([])
            self.paletteButtons.append(TextButton(WHITE, x, 40, width, 20,
                                                  folder.split("\\")[1], 15,
                                                  lambda: Palette.DisplayPalette(self, screen, self.objects[i])))
            for filename in glob.glob(folder + '*.png'):
                image = pygame.image.load(filename)
                image = pygame.transform.scale(image, self.tileScale)
                self.objects[i].append(image)
                j += 1
            i += 1
            x += width + 10

    def DisplayPalette(self, screen: Screen, paletteToDisplay):
        backgroundRect = (1520, 0, 400, 1080)
        pygame.draw.rect(screen.window, BROWN, backgroundRect)
        y = 0
        x = 0
        for i in self.paletteButtons:
            i.DisplayButton(screen)

        for i in range(len(paletteToDisplay)):
            if i % 4 == 0:
                y += self.tileSize * 2
                x = 0
            screen.window.blit(paletteToDisplay[i], (25 + 1520 + self.tileSize * 2 * x, y))
            x += 1

    def PlaceTile(self, tileIndex, mouseX, mouseY):
        pass
