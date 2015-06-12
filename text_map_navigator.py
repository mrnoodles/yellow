__author__ = 'andres'

import pygame
import maps.location_info

#pygame.mixer.pre_init(44100,-16,2, 1024 * 3)
pygame.init()
from sound import sound_bank
import mixer


window = pygame.display.set_mode((100, 100))


def navigate():

    current_city = maps.location_info.PALLET_TOWN
    song = current_city["SONG"]

    mixer.play_bgm(song)

    while True:
        print current_city["NAME"], ":\n"

        for exit in range(len(current_city["EXITS"])):
            print exit, ".", current_city["EXITS"][exit]

        option = input("Where would you like to go? :")

        current_city = maps.location_info.locations[current_city["EXITS"][option]]

        if song != current_city["SONG"]:
            song = current_city["SONG"]
            mixer.play_bgm(song)

if __name__ == "__main__":
    navigate()