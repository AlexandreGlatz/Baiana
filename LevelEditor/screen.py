import pygame


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
