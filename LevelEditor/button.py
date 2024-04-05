import pygame


class Button:
    def __init__(self, color, x, y, width, height, textSize, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textSize = textSize

    def DisplayButton(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        # rect = pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        s = pygame.Surface((self.width, self.height))  # the size of your rect
        s.set_alpha(255)  # alpha level
        s.fill((255, 255, 255))  # this fills the entire surface
        win.blit(s, (self.x, self.y))
        if self.text != '':
            font = pygame.font.SysFont('Verdana', self.textSize)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def Hover(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False
