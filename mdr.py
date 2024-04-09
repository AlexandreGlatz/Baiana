import pygame as pg
from pygame.math import Vector2


pg.init()
screen = pg.display.set_mode((640, 480))
screen_rect = screen.get_rect()

FONT = pg.font.Font(None, 24)
BULLET_IMAGE = pg.Surface((20, 11), pg.SRCALPHA)
pg.draw.polygon(BULLET_IMAGE, pg.Color('aquamarine1'),
                [(0, 0), (20, 5), (0, 11)])


class Bullet(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super().__init__()
        self.image = pg.transform.rotate(BULLET_IMAGE, -angle)
        self.rect = self.image.get_rect(center=pos)
        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(40, 0).rotate(angle)
        # Then add the offset vector to the position vector.
        self.pos = Vector2(pos) + offset  # Center of the sprite.
        # Rotate the direction vector (1, 0) by the angle.
        # Multiply by desired speed.
        self.velocity = Vector2(1, 0).rotate(angle) * 9

    def update(self):
        self.pos += self.velocity  # Add velocity to pos to move the sprite.
        self.rect.center = self.pos  # Update rect coords.

        if not screen_rect.contains(self.rect):
            self.kill()


def main():
    clock = pg.time.Clock()
    cannon_img = pg.Surface((40, 20), pg.SRCALPHA)
    cannon_img.fill(pg.Color('aquamarine3'))
    cannon = cannon_img.get_rect(center=(320, 240))
    angle = 0
    bullet_group = pg.sprite.Group()  # Add bullets to this group.

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Left button fires a bullet from center with
                # current angle. Add the bullet to the bullet_group.
                if event.button == 1:
                    bullet_group.add(Bullet(cannon.center, angle))

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            angle -= 3
        elif keys[pg.K_d]:
            angle += 3
        if keys[pg.K_SPACE]:
            bullet_group.add(Bullet(cannon.center, angle))

        # Rotate the cannon image.
        rotated_cannon_img = pg.transform.rotate(cannon_img, -angle)
        cannon = rotated_cannon_img.get_rect(center=cannon.center)

        bullet_group.update()

        # Draw
        screen.fill((30, 40, 50))
        screen.blit(rotated_cannon_img, cannon)
        bullet_group.draw(screen)
        txt = FONT.render('angle {:.1f}'.format(angle), True, (150, 150, 170))
        screen.blit(txt, (10, 10))
        pg.display.update()

        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()