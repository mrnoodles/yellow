__author__ = 'user'

import sys
import pygame
import keyboard
import physics
import mixer
import graphics
import pokedex

def main():

    controller()
    model()
    view()


def controller():

    for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pass

def model():
    pass

def view():
    pass

if __name__ == "__main__":
    pygame.init()
    main()