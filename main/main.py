import pygame
"""
Uhh.
"""

# Initialize pygame
pygame.init()

# Set initial screen size
screen = pygame.display.set_mode((800, 600))

# Title and icons and stuff
pygame.display.set_caption("This is a test currently.")
icon = pygame.image.load('daniel.png')

pygame.display.set_icon(icon)

# Player set up
playerX = 370
playerY = 480
playerX_delta = 0
playerY_delta = 0
playerSpeed = 0.1
playerImg = icon

def player(x, y):
    screen.blit(icon, (x, y))

# Game loop
RUNNING = True
while RUNNING:

    screen.fill((0, 0, 0)) # Back ground color.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerY_delta -= playerSpeed
            if event.key  == pygame.K_s:
                playerY_delta += playerSpeed
            if event.key == pygame.K_a:
                playerX_delta -= playerSpeed
            if event.key == pygame.K_d:
                playerX_delta += playerSpeed

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_delta = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_delta = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerX = 370
                playerY = 480
    
    playerX += playerX_delta
    playerY += playerY_delta
    

    player(playerX, playerY)
    pygame.display.update()