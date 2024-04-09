import pygame


class Button:

    def __init__(self, color, x, y, width, height):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def IsHover(self, mousePos, screen):
        if self.x < mousePos[0] < self.x + self.width:
            if self.y < mousePos[1] < self.y + self.height:
                return True

