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
    pygame.key.set_repeat(15, 15)
    state = context.Context()

    where = locations.MY_HOUSE
    state.gps = navigation_registry.Navigator(where, where.map_data[1], (3, 3))
    state.window = pygame.display.set_mode(config.WINDOW_DIMENSIONS)
    state.change_controller("standing")
    state.gps.facing = "DOWN"


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

        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()


            if state.controller == "standing":
                #state.gps.direction = None

                temp_dir = joypad.movement(keys)

                if not (temp_dir is None):
                    if state.gps.facing == joypad.get_facing(keys):
                        state.gps.direction = temp_dir
                    state.gps.facing = joypad.get_facing(keys)


def game_logic(state):
    if state.controller == "standing" and  not (state.gps.direction is None):
        direction = state.gps.direction
        pos = state.gps.position
        state.gps.destination = pos[0] + direction[0], pos[1] + direction[1]

        map = state.gps.map

        if map.contains_position(state.gps.destination):
            dest_type = map.walkable[state.gps.destination[0]][state.gps.destination[1]]
            value = legends.walkable_legend[dest_type%100]
            print value
            argument = dest_type/100


            if (value == "WALKABLE") or (value == "WARP"):
                state.change_controller("walking")
            else:
                state.change_controller("thud")
        else:
            state.change_controller("thud")

    if state.controller == "walking":
        if state.global_frame_count - state.controller_start > 15:
            state.change_controller("standing")
            state.gps.land_on_destination()


def draw(state):
    area = state.gps.map
    pos = state.gps.position

    direction = state.gps.direction

    if direction is None:
        direction = (0, 0)

    mov = state.controller == "walking"
    frame = state.global_frame_count - state.controller_start
    frame = frame*(frame<16)
    #state.window.fill((0,0,0))
    graphics.flush_everything_else()
    #print frame

    origin_pos = (48 - pos[1]*16 - direction[1]*mov*frame, 48 - pos[0]*16 - direction[0]*mov*frame)
    print origin_pos
    print mov
    print frame

    graphics.update_map_layer(area, (0,0))
    graphics.update_hero_layer(state.gps.facing, mov, frame, pos[0] + pos[1])
    graphics.soft_screen.blit(graphics.map_layer, origin_pos)
    graphics.soft_screen.blit(graphics.hero_layer, (48, 48))




    graphics.update_window(state.window)

if __name__ == "__main__":
    main()
