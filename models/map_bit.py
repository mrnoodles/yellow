__author__ = 'andres'

import config
import graphics
import csv

DEFAULT_COLORS = {
    "WALKABLE": graphics.COLORS["WHITE"],
    "UNWALKABLE": graphics.COLORS["BLACK"],
    "WARP": graphics.COLORS["PINK"]
}


class LogicMap:

    def __init__(self, file=None):
        self.array = []


class GraphicMap:

    def __init__(self, file=None):
        self.array = []

