__author__ = 'user'

import pygame
import config
pygame.init()

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "PINK": (255, 127, 191)
}

soft_screen = pygame.Surface((160, 144), depth=8)

def update_window(window):
    pygame.transform.scale(soft_screen, config.WINDOW_DIMENSIONS, window)