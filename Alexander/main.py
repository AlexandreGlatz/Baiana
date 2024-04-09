import pygame
import sys
import math
from pygame.locals import *
from kayakClasses import *
from tools import *


def KayakLvl():
    pygame.init()
    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 720
    WHITE: [int] = (255, 255, 255)
    BLACK: [int] = (0, 0, 0)

    kayakScreen: KayakScreen = KayakScreen(SCREEN_WIDTH, SCREEN_HEIGHT, 10)
    kayakScreen.CreateWindow()
    kayakScreen.CreateWavesTable()

    kayakScreen.SetBgColor(WHITE)
    kayakScreen.DrawWaves(BLACK)

    isRunning: bool = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        pygame.display.update()

    pygame.quit()


KayakLvl()
