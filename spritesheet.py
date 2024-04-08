import pygame
import sys

pygame.init()

win_width, win_height = 500, 500
win = pygame.display.set_mode((win_width, win_height))

# Chargez le spritesheet
spritesheet = pygame.image.load("spritesheet.png")  # Assurez-vous de mettre le bon chemin vers votre fichier spritesheet

# Définissez les dimensions de chaque image dans le spritesheet
sprite_width, sprite_height = 60, 60

# Créez une classe ou une structure pour gérer les animations du sprite
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.current_frame = 0
        self.animation_speed = 0.1
        self.frames = []  # Une liste pour stocker les images extraites du spritesheet
        self.extract_frames()

    def extract_frames(self):
        # Extrayez les images individuelles du spritesheet et stockez-les dans la liste des frames
        for i in range(4):  # Par exemple, si vous avez 4 images dans votre spritesheet pour une animation
            frame = spritesheet.subsurface(pygame.Rect(i * sprite_width, 0, sprite_width, sprite_height))
            self.frames.append(frame)

    def update(self):
        # Mettez à jour l'animation du sprite
        self.current_frame += self.animation_speed
        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def draw(self, surface):
        # Dessinez le sprite sur la surface spécifiée
        surface.blit(self.frames[int(self.current_frame)], (self.x, self.y))

player = Player(200, 200)

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    win.fill((0, 0, 0))
    player.draw(win)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
