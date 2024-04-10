import pygame
import math
import gameobject


class Vine(gameobject.object):
    def __init__(self, x, y):
        self.original_image = pygame.image.load('liane.png')
        super().__init__(self.original_image, x, y, False, 1)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.pivot = pygame.Vector2(self.rect.midtop)  # Pivot at the top of the vine
        self.angle = 0
        self.length = 32  # Length of the vine
        self.angular_velocity = 5  # Angular velocity of swinging
        self.max_swing_angle = 45  # Maximum swing angle in degrees
        self.original_center_x = x
        self.original_center_y = y
        self.dt = 0

    def update(self, player):
        if player.is_grapling() and self == player.grappled_vine:
            # Calculate swing angle based on sine function for a pendulum
            swing_angle = math.sin(self.angle) * self.max_swing_angle
            self.angle += self.angular_velocity * self.dt
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

    def draw(self):
        self.screen.blit(self.image, self.rect)
