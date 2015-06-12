
__author__ = 'user'

import sys
import pygame

import config
import context

def main():
    setup()

    # script1.main(state)

def setup():
    pygame.init()
    state = context.Context()

    window = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    state.window = window

def game_loop():
    sys_clock = pygame.time.Clock()
    while True:
        handle_events()
        sys_clock.tick(config.FPS)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
