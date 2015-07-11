__author__ = 'andres'

def navigate():

    while True:
        option = input("Where would you like to go? :")

        warp = current_location.warps[option]

        current_location = locations.locations[warp.location]
        current_map = current_location.map_data[warp.map]


        if song != current_location.song:
            song = current_location.song
            mixer.play_bgm(song)


import sys
import pygame
pygame.init()
import config
import graphics
from models import navigation_registry
from models import context

from maps import locations
from maps import maps
import mixer

def main():
    state = setup()
    game_loop(state)
    # script1.main(state)

def setup():
    pygame.init()
    state = context.Context()

    where = locations.MY_HOUSE
    state.navigation_registry = navigation_registry.Navigator(where, where.map_data[1], (3, 5))
    state.window = pygame.display.set_mode(config.WINDOW_DIMENSIONS)


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
    area = state.navigation_registry.map
    pos = state.navigation_registry.position

    graphics.draw_logic_map(area.walkable, pos)
    graphics.draw_flavor_map(area.drawable, pos)
    graphics.update_window(state.window)

if __name__ == "__main__":
    main()
