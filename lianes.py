import pygame
import sys
from pygame.locals import *
import math

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Jeu de Lianes')

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
# Chargement de l'image du joueur
class Player(pygame.sprite.Sprite):
    def __init__(self,starting_angle=0):
        super().__init__()
        self.original_image = pygame.image.load('player.png')
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (100, WINDOW_HEIGHT - 100)
        self.velocity_x = 0
        self.velocity_y = 0  # Ajout de la vitesse verticale
        self.gravity = 0.5
        self.pivot = pygame.Vector2(self.rect.midtop)  # Pivot at the top of the vine
        self.jumping = False
        self.grappling = False  # Indicateur si le joueur est accroché à une liane
        self.grappled_vine = None  # Référence à la liane à laquelle le joueur est accroché
        self.angle = starting_angle
        self.length = 32  # Length of the vine
        self.angular_velocity = 5  # Angular velocity of swinging
        self.max_swing_angle = 45  # Maximum swing angle in degrees
    def update(self, dt):
        
        # Si le joueur est accroché à une liane
        if self.grappling:
            
            swing_angle = math.sin(self.angle) * self.max_swing_angle
            self.angle += self.angular_velocity * dt
            if self.angle >= math.pi * 2:
                self.angle -= math.pi * 2

            # Calculate the position of the midbottom of the vine based on swing angle
            pivot_to_bottom = pygame.Vector2(0, self.length).rotate(swing_angle)
            bottom_pos = self.pivot + pivot_to_bottom

            # Rotate the image around its center
            self.image = pygame.transform.rotate(self.original_image, -swing_angle)

            # Update the rect position to keep the midbottom at the calculated position
            self.rect = self.image.get_rect(center=bottom_pos)
            self.rect.midtop = (self.grappled_vine.rect.midbottom[0]-15,self.grappled_vine.rect.midbottom[1]-(self.rect.height/3)*2)
        else:
            self.angle = 0
            self.image = self.original_image

        # Déplacement horizontal du joueur
        self.rect.x += self.velocity_x * dt

        # Déplacement vertical du joueur
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y * dt

        # Limiter le joueur en bas de l'écran
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.stop_jump()

        # Limiter le joueur en haut de l'écran (facultatif)
        if self.rect.top <= 0:
            self.rect.top = 0

        # Limiter le joueur à l'intérieur de l'écran en horizontal
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def jump(self):
        if self.jumping:
            return

        # Permet de sauter même lorsque le joueur est accroché
        self.jumping = True
        self.velocity_y = -1000
        self.gravity = 50

        self.stop_grappling()  # Arrêter l'accrochage à la liane

    def stop_jump(self):
        if self.jumping == False:
            return

        self.jumping = False
        self.velocity_y = 0  # Arrêter la chute verticale
        self.gravity = 0  # Arrêter la gravité

    def try_graple_vine(self, vines):
        if self.jumping == False:
            return

        vines_collided = pygame.sprite.spritecollide(self, vines, False)
        if self.grappled_vine in vines_collided:
            return

        if len(vines_collided) == 0:
            return

        self.stop_jump()

        self.grappled_vine = vines_collided[0]
        self.grappling = True
        self.velocity_x = 0

    def stop_grappling(self):
        if self.grappled_vine:
            self.grappled_vine.rect.center = (self.grappled_vine.original_center_x, self.grappled_vine.original_center_y)
            self.grappled_vine.angle = 0
            self.grappled_vine.image = self.grappled_vine.original_image

        self.grappled_vine = None
        self.grappling = False

    def is_grapling(self):
        return self.grappling


class Vine(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.image.load('liane.png')
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.pivot = pygame.Vector2(self.rect.midtop)  # Pivot at the top of the vine
        self.angle = 0
        self.length = 32  # Length of the vine
        self.angular_velocity = 5  # Angular velocity of swinging
        self.max_swing_angle = 45  # Maximum swing angle in degrees
        self.original_center_x = x
        self.original_center_y = y
    def update(self, player, dt):
        
        if player.is_grapling() and self == player.grappled_vine:
            # Calculate swing angle based on sine function for a pendulum
            swing_angle = math.sin(self.angle) * self.max_swing_angle
            self.angle += self.angular_velocity * dt
            if self.angle >= math.pi * 2:
                self.angle -= math.pi * 2

            # Calculate the position of the midbottom of the vine based on swing angle
            pivot_to_bottom = pygame.Vector2(0, self.length).rotate(swing_angle)
            bottom_pos = self.pivot + pivot_to_bottom

            # Rotate the image around its center
            self.image = pygame.transform.rotate(self.original_image, -swing_angle)

            # Update the rect position to keep the midbottom at the calculated position
            self.rect = self.image.get_rect(center=bottom_pos)
        else:
            self.angle = 0
            self.image = self.original_image
            
       
         











background_image = pygame.image.load('black.jpg')
platform = pygame.Surface((150,20))

def main():
    player = Player()

    vines = pygame.sprite.Group()
    vines.add(Vine(200, 300))
    vines.add(Vine(300, 300))  # Exemple de liane

    

    dt = 0
    targetFPS = 60
    dtTarget = 1000 / targetFPS

    while True:
        start = pygame.time.get_ticks()

        WINDOW.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if player.is_grapling() == False:
                    if event.key == K_LEFT:
                        player.velocity_x = -300
                    elif event.key == K_RIGHT:
                        player.velocity_x = 300

                if event.key == K_SPACE:
                    if player.jumping:
                        player.try_graple_vine(vines)
                    else:
                        player.jump()  # Autoriser le saut lorsque le joueur se détache de la liane

            elif event.type == KEYUP:
                if event.key == K_LEFT and player.velocity_x < 0:
                    player.velocity_x = 0
                elif event.key == K_RIGHT and player.velocity_x > 0:
                    player.velocity_x = 0

        # Déplacement vertical du joueur
        player.update(dt)

        # Déplacement des lianes
        vines.update(player, dt)

        # Affichage des sprites
        for vine in vines:
            WINDOW.blit(vine.image, vine.rect)
        if player.is_grapling():
            WINDOW.blit(player.image, player.rect)
        else:
            WINDOW.blit(player.original_image, player.rect)
            # Réinitialisation de la position et de l'image de la liane
            vine.rect.center = (vine.original_center_x, vine.original_center_y)
            vine.angle = 0
            vine.image = vine.original_image
        
   
        pygame.display.update()

        end = pygame.time.get_ticks()
        dt = end - start
        if dt < dtTarget:
            pygame.time.wait(int(dtTarget - dt))
            dt = dtTarget

        dt /= 1000


if __name__ == "__main__":
    main()
