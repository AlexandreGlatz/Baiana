import pygame
from textButton import *
from button import *


class TileButton(Button):

    def __init__(self, x, y, width, height, paletteIndex, tileIndex, image, imageFile, color=(0, 0, 0, 0)):
        Button.__init__(self, color, x, y, width, height)
        self.tileIndex = tileIndex
        self.imageWidth = image.get_width()
        self.imageHeight = image.get_height()
        self.baseImage = image
        self.thumbnail = pygame.transform.scale(self.baseImage, (width, height))
        self.image = pygame.transform.scale(self.baseImage, (self.imageWidth * 0.4, self.imageHeight * 0.4))
        self.paletteIndex = paletteIndex
        self.imageFile = imageFile

    def DisplayTileButton(self, screen):
        screen.window.blit(self.thumbnail, (self.x, self.y))

    def GetPalette(self):
        return self.paletteIndex

    def GetTile(self):
        return self.tileIndex

    def GetImageWidth(self):
        return self.imageWidth * 0.4

    def GetImageFile(self):
        return self.imageFile

    def OnClick(self, screen):
        pygame.draw.rect(screen.window, (0, 0, 0, 255), (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 1)
        screen.window.blit(self.thumbnail, (self.x, self.y))

    def UnClick(self, screen):
        pygame.draw.rect(screen.window, BROWN, (self.x - 5, self.y - 5, self.width + 10, self.height + 10), 1)
        screen.window.blit(self.thumbnail, (self.x, self.y))
