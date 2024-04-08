import pygame
import gameobject
from math import sqrt

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

    def collision(self, list):  # non opti car AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        # it took like 15h to have it work correctly
        indexes = self.rect.collidelistall(list)
        if indexes:
            for i in indexes:
                if list[i].isSolid:
                    vectorTopLeft = [list[i].rect.topleft[0] - self.rect.bottomright[0],
                                     list[i].rect.topleft[1] - self.rect.bottomright[1]]
                    vectorTopRight = [list[i].rect.topright[0] - self.rect.bottomleft[0],
                                      list[i].rect.topright[1] - self.rect.bottomleft[1]]
                    vectorBottomRight = [list[i].rect.bottomright[0] - self.rect.topleft[0],
                                         list[i].rect.bottomright[1] - self.rect.topleft[1]]
                    vectorBottomLeft = [list[i].rect.bottomleft[0] - self.rect.topright[0],
                                        list[i].rect.bottomleft[1] - self.rect.topright[1]]
                    normTL = sqrt(vectorTopLeft[0]**2 + vectorTopLeft[1]**2)
                    normTR = sqrt(vectorTopRight[0]**2 + vectorTopRight[1]**2)
                    normBR = sqrt(vectorBottomRight[0]**2 + vectorBottomRight[1]**2)
                    normBL = sqrt(vectorBottomLeft[0]**2 + vectorBottomLeft[1]**2)

                    if min(normBL, normBR, normTL, normTR) == normTL:  # closer to topleft
                        if vectorTopLeft[0] > vectorTopLeft[1]:  # left
                            self.rect.right = list[i].rect.left
                        else:  # top
                            self.rect.bottom = list[i].rect.top
                            self.Egravity = 0
                            self.speed[1] = 0
                            self.jump = True

                    elif min(normBL, normBR, normTL, normTR) == normTR:  # closer to topright
                        if -vectorTopRight[0] > vectorTopRight[1]:  # right
                            self.rect.left = list[i].rect.right
                        else:  # top
                            self.rect.bottom = list[i].rect.top
                            self.speed[1] = 0
                            self.Egravity = 0
                            self.speed[1] = 0
                            self.jump = True

                    elif min(normBL, normBR, normTL, normTR) == normBR:  # closer to bottomright
                        if -vectorBottomRight[0] > -vectorBottomRight[1]:  # right
                            self.rect.left = list[i].rect.right
                        else:  # bottom
                            self.rect.top = list[i].rect.bottom
                            self.speed[1] = 0

                    else:  # closer to bottomleft
                        if vectorBottomLeft[0] > -vectorBottomLeft[1]:  # left
                            self.rect.right = list[i].rect.left
                        else:  # bottom
                            self.rect.top = list[i].rect.bottom
                            self.speed[1] = 0

        else:
            self.collup = False
            self.collright = False
            self.collleft = False
            self.colldown = False
            self.Egravity = self.gravity
