import pygame
import math
import random
from tools import *


class CircleCollider:
    # TODO: Arc Collider
    def __init__(self, startAngle: int, endAngle: int, radius: float):
        self.startAngle: int = startAngle
        self.endAngle: int = endAngle
        self.radius = radius

    def IsCollidingArc(self, collider):
        pass


class BoxCollider:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def IsCollidingRect(self, collider):
        return (self.x < collider.x + collider.width and
                self.x + self.width > collider.x and
                self.y < collider.y + collider.height and
                self.y + self.height > collider.y)


class PlayerInKayak(BoxCollider):

    def __init__(self, x: int, y: int, width: int, height: int):
        BoxCollider.__init__(x, y, width, height)
        self.vx: int = 0
        self.vy: int = 0
        self.isTouchingWater: bool = False

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def Move(self, moveSpeed: int):
        self.vx = moveSpeed

    def Accelerate(self, accelerateSpeed: int):
        self.vy = accelerateSpeed
        if self.isTouchingWater:
            self.vx = accelerateSpeed*2


# TODO: full screen
class Screen:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height
        self.window: pygame.display = None

    def CreateWindow(self):
        self.window = pygame.display.set_mode((self.width, self.height))

    def SetBgColor(self, color):
        self.window.fill(color)


class KayakScreen(Screen):
    def __init__(self, width, height, wavesAmount):
        Screen.__init__(self, width, height)
        self.wavesAmount = wavesAmount
        self.wavesTable = []

    def CreateWavesTable(self):

        for i in range(self.wavesAmount):
            self.wavesTable.append((-70, -290))
            self.wavesTable.append((110, 250))

    def DrawWaves(self, wavesColor):
        k = 0
        for i in range(self.wavesAmount):
            startAngle = self.wavesTable[i][0]
            endAngle = self.wavesTable[i][1]
            pygame.draw.arc(self.window, wavesColor, (i * 469, 500 - k, 500, 200),
                            DegToRad(startAngle), DegToRad(endAngle), 1)
            if k == 0:
                k = 70
            else:
                k = 0

# TODO: main menu
