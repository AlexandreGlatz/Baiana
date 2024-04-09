import pygame
import sys
import player
import gameobject
"""
linked to player and gameobject

escape to quit
space to debug mode
"""
gravity = 1
image_file = pygame.image.load("asset/basic.png")
image_file2 = pygame.image.load("asset/plat.png")
image_file3 = pygame.image.load("asset/aaa2.png")
image_file32 = pygame.image.load("asset/aaa.png")
image_file4 = pygame.image.load("asset/mur.png")
image_file_water = pygame.image.load("asset/water-export.png")
pygame.init()
screensize = pygame.display.set_mode().get_size()  # WindowBorderless
screen = pygame.display.set_mode(screensize, 0, 32)


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
        self.player = player.Player(image_file, 100, 500, gravity, .25)
        self.loadmap()
        self.setup_background()

    def loadmap(self):
        for i in range((screensize[0] // image_file2.get_rect().width) + 1):
            self.listobstable.append(gameobject.object(image_file2, i * image_file2.get_rect().width,
                                                       self.screen.get_height() - 10, True, 1))
            self.listobstable.append(gameobject.object(image_file2, i * image_file2.get_rect().width,
                                                       -image_file2.get_rect().height + 10, True, 1))

        self.listobstable.append(gameobject.object(image_file_water,
                                                   self.screen.get_width() - image_file_water.get_rect().width,
                                                   self.screen.get_height() - 10, True, 1))
        self.listobstable.append(gameobject.shark(screensize[0] * .8, self.screen.get_height() - 50, 50, 200, 200,
                                                  True, .2))
        self.listobstable.append(gameobject.object(image_file3, 200, 200, True, 1))
        self.listobstable.append(gameobject.object(image_file32, 400, 200, False, 1))

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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
                self.player.Movement(event)
            else:
                self.player.Movementdebug(event)

    def givedt(self, dt):
        self.player.dt = dt
        for i in self.listobstable:
            try:
                if i.__getattribute__("speed"):
                    i.dt = dt
            except AttributeError:
                pass

    def main(self):
        dt = 1
        self.clock.tick(self.fps)
        while 1:
            self.event_loop()
            self.player.Update(self.listobstable)
            self.draw()
            self.givedt(dt)
            dt = self.clock.tick(self.fps) / 1000


if __name__ == '__main__':
    app = Main()
    app.main()
