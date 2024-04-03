import pygame


class object(pygame.sprite.Sprite):
    def __init__(self, x, y, height , width, isSolid):
        self.isSolid = isSolid
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
