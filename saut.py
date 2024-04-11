import pygame
import sys
import math

pygame.init()
pygame.mixer.init()

#Music
pygame.mixer.music.load('Gerudo Valley - The Legend of Zelda Ocarina Of Time.mp3')
pygame.mixer.music.play(-1)

# Window settings
wind_size = (1920, 1080)
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
scale_m_factor = 0.4
scale_m2_factor = 0.4
scale_d_factor = 0.4
scale_d2_factor = 0.4
scale_d3_factor = 0.4

jump_sheet_path = 'jump-Sheet.png'
jump_sheet = pygame.image.load(jump_sheet_path).convert_alpha()

villain_sheet_path ='mechant.png'
villain_sheet = pygame.image.load(villain_sheet_path).convert_alpha()

villain2_sheet_path ='mechant2.png'
villain2_sheet = pygame.image.load(villain2_sheet_path).convert_alpha()

dancer_sheet_path = 'dancer.png'
dancer_sheet = pygame.image.load(dancer_sheet_path).convert_alpha()

dancer2_sheet_path = 'dancer2.png'
dancer2_sheet = pygame.image.load(dancer2_sheet_path).convert_alpha()

dancer3_sheet_path = 'dancer3.png'
dancer3_sheet = pygame.image.load(dancer3_sheet_path).convert_alpha()

# Cutting sprite sheet frames
frame_width = 512
frame_height = 700
running_frames = [sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height)) for i in range(4)]

    #jump
frame_j_width = 500
frame_j_height = 700
jumping_frames = [jump_sheet.subsurface(pygame.Rect(i * frame_j_width, 0, frame_j_width, frame_j_height)) for i in range(5)]

    #mechant
frame_m_width = 200
frame_m_height = 700
mechant_frames = [villain_sheet.subsurface(pygame.Rect(i * frame_m_width, 0, frame_m_width, frame_m_height)) for i in range(13)]

    #mechant2
frame_m2_width = 200
frame_m2_height = 700
mechant2_frames = [villain2_sheet.subsurface(pygame.Rect(i * frame_m2_width, 0, frame_m2_width, frame_m2_height)) for i in range(13)]

    #dancer
frame_d_width = 210
frame_d_height = 700
dancer_frames = [dancer_sheet.subsurface(pygame.Rect(i * frame_d_width, 0, frame_d_width, frame_d_height)) for i in range(2)]

    #dancer2
frame_d2_width = 210
frame_d2_height = 700
dancer2_frames = [dancer2_sheet.subsurface(pygame.Rect(i * frame_d2_width, 0, frame_d2_width, frame_d2_height)) for i in range(2)]

    #dancer3
frame_d3_width = 210
frame_d3_height = 700
dancer3_frames = [dancer3_sheet.subsurface(pygame.Rect(i * frame_d3_width, 0, frame_d3_width, frame_d3_height)) for i in range(2)]

# Resizing frames
scaled_frame_width = int(frame_width * scale_factor)
scaled_frame_height = int(frame_height * scale_factor)
running_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_width, scaled_frame_height)) for frame in running_frames]

    #jump
scaled_frame_j_width = int(frame_j_width * scale_factor)
scaled_frame_j_height = int(frame_j_height * scale_factor)
jumping_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_j_width, scaled_frame_j_height)) for frame in jumping_frames]

    #mechant
scaled_frame_m_width = int(frame_m_width * scale_m_factor)
scaled_frame_m_height = int(frame_m_height * scale_m_factor)
mechant_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_m_width, scaled_frame_m_height)) for frame in mechant_frames]

    #mechant2
scaled_frame_m2_width = int(frame_m2_width * scale_m2_factor)
scaled_frame_m2_height = int(frame_m2_height * scale_m2_factor)
mechant2_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_m2_width, scaled_frame_m2_height)) for frame in mechant2_frames]

    #dancer
scaled_frame_d_width = int(frame_d_width * scale_d_factor )
scaled_frame_d_height = int(frame_d_height * scale_d_factor)
dancer_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_d_width, scaled_frame_d_height)) for frame in dancer_frames]

    #dancer2
scaled_frame_d2_width = int(frame_d2_width * scale_d2_factor)
scaled_frame_d2_height = int(frame_d2_height * scale_d2_factor)
dancer2_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_d2_width, scaled_frame_d2_height)) for frame in dancer2_frames]

    #dancer3
scaled_frame_d3_width = int(frame_d3_width * scale_d3_factor)
scaled_frame_d3_height = int(frame_d3_height * scale_d3_factor)
dancer3_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_d3_width, scaled_frame_d3_height)) for frame in dancer3_frames]

all_sprites = pygame.sprite.Group()

# Villain Class
class Villain(pygame.sprite.Sprite):
    def __init__(self, pos, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_time = 0.15
        self.current_time = 0

    def update(self, dt):
        # Animation loop
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

villain = Villain([400, 50], mechant_frames_scaled)

all_sprites.add(villain)

# Villain2 Class
class Villain2(pygame.sprite.Sprite):
    def __init__(self, pos, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_time = 0.15
        self.current_time = 0

    def update(self, dt):
        # Animation loop
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

villain2 = Villain2([300, 50], mechant2_frames_scaled)

all_sprites.add(villain2)

# Dancer Class
class Dancer(pygame.sprite.Sprite):
    def __init__(self, pos, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_time = 0.15
        self.current_time = 0

    def update(self, dt):
        # Animation loop
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

dancer = Dancer([200, 50], dancer_frames_scaled)

all_sprites.add(dancer)

# Dancer2 Class
class Dancer2(pygame.sprite.Sprite):
    def __init__(self, pos, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_time = 0.15
        self.current_time = 0

    def update(self, dt):
        # Animation loop
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

dancer2 = Dancer2([100, 50], dancer2_frames_scaled)

all_sprites.add(dancer2)

# Dancer3 Class
class Dancer3(pygame.sprite.Sprite):
    def __init__(self, pos, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.animation_time = 0.15
        self.current_time = 0

    def update(self, dt):
        # Animation loop
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

dancer3 = Dancer3([0, 50], dancer3_frames_scaled)

all_sprites.add(dancer3)

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
        self.vx = 0
        self.vy = 0

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
        if isinstance(entity, pygame.sprite.Sprite):
            return entity.rect.move(-self.rect.topleft[0], -self.rect.topleft[1])
        elif isinstance(entity, pygame.Rect):
            return entity.move(-self.rect.topleft[0], -self.rect.topleft[1])
        else:
            return entity.move(-self.rect.topleft[0], -self.rect.topleft[1])

player = Player([400, 405], running_frames_scaled, jumping_frames_scaled)
all_sprites.add(player)
camera = Camera(player, wind_size[0], wind_size[1])

class BackgroundElement(pygame.sprite.Sprite):
    def __init__(self, image, pos, parallax_speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.parallax_speed = parallax_speed
        self.width = image.get_width()

    def update(self, camera_speed):
        self.rect.x += camera_speed * self.parallax_speed

        if self.rect.left > wind_size[0]:
            self.rect.right = 0

        if self.rect.right < 0:
            self.rect.left = wind_size[0]

# parallax
bg_far_path = 'background_3.png'
bg_near_path = 'backg_2.png'

bg_far_image = pygame.image.load(bg_far_path).convert_alpha()
bg_near_image = pygame.image.load(bg_near_path).convert_alpha()

# Initialization of backgrounds
bg_far1 = BackgroundElement(bg_far_image, (0, 0), 0.5)
bg_far2 = BackgroundElement(bg_far_image, (bg_far_image.get_width(), 0), 0.5)
bg_near1 = BackgroundElement(bg_near_image, (0, 0), 1)
bg_near2 = BackgroundElement(bg_near_image, (bg_near_image.get_width(), 0), 1)

background_elements = pygame.sprite.Group(bg_far1, bg_far2, bg_near1, bg_near2)

# Decor element (static)
decor_element = pygame.Surface((100, 50))
decor_element.fill(WHITE)
decor_rect = decor_element.get_rect(center=(wind_size[0] // 2, wind_size[1] // 2))

running = True
clock = pygame.time.Clock()

while running:
    dt = clock.tick(60) / 1000

    direction = -1 if player.vx > 0 else 1 if player.vx < 0 else 0
    camera_speed = player.speed * dt * direction
    background_elements.update(camera_speed)

    screen.fill(BLACK)
    for element in background_elements:
        screen.blit(element.image, element.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update(dt)
    camera.update()

    decor_position = camera.apply(decor_rect)
    screen.blit(decor_element, decor_position)

    for sprite in all_sprites:
        screen.blit(sprite.image, camera.apply(sprite))

    score_text = font.render(f'Score: 0', True, GREEN)
    screen.blit(score_text, (25, 25))

    pygame.display.flip()

pygame.quit()