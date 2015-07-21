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
from controllers import one_and_only as joypad
from maps import locations
from maps import legends
import mixer

def main():
    state = setup()
    game_loop(state)
    # script1.main(state)

def setup():
    pygame.init()
    state = context.Context()

    where = locations.MY_HOUSE
    state.navigation_registry = navigation_registry.Navigator(where, where.map_data[1], (3, 3))
    state.window = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    state.change_controller("standing")


    return state

def game_loop(state):
    sys_clock = pygame.time.Clock()
    state.global_frame_count = 0

    while True:
        handle_events(state)
        game_logic(state)
        draw(state)

        pygame.display.update()
        sys_clock.tick(config.FPS)
        state.global_frame_count += 1

def handle_events(state):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        state.direction = None
        if state.controller == "standing":
            state.direction = joypad.movement(pygame.key.get_pressed())

def game_logic(state):
    if state.controller == "standing":
        direction = state.direction
        pos = state.navigation_registry.position
        state.destination = pos[0] + direction[0], pos[1] + direction[1]

        map = state.navigation_registry.map

        if map.contains_position(state.destination):
            dest_type = map.walkable[state.destination[0]][state.destination[1]]
            value = legends.walkable_legend[dest_type%100]
            argument = dest_type/100

            if (value == "WALKABLE") or (value == "WARP"):
                state.change_controller("walking")
            else:
                state.change_controller("thud")
        else:
            state.change_controller("thud")


def draw(state):
    area = state.navigation_registry.map
    pos = state.navigation_registry.position

    graphics.draw_logic_map(area.walkable, pos)
    graphics.draw_flavor_map(area.drawable, pos)
    graphics.update_window(state.window)

if __name__ == "__main__":
    main()
