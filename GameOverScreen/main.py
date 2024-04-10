import pygame
from screen import *
from imageButton import *
from tools import *


def GameOver():
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080

    WHITE = (255, 255, 255, 255)
    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT, "Level Editor")
    screen.CreateWindow()
    screen.SetBgColor(WHITE)

    imgReturn = pygame.image.load('assets/plainTxt/return.png')
    imgReturnHover = pygame.image.load('assets/hoverTxt/returnHover.png')

    imgQuit = pygame.image.load('assets/plainTxt/mainMenu.png')
    imgQuitHover = pygame.image.load('assets/hoverTxt/mainMenuHover.png')
    buttons = [ImageButton(750, 550, imgReturn.get_width(), imgReturn.get_height(), imgReturn, imgReturnHover, print("a")),
               ImageButton(750, 700, imgQuit.get_width(), imgQuit.get_height(), imgQuit, imgQuitHover, print('b'))]

    imgTitle = pygame.image.load('assets/plainTxt/gameOver.png')

    bgImg = pygame.image.load('assets/menu.png')
    menuBg = pygame.image.load('assets/bgTextured.png')
    while True:
        mousePos = pygame.mouse.get_pos()

        screen.SetBgImage(bgImg)
        screen.window.blit(menuBg, (CenterX(menuBg.get_width(), SCREEN_WIDTH), 100))
        screen.window.blit(imgTitle, (CenterX(imgTitle.get_width(), SCREEN_WIDTH), 240))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        for i in buttons:
            i.DisplayButton(screen)
            if i.IsHover(mousePos):
                i.SetDisplayedImage(1)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        i.Click()
            else:
                i.SetDisplayedImage(0)

        pygame.display.update()




