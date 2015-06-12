__author__ = 'andres'

import pygame
import sys
import config

def controller(state):

    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



def model(state):
    pass

def view(state):
    pass

def main(state):

    while True:

        controller(state)
        model(state)
        view(state)

        config.CLOCK.tick(config.FPS)

