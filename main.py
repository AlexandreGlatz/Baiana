import pygame
import sys
import os
import player
import gameobject


gravity = .1
screensize = [1280, 720]
image_file = os.path.expanduser("asset/Untitled.png")

pygame.init()
pygame.time.Clock.tick(pygame.time.Clock(), 60)
screen = pygame.display.set_mode((screensize[0], screensize[1]), 0, 32)


class Main(object):
    def __init__(self):  # world
        self.screen = None
        self.player = None
        self.background = None
        self.listobstable = []
        self.setup()

    def setup(self):
        self.screen = screen
        self.player = player.Player(image_file, 50, 50, gravity)
        self.listobstable.append(gameobject.object(200, self.screen.get_height()-250, 50, 500, True))
        self.listobstable.append(gameobject.object(200, self.screen.get_height() - 50, 50, 50, True))
        self.listobstable.append(gameobject.object(500, self.screen.get_height() - 50, 50, 50, True))
        self.setup_background()

    def setup_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw()
        for i in self.listobstable:
            i.draw()
        pygame.display.flip()

    def event_loop(self):
        player = self.player
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                player.Movement(event)
            player.collision(self.listobstable)
            player.Update()
            print("Speed: ", self.player.speed, "Coll: ", player.coll)
            self.draw()
            pygame.time.delay(1)


if __name__ == '__main__':
    app = Main()
    app.event_loop()
