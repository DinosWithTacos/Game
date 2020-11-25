import pygame, sys
"""
Uhh.
"""

# Initialize pygame
pygame.init()

# Set initial screen size
screenX = 1920
screenY = 1080
HW, HH = screenX / 2, screenY / 2
AREA = screenX * screenY

DEBUG = False


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

DEBUG = False


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

class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename)

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows

        hw, hh = self.cellCenter = (w/2, h/2)

        self.cells = list([(index % cols * w, index // cols * h)
                           for index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h)
        ])

    def draw(self, surface, cellIndex, x, y, handle=0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])


# s = spritesheet("images\Weathen Spritesheet.png", 5, 5)

CENTER_HANDLE = 4

INDEX = 0

# Game loop
RUNNING = True

while RUNNING:
    screen.fill((200, 200, 200))  # Back ground color.

    # s.draw(screen, INDEX % s.totalCellCount, HW, HH, CENTER_HANDLE)
    INDEX += 1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If quit is pressed in the upper left
            print("So long gay Bowser")
            pygame.quit()
            sys.exit()
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
                DEBUG = not DEBUG

    playerX_pos += playerX_pos_delta
    playerY_pos += playerY_pos_delta

    debug_txt = font.render("", True, (0, 0, 0))

    if DEBUG:
        debug_txt = font.render(str(playerX_pos), True, (0, 0, 255))

    player(playerX_pos, playerY_pos)  # Places our player
    weathen(20, 20)

    screen.blit(debug_txt, (900, 0))
    pygame.display.update()
