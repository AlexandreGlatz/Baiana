import pygame
import gameobject
from math import sqrt

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
        self.player = super().__init__(image_file, startposX, startpoxY, True, resize)
        self.speed = [0, 0]
        area = self.screen.get_rect()
        self.width, self.height = area.width, area.height  # screen
        self.gravity = gravity  # world gravity
        self.Egravity = gravity  # current gravity
        self.jump = False

        # run
        sprite_sheet = pygame.image.load("asset/run_sheet.png").convert_alpha()
        frame_width = sprite_sheet.get_width() / 6
        frame_height = sprite_sheet.get_height()
        running_frames = [sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
                          for i in range(5)]
        scaled_frame_width = int(frame_width * resize)
        scaled_frame_height = int(frame_height * resize)

        self.running_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_width, scaled_frame_height)) for
                                      frame in running_frames]
        self.currentframeRun = 0
        self.last_update = 0
        self.idle = pygame.transform.smoothscale_by(image_file, resize)

        # jump
        jump_sheet = pygame.image.load("asset/jump-Sheet.png").convert_alpha()
        frame_j_width = jump_sheet.get_width() / 6
        frame_j_height = jump_sheet.get_height()
        jumping_frames = [jump_sheet.subsurface(pygame.Rect(i * frame_j_width, 0, frame_j_width, frame_j_height)) for i
                          in range(4)]

        scaled_frame_j_width = int(frame_j_width * resize)
        scaled_frame_j_height = int(frame_j_height * resize)
        self.jumping_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_j_width, scaled_frame_j_height)) for
                                      frame in jumping_frames]
        self.currentframeJump = 0

    def Update(self, list, fps):
        self.speed[1] += self.Egravity
        self.rect.move_ip(self.speed)
        # to not go outsize of the screen
        # usefull when no clipping
        """self.rect.left = clip(self.rect.left, 0, self.width)
        self.rect.right = clip(self.rect.right, 0, self.width)
        self.rect.top = clip(self.rect.top, 0, self.height)
        self.rect.bottom = clip(self.rect.bottom, 0, self.height)"""
        self.collision(list)

        if self.speed[0] > 0:
            self.facingL = False
        elif self.speed[0] < 0:
            self.facingL = True

        current_time = pygame.time.get_ticks()
        if self.jump and self.speed[0] != 0:  # not jumping
            if current_time - self.last_update > fps * 2:
                self.last_update = current_time
                self.currentframeRun = (self.currentframeRun + 1) % len(self.running_frames_scaled)
                self.image = self.running_frames_scaled[self.currentframeRun]
                if self.facingL:
                    self.image = pygame.transform.flip(self.image, True, False)
        elif self.jump and self.speed[0] == 0:  # not moving and not jumping
            self.image = self.idle
            if self.facingL:
                self.image = pygame.transform.flip(self.image, True, False)
        elif not self.jump and self.speed[0] != 0:  # jumping and moveing
            if current_time - self.last_update > fps:
                self.last_update = current_time
                self.currentframeJump = (self.currentframeJump + 1) % len(self.jumping_frames_scaled)
                self.image = self.jumping_frames_scaled[self.currentframeJump]
                if self.facingL:
                    self.image = pygame.transform.flip(self.image, True, False)

    def Movement(self, event):
        if event.type == pygame.KEYDOWN:
            deltax, deltay = delta.get(event.key, (0, 0))
            self.speed[0] += deltax * self.dt * self.resize
            if self.jump:
                self.speed[1] = deltay * self.dt * self.resize
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

    def draw(self):
        self.rect.height = self.image.get_height()
        self.rect.width = self.image.get_width()
        self.screen.blit(self.image, self.rect)
