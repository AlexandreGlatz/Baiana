import pygame
from editorClasses import *

class TextButton:

    def __init__(self, color, x, y, width, height, text, textSize, func):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textSize = textSize
        self.func = func

    def DisplayButton(self, screen):
        s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # per-pixel alpha
        s.fill(self.color)  # notice the alpha value in the color
        screen.window.blit(s, (self.x, self.y))
        font = pygame.font.SysFont('Verdana', self.textSize)
        text = font.render(self.text, 1, (0, 0, 0))
        screen.window.blit(text,
                           (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def Hover(self, mousePos, screen):
        if self.x < mousePos[0] < self.x + self.width:
            if self.y < mousePos[1] < self.y + self.height:
                underlineRect = (self.x - self.width - 5, self.y, self.width, 1)
                pygame.draw.rect(screen.window, BLACK, underlineRect)
                return True

    def OnClick(self):
        return self.func()
