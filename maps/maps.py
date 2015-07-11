__author__ = 'andres'

import drawables
import walkables

class Map:

    def __init__(self, walkable, drawable, dimensions, debug_name="the middle of nowhere"):
        self.walkable = walkable
        self.drawable = drawable
        self.dimensions = dimensions
        self.debug_name = debug_name

maps = {
    0: Map(walkables.my_house_1, drawables.my_house_1, (8, 8), "1f"),
    1: Map(walkables.my_house_2, drawables.my_house_2, (0, 0), "2f"),
    2: Map(walkables.rivals_house_1, walkables.rivals_house_1, (0, 0), "1f"),
    3: Map(walkables.rivals_house_2, drawables.rivals_house_2, (0, 0), "2f"),
    4: Map(walkables.professor_oaks_lab, drawables.professor_oaks_lab, (0, 0), "Pokemon Lab")
}