import pygame

image1 = pygame.image.load("asset/Calque 11.png")
image2 = pygame.image.load("asset/Calque 11 (1).png")


class object:
    def __init__(self, image_file, x, y, isSolid):
        self.isSolid = isSolid
        self.image = image_file
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.screen = pygame.display.get_surface()

    def draw(self):
        self.screen.blit(self.image, self)


class shark(object):
    def __init__(self, x, y, length, speed, isSolid):
        self.shark = object.__init__(self, image1, x, y, isSolid)
        self.facingL = False
        self.startX = x
        self.length = length
        self.speed = speed

    def draw(self):
        self.move()
        if self.facingL:
            self.image = image1
            self.screen.blit(self.image, self)
        else:
            self.image = image2
            self.screen.blit(self.image, self)

    def move(self):
        if self.rect.x > self.startX + self.length or self.rect.x < self.startX - self.length:
            if self.facingL:
                self.facingL = False
            else:
                self.facingL = True

        if self.facingL:
            self.rect.move_ip(-self.speed, 0)
        else:
            self.rect.move_ip(self.speed, 0)
