import pygame
import sys
import player
import gameobject

gravity = 1
screensize = [1280, 720]
image_file = pygame.image.load("asset/Untitled.png")
image_file2 = pygame.image.load("asset/plat.png")
image_file3 = pygame.image.load("asset/aaa2.png")
image_file32 = pygame.image.load("asset/aaa.png")
image_file4 = pygame.image.load("asset/mur.png")
image_file_water = pygame.image.load("asset/water-export.png")
pygame.init()
screen = pygame.display.set_mode((screensize[0], screensize[1]), 0, 32)


class Main(object):
    def __init__(self):  # world
        self.debug = False
        self.screen = None
        self.player = None
        self.background = None
        self.listobstable = []
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.setup()

    def setup(self):
        self.screen = screen
        self.player = player.Player(image_file, 97, 500, gravity)
        self.loadmap()
        self.setup_background()

    def loadmap(self):
        """for i in range((screensize[0] // image_file2.get_rect().width) + 1):
            self.listobstable.append(gameobject.object(image_file2, i * image_file2.get_rect().width,
                                                       self.screen.get_height() - 10, True))
            self.listobstable.append(gameobject.object(image_file2, i * image_file2.get_rect().width,
                                                       -image_file2.get_rect().height + 10, True))
        self.listobstable.append(gameobject.object(image_file3, 500, 300, True))
        self.listobstable.append(gameobject.object(image_file32, 750, 300, False))
        self.listobstable.append(gameobject.object(image_file4, 200, 200, True))"""
        self.listobstable.append(gameobject.object(image_file_water, 0, self.screen.get_height() - 10, True))
        self.listobstable.append(gameobject.shark(500, 400, 200, 2, True))

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

    def event_loop(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.debug:
                self.player.gravity = 0
                self.player.Egravity = 0
                self.debug = True
                print('DEBUG TRUE')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.debug:
                self.player.gravity = gravity
                self.player.Egravity = gravity
                self.debug = False
                print("DEBUG FALSE")

            if not self.debug:
                self.player.Movement(event, dt)
            else:
                self.player.Movementdebug(event)

    def main(self):
        dt = 0
        self.clock.tick(self.fps)
        while 1:
            self.event_loop(dt)
            self.player.Update(self.listobstable)
            self.draw()
            dt = self.clock.tick(self.fps) / 1000


if __name__ == '__main__':
    app = Main()
    app.main()
