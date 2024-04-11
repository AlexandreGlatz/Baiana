import pygame
class BackgroundElement(pygame.sprite.Sprite):
    def __init__(self, image, pos, parallax_speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.parallax_speed = parallax_speed
        self.width = image.get_width()

    def update(self, camera_speed, screensize):
        self.rect.x += camera_speed * self.parallax_speed

        if self.rect.left > screensize[0]:
            self.rect.right = 0

        if self.rect.right < 0:
            self.rect.left = screensize[0]