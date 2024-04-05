import pygame
import glob
from button import *

BROWN: [int] = (163, 85, 49)
WHITE: [int] = (255, 255, 255)
BLACK: [int] = (0, 0, 0)


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
        self.tiles: [pygame.image] = []
        self.props: [pygame.image] = []
        self.backgrounds: [pygame.image] = []
        self.paletteButtons: [Button] = []

    def CreatePaletteButtons(self):
        tilesButton = Button(WHITE, 1550, 40, 100, 20, 15, "Tiles")
        propsButton = Button(WHITE, 1550 + 100 + 10, 40, 100, 20, 15, "Props")
        backgroundsButton = Button(WHITE, 1550 + 210 + 10, 40, 100, 20, 15, "Backgrounds")
        self.paletteButtons = [tilesButton, propsButton, backgroundsButton]

    def CreateLists(self):
        for filename in glob.glob('assets/tiles/*.png'):
            image = pygame.image.load(filename)
            image = pygame.transform.scale(image, self.tileScale)
            self.tiles.append(image)

        for filename in glob.glob('assets/props/*.png'):
            image = pygame.image.load(filename)
            image = pygame.transform.scale(image, self.tileScale)
            self.props.append(image)

        for filename in glob.glob('assets/backgrounds/*.png'):
            image = pygame.image.load(filename)
            image = pygame.transform.scale(image, self.tileScale)
            self.backgrounds.append(image)

    def DisplayPalette(self, screen: Screen, paletteToDisplay: str):
        backgroundRect = (1520, 0, 400, 1080)
        pygame.draw.rect(screen.window, BROWN, backgroundRect)
        y = 0
        x = 0
        for i in self.paletteButtons:
            i.DisplayButton(screen.window)

        if paletteToDisplay == "tiles":
            for i in range(len(self.tiles)):
                if i % 4 == 0:
                    y += self.tileSize * 2
                    x = 0
                screen.window.blit(self.tiles[i], (25 + 1520 + self.tileSize * 2 * x, y))
                x += 1

        elif paletteToDisplay == "props":
            for i in range(len(self.props)):
                if i % 4 == 0:
                    y += 100
                    x = 0
                screen.window.blit(self.props[i], (25 + 1520 + self.tileSize * 2 * x, y))
                x += 1

        elif paletteToDisplay == "backgrounds":
            for i in range(len(self.backgrounds)):
                if i % 4 == 0:
                    y += 100
                    x = 0
                screen.window.blit(self.backgrounds[i], (25 + 1520 + self.tileSize * 2 * x, y))
                x += 1

    def PlaceTile(self, tileIndex, mouseX, mouseY):
        pass
