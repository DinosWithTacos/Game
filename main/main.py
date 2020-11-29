import pygame
import sys
import cons
import spritesheet

# Initialize pygame and general settings
CLOCK = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((cons.screenX, cons.screenY))
pygame.display.set_icon(cons.icon)


def scale(sur, sclar):
    """Changes cale of pygame.surface objects

    Args:
        Sur (pygame.surface): PyGame surface you want to change scale of
        Sclar (int): Scale of object you want to affect by

    Returns:
        pygame.surface: Scaled pygame.surface
    """
    return pygame.transform.scale(sur, (sclar, sclar))


playerImg = scale(pygame.image.load('images\daniel.png'), 100)

evil_fuck_img = scale(pygame.image.load("images\weathin.png"), 100)

font = pygame.font.SysFont(None, 24)


def player(x, y):
    # screen.blit(playerImg, (x, y))
    pass


def jump():
    print("i jumped")


def quit_():
    print("So long gay Bowser")
    pygame.quit()
    sys.exit()

# Weathen images


weathen = spritesheet.spritesheet(
    scale(pygame.image.load("images\Weathen Spritesheet.png"), 800), 5, 5)

player_runnning_img = spritesheet.spritesheet(
    scale(pygame.image.load("images\wipsprite (1).png"), 500), 3, 2)

CENTER_HANDLE = 4

INDEX = 0
animationINDEX = 0
isMoving = False

playerX_pos = cons.screenX / 2
playerY_pos = cons.screenY - (cons.screenY * 1 / 5)
playerXL_pos_delta = 0
playerXR_pos_delta = 0
playerY_pos_delta = 0

last_drawn_index = animationINDEX % player_runnning_img.totalCellCount


# Game loop
RUNNING = True


while RUNNING:

    player_runnning_img.draw(screen, last_drawn_index,
                             playerX_pos, playerY_pos, CENTER_HANDLE)

    screen.fill(cons.LGREY)  # Back ground color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If quit is pressed in the upper left
            quit_()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerXL_pos_delta -= cons.playerSpeed
            if event.key == pygame.K_d:
                player_runnning_img.draw(screen, last_drawn_index,
                                         playerX_pos, playerY_pos, CENTER_HANDLE)
                playerXR_pos_delta += cons.playerSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                playerXL_pos_delta = 0
            if event.key == pygame.K_d:
                last_drawn_index = animationINDEX % player_runnning_img.totalCellCount
                playerXR_pos_delta = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                jump()
            if event.key == pygame.K_F1:
                cons.DEBUG = not cons.DEBUG
            if event.key == pygame.K_ESCAPE:
                quit_()

    playerX_pos += playerXL_pos_delta
    playerX_pos += playerXR_pos_delta
    playerY_pos += playerY_pos_delta

    total_player_delta = playerXL_pos_delta + \
        playerXR_pos_delta + playerY_pos_delta

    debug_txt = font.render("", True, (0, 0, 0))

    debug_info = str((playerX_pos, round(CLOCK.get_fps(), 3)))
    debug_info = [playerX_pos, total_player_delta, round(CLOCK.get_fps(), 3), last_drawn_index]

    if cons.DEBUG:  # if debug is enabled
        debug_txt = font.render(str(debug_info), True, (0, 0, 255))

    # weathen.draw(screen, INDEX % weathen.totalCellCount,
    #             100, 100, 1, True, CENTER_HANDLE)  # Draws in weathen

    INDEX += 1
    if INDEX % cons.animationFPS == 0:
        animationINDEX += 1

    player(playerX_pos, playerY_pos)  # Places our player

    if cons.VSYNC:
        CLOCK.tick(cons.FPS)

    screen.blit(debug_txt, (900, 0))  # Places debug txt
    pygame.display.update()  # updates the screen
