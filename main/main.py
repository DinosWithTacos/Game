import pygame
"""
Uhh.
"""

# Initialize pygame
pygame.init()

# Set initial screen size
screenX = 1920
screenY = 1080

VSync = False
debug = False

if VSync:
    pygame.time.Clock.tick = 60

screen = pygame.display.set_mode((screenX, screenY))

# Title and icons and stuff
pygame.display.set_caption("This is a test currently.")
icon = pygame.image.load('images\daniel.png')

pygame.display.set_icon(icon)

# Player set up, starting pos and velocity
playerX_pos = screenX / 2 
playerY_pos = 900
playerX_pos_delta = 0
playerY_pos_delta = 0
playerSpeed = 5



def scale(Sur, Sclar):
    return pygame.transform.scale(Sur, (Sclar, Sclar))

playerImg = scale(pygame.image.load('images\daniel.png'), 100)

evil_fuck_img = scale(pygame.image.load("images\weathin.png"), 100)

font = pygame.font.SysFont(None, 24)


def player(x, y):
    screen.blit(playerImg, (x, y))

def jump():
    print("i jumped")


def weathen(x, y):

    screen.blit(evil_fuck_img, (x, y))

# Game loop
RUNNING = True
while RUNNING:
    screen.fill((200, 200, 200)) # Back ground color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If quit is pressed in the upper left
            RUNNING = False
            print("So long gay Bowser")
            break
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_pos_delta -= playerSpeed
            if event.key == pygame.K_d:
                playerX_pos_delta += playerSpeed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_pos_delta = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                jump()
            if event.key == pygame.K_F1:
                debug = not debug
    
    if playerX_pos < screenX or playerX_pos > 0: # checks player is out of bounds
        playerX_pos += playerX_pos_delta
        playerY_pos += playerY_pos_delta
    
    debug_txt = font.render("", True, (0,0,0))

    if debug:
        debug_txt = font.render(str(playerX_pos), True, (0, 0, 255))


    player(playerX_pos, playerY_pos) # Places our player
    weathen(20, 20)



    screen.blit(debug_txt, (900, 0))
    pygame.display.update()