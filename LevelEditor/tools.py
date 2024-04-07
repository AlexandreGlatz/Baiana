def PlaceTile( screen, tileButton, mousePos):
    screen.window.blit(tileButton.image, (mousePos[0], mousePos[1]))