import pygame
from textButton import *
from button import *


class TileButton(Button):

    def __init__(self, x, y, width, height, paletteIndex,  tileIndex, image, color=TRANSPARENT):
        Button.__init__(self, color, x, y, width, height)
        self.tileIndex = tileIndex
        self.imageWidth = image.get_width()
        print(self.imageWidth * 0.2)
        self.imageHeight = image.get_height()
        self.baseImage = image
        self.thumbnail = pygame.transform.scale(self.baseImage, (width, height))
        self.image = pygame.transform.scale(self.baseImage, (self.imageWidth * 0.2, self.imageHeight * 0.2))
        self.paletteIndex = paletteIndex

    def DisplayTileButton(self, screen):
        screen.window.blit(self.thumbnail, (self.x, self.y))

    def GetPalette(self):
        return self.paletteIndex

    def GetTile(self):
        return self.tileIndex

    def OnClick(self, screen):
        pygame.draw.rect(screen.window, BLACK, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 1)
        screen.window.blit(self.thumbnail, (self.x, self.y))

    def UnClick(self, screen):
        pygame.draw.rect(screen.window, BROWN, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 1)
        screen.window.blit(self.thumbnail, (self.x, self.y))
