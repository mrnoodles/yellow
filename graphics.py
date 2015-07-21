__author__ = 'user'

import pygame
import config
from maps import legends
pygame.init()
legends.init()

COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "PINK": (255, 127, 191)
}

hero_layer = pygame.Surface((16, 16))
map_layer = pygame.Surface((160, 144))

soft_screen = pygame.Surface((160, 144))


def draw_logic_tile(tile_id, position):
    type_of_tile = legends.walkable_legend[tile_id%100]
    walkable_index_equivalent = legends.walkable_draws[type_of_tile]

    soft_screen.blit(legends.images[walkable_index_equivalent], position)

def draw_flavor_tile(tile_id, position):
    #type_of_tile = legends.drawable_legend[tile_id]

    if tile_id != -1:
        img = legends.images[tile_id]
        if not (img is None):
            soft_screen.blit(img, position)

def draw_logic_map(logic_map, player_position):
    height = len(logic_map)
    width = len(logic_map[0])

    for row in range(height):
        for column in range(width):
            draw_logic_tile(logic_map[row][column], (((-player_position[1] + column +3))*16, ((-player_position[0] + row +3))*16))

def draw_flavor_map(flavor_map, player_position):
    height = len(flavor_map)
    width = len(flavor_map[0])

    for row in range(height):
        for column in range(width):
            if not (flavor_map[row][column] is None):
                draw_flavor_tile(flavor_map[row][column], (((-player_position[1] + column +3))*16, ((-player_position[0] + row +3))*16))

def update_map_layer(map, origin_position):
    height = len(map.drawable)
    width = len(map.drawable[0])

    center_row = origin_position[0]/16
    center_column = origin_position[1]/16

    row_offset = origin_position[0]%16
    column_offset = origin_position[1]%16

    start = max(center_row -3, 0), max(center_column -3, 0)
    end = min(height - center_row + 3, height), min(width - center_column + 3, width)

    #print start, end
    for row in range(start[0], end[0]):
        for column in range(start[1], end[1]):
            tile_id = map.drawable[row][column]
            if tile_id != -1:
                img = legends.images[tile_id]
                pos = (column*16 + column_offset, row*16 + row_offset)
                map_layer.blit(img, pos)


def update_hero_layer(orientation, controller, frame=0, ij=0):
    if controller == "walking" or controller == "thud":
        if orientation == "UP":
            if frame%16:
                if (-1)**ij + 1:
                    hero_layer.blit(legends.player[1], (0, 0))
                else:
                    hero_layer.blit(legends.player[2], (0, 0))
            else:
                hero_layer.blit(legends.player[0], (0, 0))
        if orientation == "DOWN":
            if frame%16:
                if (-1)**ij + 1:
                    hero_layer.blit(legends.player[4], (0, 0))
                else:
                    hero_layer.blit(legends.player[5], (0, 0))
            else:
                hero_layer.blit(legends.player[3], (0, 0))
        if orientation == "LEFT":
            if frame%16:
                hero_layer.blit(legends.player[7], (0, 0))
            else:
                hero_layer.blit(legends.player[6], (0, 0))
        if orientation == "RIGHT":
            if frame%16:
                hero_layer.blit(legends.player[9], (0, 0))
            else:
                hero_layer.blit(legends.player[8], (0, 0))
    else:
        if orientation == "UP":
            hero_layer.blit(legends.player[0], (0, 0))
        if orientation == "DOWN":
            hero_layer.blit(legends.player[3], (0, 0))
        if orientation == "LEFT":
            hero_layer.blit(legends.player[6], (0, 0))
        if orientation == "RIGHT":
            hero_layer.blit(legends.player[8], (0, 0))



def update_window(window):
    pygame.transform.scale(soft_screen, config.WINDOW_DIMENSIONS, window)

def flush(window):
    soft_screen.fill(COLORS["BLACK"])

def flush_everything_else():
    soft_screen.fill(COLORS["BLACK"])
    map_layer.fill((COLORS["BLACK"]))
    hero_layer.fill(COLORS["WHITE"])