__author__ = 'andres'

import pygame
import sys
import config

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def game_logic():
    pass

def draw():
    pass

def navigate():
    sys_clock = pygame.time.Clock()
    while True:
        handle_events()
        game_logic()
        draw()
        pygame.display.update()
        sys_clock.tick(config.FPS)