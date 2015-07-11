__author__ = 'New'

import pygame

import walkables
import drawables

walkable_legend = {
    0: "WALL",
    1: "WALKABLE",
    2: "ITEM PC",
    20: "NPC",
    40: "WARP",
    60: "ITEM"
}

drawable_legend = {
    0: "black.png",
    1: "house_tile.png",
    2: "vertical_bed.png",
    3: "computer.png",
    4: "horizontal_table.png",
    5: "house_wall.png",
    6: "house_window.png",
    7: "tv.png",
    8: "ness.png",
    9: "horizontal_plant.png",
    10: "house_downstairs.png"
}

images = []

def init():
    for i in range(1, 10):
        images.append(pygame.image.load(drawable_legend[i]))
