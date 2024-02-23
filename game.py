import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
jumped = False
jump_toggle = False
dt = 0
jump_time = 0
game_width = screen.get_width() / 2
game_height = screen.get_height() / 2
player_pos = pygame.Vector2(game_width // 2, game_height)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jump_time += 1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    pygame.draw.circle(screen, "red", player_pos, 40)

    # gives smooth movement when player decides to jump
    if jumped:
        if not player_pos.y <= 0:
            player_pos.y -= 1500 * dt
        else:
            jumped = False

    # Handles player jumping
    keys = pygame.key.get_pressed()

    # allows player to jump every 1/6 seconds
    if jump_time % 10 == 0:
        jumped = False

    if not keys[pygame.K_SPACE]:
        jump_toggle = True

    if keys[pygame.K_SPACE] and not jumped and jump_toggle:
        jumped = True
        jump_time = 0
        jump_toggle = False

    # Handles the constant downwards drift of the player
    if not player_pos.y >= game_height * 2:
        player_pos.y += 400 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
