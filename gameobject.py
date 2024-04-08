import pygame


class object:
    def __init__(self, image_file, x, y, isSolid):
        self.isSolid = isSolid
        self.image = image_file
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.screen = pygame.display.get_surface()

    def draw(self):
        self.screen.blit(self.image, self)
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)
