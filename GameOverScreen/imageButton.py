import pygame
from button import *


class ImageButton(Button):

    def __init__(self, x, y, width, height, image, hoverImage, func):
        Button.__init__(self, (0, 0, 0, 0), x, y, width, height)
        self.imageDisplayed = image
        self.baseImage = image
        self.hoverImage = hoverImage
        self.possibleImages = [image, hoverImage]
        self.func = func

    def SetDisplayedImage(self, index):
        self.imageDisplayed = self.possibleImages[index]

    def DisplayButton(self, screen):
        screen.window.blit(self.imageDisplayed, (self.x, self.y))

    def Click(self):
        self.func()
