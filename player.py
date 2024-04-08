import pygame
import gameobject

delta = {
    pygame.K_LEFT: (-500, 0),
    pygame.K_RIGHT: (+500, 0),
    pygame.K_UP: (0, -200),
    pygame.K_DOWN: (0, 200),
}


def clip(val, minval, maxval):
    return min(max(val, minval), maxval)


class Player(gameobject.object):
    def __init__(self, image_file, startposX, startpoxY, gravity):
        self.player = gameobject.object.__init__(self, image_file, startposX, startpoxY, True)
        self.speed = [0, 0]
        area = self.screen.get_rect()
        self.width, self.height = area.width, area.height  # screen
        self.gravity = gravity  # world gravity
        self.Egravity = gravity  # current gravity
        self.colldown = False
        self.collup = False
        self.collleft = False
        self.collright = False
        self.jump = False

    def __str__(self):
        return (f"Speed: {self.speed} "
                f"Gravity: {self.Egravity}\n"
                f"collup: {self.collup}\n"
                f"colldown: {self.colldown}\n"
                f"collleft: {self.collleft}\n"
                f"collright: {self.collright}\n"
                )

    def Update(self, list):
        self.speed[1] += self.Egravity
        self.rect.move_ip(self.speed)
        self.rect.left = clip(self.rect.left, 0, self.width)
        self.rect.right = clip(self.rect.right, 0, self.width)
        self.rect.top = clip(self.rect.top, 0, self.height)
        self.rect.bottom = clip(self.rect.bottom, 0, self.height)
        self.collision(list)

    def Movement(self, event, dt):
        if event.type == pygame.KEYDOWN:
            deltax, deltay = delta.get(event.key, (0, 0))
            self.speed[0] += deltax * dt
            if self.jump:
                self.speed[1] = deltay * 5 * dt
                self.jump = False
                self.Egravity = self.gravity
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.speed[0] = 0
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and self.speed[1] < 0:
                self.speed[1] = 0

    def Movementdebug(self, event):
        if event.type == pygame.KEYDOWN:
            deltax, deltay = delta.get(event.key, (0, 0))
            self.speed[0] = deltax // 50
            self.speed[1] = deltay // 20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.speed[0] = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.speed[1] = 0

    def collision(self, list):  # marche que avec des carrés
        indexes = self.rect.collidelistall(list)
        if indexes:
            for i in indexes:
                vector = [list[i].rect.centerx - self.rect.centerx, list[i].rect.centery - self.rect.centery]
                print(vector, indexes)
                if vector[0] > 0 and vector[1] > 0:  # topleft
                    if vector[0] > vector[1]:  # left
                        self.rect.right = list[i].rect.left
                    else:  # top
                        self.rect.bottom = list[i].rect.top
                        self.Egravity = 0
                        self.speed[1] = 0
                        self.jump = True

                if vector[0] > 0 > vector[1]:  # bottomleft
                    if vector[0] > -vector[1]:  # left
                        self.rect.right = list[i].rect.left
                    else:  # bottom
                        self.rect.top = list[i].rect.bottom
                        self.speed[1] = 0

                if vector[0] < 0 < vector[1]:  # topright
                    if -vector[0] > vector[1]:  # right
                        self.rect.left = list[i].rect.right
                    else:  # top
                        self.rect.bottom = list[i].rect.top
                        self.speed[1] = 0
                        self.Egravity = 0
                        self.speed[1] = 0
                        self.jump = True

                if vector[0] < 0 and vector[1] < 0:  # bottomright
                    if -vector[0] > -vector[1]:  # right
                        self.rect.left = list[i].rect.right
                    else:  # bottom
                        self.rect.top = list[i].rect.bottom
                        self.speed[1] = 0

        else:
            self.collup = False
            self.collright = False
            self.collleft = False
            self.colldown = False
            self.Egravity = self.gravity
