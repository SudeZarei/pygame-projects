# keep all constants here to change them easily
# constants are just for checkers game

import pygame

WIDTH = int(800)
HEIGHT = int(800)
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH // COLS
HUD_WIDTH = 300

#rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255) # shows ways
BIEGE = (213, 159, 89)
BROWN = (158, 94, 22)
GRAY = (128, 128, 128) # for outline
LIGHT_PURPLE = (194, 133, 254) # menu
DARK_PURPLE = (68, 8, 57)

#img
CROWN = pygame.transform.scale(pygame.image.load('assets\\crown.png'), (44,25))
RESTART = pygame.transform.scale(pygame.image.load('assets\\restart.png'), (105,105))
HOME = pygame.transform.scale(pygame.image.load('assets\\home.png'), (105,105))
COMPUTER = pygame.transform.scale(pygame.image.load('assets\\AI.png'), (200,200))
PLAYER = pygame.transform.scale(pygame.image.load('assets\\player.png'), (200,200))
BLACK_PIC = pygame.transform.scale(pygame.image.load('assets\\black.png'), (100,100))
RED_PIC = pygame.transform.scale(pygame.image.load('assets\\red.png'), (100,100))


#font
FONT = pygame.font.Font('assets\\Montserrat.ttf', 30)
NAME_FONT = pygame.font.Font('assets\\Montserrat.ttf', 100)