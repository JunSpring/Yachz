import pygame, math, os, json
import data.text as text
from pygame.locals import *

BORDER_WIDTH = 70

mainClock = pygame.time.Clock()

pygame.init()
pygame.mixer.set_num_channels(32)
pygame.display.set_caption('🎲Yachz')
screen = pygame.display.set_mode((800 + 2 * BORDER_WIDTH, 550))

display = pygame.Surface((275, 400))
gui_display = pygame.Surface((275, 400))
gui_display.set_colorkey((0, 0, 0))

font = text.Font('data/fonts/large_font.png', (255, 255, 255))
