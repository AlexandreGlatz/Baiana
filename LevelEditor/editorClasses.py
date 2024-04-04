import pygame


class Screen:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.window: pygame.display = None

    def CreateWindow(self):
        self.window = pygame.display.set_mode((self.width, self.height))

    def SetBgColor(self, color):
        self.window.fill(color)


class Palette:
    def __init__(self):
        self.tiles: [pygame.image] = []

    def PlaceTile(self, tileIndex, mouseX, mouseY):
        pass
