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
    screen.blit(playerImg, (x, y))


def jump():
    print("i jumped")

# Weathen images


weathen = spritesheet.spritesheet(scale(pygame.image.load("images\Weathen Spritesheet.png"), 800), 5, 5)

CENTER_HANDLE = 4

INDEX = 0

playerX_pos = cons.screenX / 2
playerY_pos = cons.screenY - (cons.screenY * 1 / 5)
playerX_pos_delta = 0
playerY_pos_delta = 0

# Game loop
DEBUG = False
RUNNING = True


while RUNNING:

    screen.fill(cons.LGREY)  # Back ground color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If quit is pressed in the upper left
            print("So long gay Bowser")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_pos_delta -= cons.playerSpeed
            if event.key == pygame.K_d:
                playerX_pos_delta += cons.playerSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_pos_delta = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                jump()
            if event.key == pygame.K_F1:
                DEBUG = not DEBUG

    playerX_pos += playerX_pos_delta
    playerY_pos += playerY_pos_delta

    debug_txt = font.render("", True, (0, 0, 0))

    if DEBUG:  # if debug is enabled
        debug_txt = font.render(str(playerX_pos), True, (0, 0, 255))

    # weathen.draw(screen, INDEX % weathen.totalCellCount,
    #             100, 100, CENTER_HANDLE)  # Draws in weathen

    INDEX += 1

    player(playerX_pos, playerY_pos)  # Places our player

    if cons.VSYNC:
        CLOCK.tick(cons.FPS)

    screen.blit(debug_txt, (900, 0))  # Places debug txt
    pygame.display.update()  # updates the screen
