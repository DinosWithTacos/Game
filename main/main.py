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
playerImg = icon

def player():
    screen.blit(icon, (playerX, playerY))

# Game loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False


    screen.fill((180, 180, 180))

    player()
    pygame.display.update()