__author__ = 'New'

import pygame
import os
import walkables
import drawables

walkable_legend = {
    0: "WALL",
    1: "WALKABLE",
    2: "ITEM PC",
    20: "NPC",
    40: "WARP",
    60: "ITEM",
    80: "INFO"
}

walkable_draws = {
    "WALL": 0,
    "WALKABLE": 11,
    "ITEM PC": 12,
    "WARP": 12,
    "INFO": 12
}

drawable_legend = {
    0: "black.jpg",
    1: "house_tile.png",
    2: "vertical_bed.png",
    3: "computer.png",
    4: "horizontal_table.png",
    5: "house_wall.png",
    6: "house_window.png",
    7: "tv.png",
    8: "ness.png",
    9: "horizontal_plant.png",
    10: "house_downstairs.png",
    11: "white.jpg",
    12: "pink.jpg",
    13: "tall_grass.png",
    14: "world_barrier.png",
    15: "signpost.png",
    16: "white_tile.png",
    17: "two_story_doored_house.png",
    18: "professors_lab.png",
    19: "horizontal_fence.png",
    20: "full_short_grass.png",
    21: "down_left_short_grass.png",
    22: "trainer_spawn.png",
    23: "flowerless_patch.png",
    24: "up_left_flower_patch.png",
    25: "down_right_flower_patch.png",
    26: "up_left_water_border.png",
    27: "up_right_water_border.png",
    28: "up_water_border.png",
    29: "left_water_border.png",
    30: "right_water_border.png",
    31: "down_water_border.png",
    32: "down_left_water_border.png",
    33: "down_right_water_border.png",
    34: "up_water_border.png",
    35: "water_tile.png"
}

images = []

def init():
    for i in range(13):
        path = "../assets/img/map_bits/" + drawable_legend[i]

        if os.path.isfile(path):
            images.append(pygame.image.load(path))
            print "loaded: " + os.path.abspath(path)
        else:
            images.append(None)






































