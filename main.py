__author__ = 'user'

import sys
import pygame

import config
import graphics
from models import context

def main():
    state = setup()
    game_loop(state)
    # script1.main(state)

def setup():
    pygame.init()
    state = context.Context()

    state.window = pygame.display.set_mode(config.WINDOW_DIMENSIONS, 0, 8)
    return state

def game_loop(state):
    sys_clock = pygame.time.Clock()

    while True:
        handle_events(state)
        game_logic(state)
        draw(state)

        pygame.display.update()
        sys_clock.tick(config.FPS)

def handle_events(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def game_logic(state):
    pass

def draw(state):
    graphics.update_window(state.window)

if __name__ == "__main__":
    main()
