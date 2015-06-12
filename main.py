
__author__ = 'user'

import sys
import pygame
import constants
import keyboard
import physics
import mixer
import graphics
import pokedex
import context
import script1

def main():

    pygame.init()

    state = context.Context()

    window = pygame.display.set_mode(constants.WINDOW_DIMENSIONS)
    state.window = window

    script1.main(state)




if __name__ == "__main__":
    main()