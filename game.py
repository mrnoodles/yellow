__author__ = 'Naoto'


import pygame
pygame.init()
from models import context
from views import overworld
import config



def main():
    pygame.init()
    state = context.Context()

    window = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    state.window = window

    overworld.navigate()

if __name__ == "__main__":
    main()

