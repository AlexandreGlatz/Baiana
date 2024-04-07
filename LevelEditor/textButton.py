import pygame
from editorClasses import *
from button import *
BROWN: [int] = (163, 85, 49, 255)
DARKBROWN: [int] = (114, 55, 27, 255)
WHITE: [int] = (255, 255, 255, 255)
BLACK: [int] = (0, 0, 0, 255)
TRANSPARENT: [int] = (0, 0, 0, 0)


class TextButton(Button):

    def __init__(self, color, x, y, width, height, text, textSize, palette, screen, i):
        Button.__init__(self, color, x, y, width, height)
        self.text = text
        self.textSize = textSize
        self.func = lambda: palette.DisplayPalette(screen, palette.objects[i])
        self.isSelected = False

    def DisplayCategoryButtons(self, screen):
        s = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # per-pixel alpha
        s.fill(self.color)  # notice the alpha value in the color
        screen.window.blit(s, (self.x, self.y))
        font = pygame.font.SysFont('Verdana', self.textSize)
        text = font.render(self.text, 1, (0, 0, 0))
        screen.window.blit(text,
                           (self.x + (self.width / 2 - text.get_width() / 2),
                            self.y + (self.height / 2 - text.get_height() / 2)))

    def OnClick(self):
        self.color = BROWN
        return self.func()

    def SetColor(self, color):
        self.color = color

