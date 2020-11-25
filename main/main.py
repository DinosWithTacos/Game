import pygame
"""
Uhh.
"""

# Initialize pygame
pygame.init()

# Set initial screen size
screenX = 1920
screenY = 1080
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
playerImg = pygame.image.load('images\daniel.png')

font = pygame.font.SysFont(None, 24)


def player(x, y):
    screen.blit(icon, (x, y))

def jump():
    print("i jumped")

# Game loop
RUNNING = True
while RUNNING:
    screen.fill((0, 0, 0)) # Back ground color.

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
    
    if playerX_pos < screenX or playerX_pos > 0: # checks player is out of bounds
        playerX_pos += playerX_pos_delta
        playerY_pos += playerY_pos_delta
        pos_update = str(("PlayerX:", playerX_pos, "w/ delta", playerX_pos_delta))
        img = font.render(pos_update, True, (0, 0, 255))
        """        print("PlayerX:", playerX_pos, "w/ delta", playerX_pos_delta)
        print("PlayerY:", playerY_pos, "w/ delta", playerY_pos_delta)"""

    player(playerX_pos, playerY_pos)

    screen.blit(img, (20, 20))
    pygame.display.update()