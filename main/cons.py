import pygame

DEBUG = True

# Display information
screenX = 1920
screenY = 1080
VSYNC = True
FPS = 60

animationFPS = 15

HW, HH = screenX / 2, screenY / 2
AREA = screenX * screenY


# Player Settings
playerSpeed = 10


# Images
pygame.display.set_caption("This is a test currently.")
icon = pygame.image.load('images\daniel.png')


# Colors
BLACK = (0, 0, 0)
DGREY = (60, 60, 60)
GREY = (125, 125, 125)
LGREY = (200, 200, 200)
WHITE = (255, 255, 255)
