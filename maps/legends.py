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
    12: "pink.jpg"
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
