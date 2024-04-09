import pygame

image1 = pygame.image.load("asset/Calque 11.png")
image2 = pygame.image.load("asset/Calque 11 (1).png")


class object:
    def __init__(self, image_file, x, y, isSolid, resize):
        self.isSolid = isSolid
        self.resize = resize
        self.image = image_file
        self.facingL = False
        self.image = pygame.transform.smoothscale_by(self.image, resize)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.screen = pygame.display.get_surface()
        self.dt = 1

    def draw(self):
        self.screen.blit(self.image, self)


class shark(object):
    def __init__(self, x, y, toLeft, toRight, speed, isSolid, resize):
        self.imageL = None
        self.shark = object.__init__(self, image1, x, y, isSolid, resize)
        self.startX = x
        self.toleft = toLeft
        self.toright = toRight
        self.speed = speed
        self.initimage()

    def initimage(self):
        self.imageL = pygame.transform.smoothscale_by(image1, self.resize)

    def draw(self):
        self.move()
        if self.facingL:
            self.image = pygame.transform.flip(self.imageL, False, False)
        else:
            self.image = pygame.transform.flip(self.imageL, True, False)
        self.screen.blit(self.image, self)

    def move(self):
        if self.rect.x > self.startX + self.toright:
            self.facingL = True
        if self.rect.x < self.startX - self.toleft:
            self.facingL = False

        if self.facingL:
            self.rect.move_ip(-self.speed * self.dt, 0)
        else:
            self.rect.move_ip(self.speed * self.dt, 0)
