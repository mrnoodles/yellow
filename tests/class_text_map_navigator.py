__author__ = 'andres'

import pygame
from maps import locations
from maps import maps

#pygame.mixer.pre_init(44100,-16,2, 1024 * 3)
pygame.init()
from sound import sound_bank
import mixer


window = pygame.display.set_mode((100, 100))


def navigate():

    current_location = locations.MY_HOUSE
    current_map = current_location.map_data[1]
    song = current_location.song

    mixer.play_bgm(song)

    while True:
        print current_location.name, current_map.debug_name, ":\n"

        for exit in range(len(current_location.warps)):
            warp = current_location.warps[exit]
            if current_map.debug_name != maps.maps[warp.map].debug_name:
                print exit, ". ", warp.location, maps.maps[warp.map].debug_name

        option = input("Where would you like to go3? :")

        warp = current_location.warps[option]

        current_location = locations.locations[warp.location]
        current_map = current_location.map_data[warp.map]


        if song != current_location.song:
            song = current_location.song
            mixer.play_bgm(song)

if __name__ == "__main__":
    navigate()