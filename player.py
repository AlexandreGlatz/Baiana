import pygame

delta = {
    pygame.K_LEFT: (-2, 0),
    pygame.K_RIGHT: (+2, 0),
    pygame.K_UP: (0, -10),
    pygame.K_DOWN: (0, 2),
}


def clip(val, minval, maxval):
    return min(max(val, minval), maxval)


class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, gravity):
        self.i = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.speed = [0, 0]
        self.screen = pygame.display.get_surface()
        area = self.screen.get_rect()
        self.width, self.height = area.width, area.height  # screen

        self.rect.x = x
        self.rect.y = y
        self.gravity = gravity
        self.Egravity = gravity
        self.coll = False

    def Update(self):
        self.speed[1] += self.Egravity
        self.rect.move_ip(self.speed)
        self.rect.left = clip(self.rect.left, 0, self.width)
        self.rect.right = clip(self.rect.right, 0, self.width)
        self.rect.top = clip(self.rect.top, 0, self.height)
        self.rect.bottom = clip(self.rect.bottom, 0, self.height)
        if self.rect.bottom == self.height:
            self.speed[1] = 0

    def Movement(self, event):
        if event.type == pygame.KEYDOWN:
            deltax, deltay = delta.get(event.key, (0, 0))
            self.speed[0] += deltax
            self.speed[1] += deltay
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.speed[0] = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.speed[1] = 0

    def draw(self):
        self.screen.blit(self.image, self)

    def collision(self, list):
        index = self.rect.collidelist(list)
        if index != -1 and list[index].isSolid:
            itemrect = list[index].rect
            if (self.rect.clipline((itemrect.topleft[0] + 5, itemrect.topleft[1]),
                                   (itemrect.topright[0] - 5, itemrect.topright[1])) and not self.coll):  # top
                self.speed[1] = 0
                self.rect.bottom = itemrect.top + 1
                self.Egravity = 0
                self.coll = True
            elif self.rect.clipline(itemrect.bottomleft, itemrect.bottomright):  # bottom
                self.speed[1] = 0
                self.rect.top = itemrect.bottom
            elif self.rect.clipline(itemrect.bottomleft, itemrect.topleft) and not self.coll:  # left
                self.speed[0] = 0
                self.rect.right = itemrect.left
            elif self.rect.clipline(itemrect.bottomright, itemrect.topright) and not self.coll:  # right
                self.speed[0] = 0
                self.rect.left = itemrect.right
        else:
            self.Egravity = self.gravity
            self.coll = False
