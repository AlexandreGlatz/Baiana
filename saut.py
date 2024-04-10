import pygame

pygame.init()

# Window settings
wind_size = (800, 600)
screen = pygame.display.set_mode(wind_size)
pygame.display.set_caption('Saut mdrr ça rebondit')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Font loading
try:
    font = pygame.font.Font('Daydream.ttf', 25)
except FileNotFoundError:
    font = pygame.font.SysFont(None, 25)

# Player settings
player_pos = [400, 405]
player_speed = 400
jump_speed = -300
gravity = 8
in_jump = False
y_speed = 0
score = 0
score_pos = [25, 25]
on_vine = False
vine_pos = [600, 200]
vine_height = 200
angle = 0
swing_speed = 0.05
f_pressed = False

# Sprite sheet loading and resizing
sprite_sheet_path = 'run_sheet.png'
sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
scale_factor = 0.3

# Cutting sprite sheet frames
frame_width = 512
frame_height = 700
running_frames = [sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height)) for i in range(4)]

# Resizing frames
scaled_frame_width = int(frame_width * scale_factor)
scaled_frame_height = int(frame_height * scale_factor)
running_frames_scaled = [pygame.transform.scale(frame, (scaled_frame_width, scaled_frame_height)) for frame in running_frames]

# Variables for animation
current_frame = 0
last_update = pygame.time.get_ticks()
frame_rate = 100

# Clock to control FPS
clock = pygame.time.Clock()

running = True
is_moving = False
facing_right = True
while running:

    delta_time = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not on_vine:
        if keys[pygame.K_q]:
            is_moving = True
            facing_right = False
            player_pos[0] -= player_speed * delta_time
        elif keys[pygame.K_d]:
            is_moving = True
            facing_right = True
            player_pos[0] += player_speed * delta_time
        else:
            is_moving = False

        if keys[pygame.K_SPACE] and not in_jump:
            y_speed = jump_speed
            in_jump = True

    # Jump management
    if in_jump:
        y_speed += gravity
        player_pos[1] += y_speed * delta_time

        if player_pos[1] >=405:
            player_pos[1] = 405
            in_jump = False
            y_speed = 0

    # Update display
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (vine_pos[0] - 5, vine_pos[1], 10, vine_height))

    # Update player animation
    current_time = pygame.time.get_ticks()
    if not in_jump and not on_vine and is_moving:
        if current_time - last_update > frame_rate:
            last_update = current_time
            current_frame = (current_frame + 1) % len(running_frames_scaled)
    else:
        current_frame = 0

    # Player orientation management
    player_image = running_frames_scaled[current_frame]
    if not facing_right:
        player_image = pygame.transform.flip(player_image, True, False)

    # Player display
    player_image_rect = player_image.get_rect(center=(player_pos[0], player_pos[1]))
    screen.blit(player_image, player_image_rect)

    # Score display
    score_text = font.render(f'Score: {score}', True, GREEN)
    screen.blit(score_text, score_pos)

    # Display update
    pygame.display.flip()

pygame.quit()
