import pygame

# Display information
screenX = 1920
screenY = 1080
VSYNC = True
FPS = 30

HW, HH = screenX / 2, screenY / 2
AREA = screenX * screenY


# Player Settings
playerSpeed = 5



# Images
pygame.display.set_caption("This is a test currently.")
icon = pygame.image.load('images\daniel.png')



# Colors
BLACK = (0,0,0)
LGREY = (200, 200, 200)