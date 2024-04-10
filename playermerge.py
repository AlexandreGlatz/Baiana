import pygame
import gameobject
from math import sqrt, pi, sin

delta = {
    pygame.K_LEFT: (-2000, 0),
    pygame.K_RIGHT: (+2000, 0),
    pygame.K_UP: (0, -5000),
    pygame.K_DOWN: (0, 5000),
}


def clip(val, minval, maxval):
    return min(max(val, minval), maxval)


class Player(gameobject.object):
    def __init__(self, image_file, startposX, startpoxY, gravity, resize):
        self.original_image = image_file
        self.player = super().__init__(image_file, startposX, startpoxY, True, resize)
        self.speed = [0, 0]
        area = self.screen.get_rect()
        self.width, self.height = area.width, area.height  # screen
        self.gravity = gravity  # world gravity
        self.Egravity = gravity  # current gravity
        self.jump = False

        self.pivot = pygame.Vector2(self.rect.midtop)
        self.grappling = False
        self.grappled_vine = None
        self.angle = 0
        self.angular_velocity = 5
        self.max_swing_angle = 45

    def Update(self, list):
        self.speed[1] += self.Egravity
        self.rect.move_ip(self.speed)
        # to not go outsize of the screen
        # usefull when no clipping
        self.rect.left = clip(self.rect.left, 0, self.width)
        self.rect.right = clip(self.rect.right, 0, self.width)
        self.rect.top = clip(self.rect.top, 0, self.height)
        self.rect.bottom = clip(self.rect.bottom, 0, self.height)
        self.collision(list)

        if self.grappling:

            swing_angle = sin(self.angle) * self.max_swing_angle
            self.angle += self.angular_velocity * self.dt
            if self.angle >= pi * 2:
                self.angle -= pi * 2

            # Calculate the position of the midbottom of the vine based on swing angle
            pivot_to_bottom = pygame.Vector2(0, 32).rotate(swing_angle)
            bottom_pos = self.pivot + pivot_to_bottom

            # Rotate the image around its center
            self.image = pygame.transform.rotate(self.original_image, -swing_angle)

            # Update the rect position to keep the midbottom at the calculated position
            self.rect = self.image.get_rect(center=bottom_pos)
            self.rect.midtop = (self.grappled_vine.rect.midbottom[0] - 15,
                                self.grappled_vine.rect.midbottom[1] - (self.rect.height / 3) * 2)
        else:
            self.angle = 0
            self.image = self.original_image

    def Movement(self, event, vines):
        if event.type == pygame.KEYDOWN:
            deltax, deltay = delta.get(event.key, (0, 0))
            self.speed[0] += deltax * self.dt * self.resize
            if self.jump:
                self.speed[1] = deltay * self.dt * self.resize
                self.jump = False
                self.Egravity = self.gravity
            if event.key == pygame.K_UP:
                self.try_graple_vine(vines)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.speed[0] = 0
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and self.speed[1] < 0:
                self.speed[1] = 0

    def Movementdebug(self, event):
        if event.type == pygame.KEYDOWN:
            deltax, deltay = delta.get(event.key, (0, 0))
            self.speed[0] = deltax // 250
            self.speed[1] = deltay // 500
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.speed[0] = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.speed[1] = 0

    def collision(self, list):  # non opti car AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        # it took like 15h to have it work correctly
        indexes = self.rect.collidelistall(list)
        if indexes and self.isSolid:
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
                    normTL = sqrt(vectorTopLeft[0] ** 2 + vectorTopLeft[1] ** 2)
                    normTR = sqrt(vectorTopRight[0] ** 2 + vectorTopRight[1] ** 2)
                    normBR = sqrt(vectorBottomRight[0] ** 2 + vectorBottomRight[1] ** 2)
                    normBL = sqrt(vectorBottomLeft[0] ** 2 + vectorBottomLeft[1] ** 2)

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
            self.Egravity = self.gravity

    def try_graple_vine(self, vines):
        vines_collided = pygame.sprite.spritecollide(self, vines, False)
        if self.grappled_vine in vines_collided:
            return

        if len(vines_collided) == 0:
            return

        self.grappled_vine = vines_collided[0]
        self.grappling = True
        self.speed[0] = 0

    def stop_grappling(self):
        if self.grappled_vine:
            self.grappled_vine.rect.center = (self.grappled_vine.original_center_x,
                                              self.grappled_vine.original_center_y)
            self.grappled_vine.angle = 0
            self.grappled_vine.image = self.grappled_vine.original_image

        self.grappled_vine = None
        self.grappling = False

    def is_grapling(self):
        return self.grappling
