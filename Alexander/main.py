import pygame
import sys
import math
from pygame.locals import *
import classes


def DegToRad(angle):

    return (angle+90)/57


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (0, 0, 0)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
isRunning = True
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    pygame.draw.arc(window, WHITE, (50, 50, 50, 50), DegToRad(0), DegToRad(180), 1)
    pygame.display.update()





