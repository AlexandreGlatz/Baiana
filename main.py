import json
import pygame
import sys
import playerani
import gameobject
import Camera

pygame.init()
screensize = pygame.display.set_mode().get_size()  # WindowBorderless
screen = pygame.display.set_mode(screensize, 0, 32)
level1 = json.load(open("level1.json"))


class Main(object):
    def __init__(self):  # world
        self.gravity = 1
        self.debug = False
        self.screen = None
        self.player = None
        self.background = None
        self.listobstable = []
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.level = level1
        self.camera = None
        self.setup()

    def setup(self):
        self.screen = screen
        self.player = playerani.Player(pygame.image.load("asset/basic.png"), 100, 500, self.gravity, .25)
        self.camera = Camera.Camera(self.player, self.screen.get_width(), self.screen.get_height())
        self.loadmap()
        self.setup_background()

    def loadmap(self):
        for i in self.level:
            self.listobstable.append(gameobject.object(pygame.image.load(i[0]), i[1], i[2], i[3], i[4]))

    def setup_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player.image, self.camera.apply(self.player.rect))
        for i in self.listobstable:
            self.screen.blit(i.image, self.camera.apply(i.rect))
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
                self.player.gravity = self.gravity
                self.player.Egravity = self.gravity
                self.debug = False
                print("DEBUG FALSE")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LALT and self.player.isSolid:
                self.player.isSolid = False
                print("COLLISION OFF")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LALT and not self.player.isSolid:
                self.player.isSolid = True
                print("COLLISION ON")

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

    def Update(self):
        self.player.Update(self.listobstable, self.fps)
        for i in self.listobstable:
            if i.__class__.__name__ == "shark":
                i.move()
        self.camera.update()

    def main(self):
        dttraget = 1000 / self.fps
        while 1:
            start = pygame.time.get_ticks()
            self.event_loop()
            self.Update()
            self.draw()
            end = pygame.time.get_ticks()
            dt = end - start
            if dt < dttraget:
                pygame.time.wait(int(dttraget - dt))
                dt = dttraget
            dt /= 1000
            self.givedt(dt)


if __name__ == '__main__':
    app = Main()
    app.main()
