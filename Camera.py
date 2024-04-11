import pygame


class Camera:
    def __init__(self, follow_target, width, height):
        self.target = follow_target
        self.rect = pygame.Rect(0, 0, width, height)
        self.smooth_speed = 0.1

    def update(self):
        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        self.rect.x += int(dx * self.smooth_speed)
        self.rect.y += int(dy * self.smooth_speed)
        if self.rect.y > 100:
            self.rect.y = 100

    def apply(self, entity):
        if isinstance(entity, pygame.Rect):
            return entity.move(-self.rect.topleft[0], -self.rect.topleft[1])
        else:
            return entity.rect.move(-self.rect.topleft[0], -self.rect.topleft[1])
