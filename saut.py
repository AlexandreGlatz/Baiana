import pygame
import sys
import math

pygame.init()
pygame.mixer.init()

#Music
pygame.mixer.music.load('Gerudo Valley - The Legend of Zelda Ocarina Of Time.mp3')
pygame.mixer.music.play(-1)

# Window settings
wind_size = (800, 600)
screen = pygame.display.set_mode(wind_size)
pygame.display.set_caption('Saut mdrr ça rebondit')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Font loading
try:
    font = pygame.font.Font('Daydream.ttf', 25)
except FileNotFoundError:
    font = pygame.font.SysFont(None, 25)

# Sprite sheet loading and resizing
sprite_sheet_path = 'run_sheet.png'
sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
scale_factor = 0.3

jump_sheet_path = 'jump-Sheet.png'
jump_sheet = pygame.image.load(jump_sheet_path).convert_alpha()

# Cutting sprite sheet frames
frame_width = 512
frame_height = 700
running_frames = [sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height)) for i in range(4)]

frame_j_width = 500
frame_j_height = 700
jumping_frames = [jump_sheet.subsurface(pygame.Rect(i * frame_j_width, 0, frame_j_width, frame_j_height)) for i in range(5)]

# Resizing frames
scaled_frame_width = int(frame_width * scale_factor)
scaled_frame_height = int(frame_height * scale_factor)
running_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_width, scaled_frame_height)) for frame in running_frames]

scaled_frame_j_width = int(frame_j_width * scale_factor)
scaled_frame_j_height = int(frame_j_height * scale_factor)
jumping_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_j_width, scaled_frame_j_height)) for frame in jumping_frames]

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, running_frames, jumping_frames):
        super().__init__()
        self.frames = running_frames
        self.current_frame = 1
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pos
        self.speed = 400
        self.jump_speed = -70
        self.gravity = 5
        self.y_speed = 0
        self.in_jump = False
        self.facing_right = True
        self.is_moving = False
        self.animation_time = 0.15
        self.current_time = 0
        self.running_frames = running_frames
        self.jumping_frames = jumping_frames

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.vx, self.vy = 0, self.y_speed
        self.is_moving = False

        if keys[pygame.K_q]:
            self.vx = -self.speed * dt
            self.facing_right = False
            self.is_moving = True
        if keys[pygame.K_d]:
            self.vx = self.speed * dt
            self.facing_right = True
            self.is_moving = True

        if keys[pygame.K_SPACE] and not self.in_jump:
            self.vy = self.jump_speed
            self.in_jump = True

        if self.in_jump:
            self.vy += self.gravity
            if self.pos[1] >= 405:
                self.pos[1] = 405
                self.in_jump = False
                self.y_speed = 0
                self.frames = self.running_frames
            else:
                self.frames = self.jumping_frames

        self.pos[0] += self.vx
        self.pos[1] += self.vy
        self.rect.topleft = self.pos

        # Update animation based on movement and elapsed time
        if self.is_moving and not self.in_jump:
            self.current_time += dt
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
                if not self.facing_right:
                    self.image = pygame.transform.flip(self.image, True, False)
        elif self.in_jump:
            self.current_time += dt
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
                if not self.facing_right:
                    self.image = pygame.transform.flip(self.image, True, False)

# Camera class
class Camera:
    def __init__(self, follow_target, width, height):
        self.target = follow_target
        self.rect = pygame.Rect(0, 0, width, height)
        self.smooth_speed = 0.1

    def update(self):
        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        self.rect.x += int(dx * self.smooth_speed)
        self.rect.y += int(dy * self.smooth_speed)

    def apply(self, entity):
        if isinstance(entity, pygame.Rect):
            return entity.move(-self.rect.topleft[0], -self.rect.topleft[1])
        else:
            return entity.rect.move(-self.rect.topleft[0], -self.rect.topleft[1])

player = Player([400, 405], running_frames_scaled, jumping_frames_scaled)
camera = Camera(player, wind_size[0], wind_size[1])
all_sprites = pygame.sprite.Group(player)

# Decor element (static)
decor_element = pygame.Surface((100, 50))
decor_element.fill(WHITE)
decor_rect = decor_element.get_rect(center=(wind_size[0] // 2, wind_size[1] // 2))

running = True
clock = pygame.time.Clock()

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)
    camera.update()

    screen.fill(BLACK)

    decor_position = camera.apply(decor_rect)
    screen.blit(decor_element, decor_position)

    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))

    score_text = font.render(f'Score: 0', True, GREEN)
    screen.blit(score_text, (25, 25))

    pygame.display.flip()

pygame.quit()