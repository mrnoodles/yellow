__author__ = 'andres'

from maps import locations
from maps import legends
import mixer

class Navigator:

    def __init__(self, location, map, position):
        self.location = location
        self.map = map
        self.song = self.location.song
        self.position = position
        self.direction = None
        self.destination = None
        self.facing = None

        mixer.play_bgm(self.song)


    def change_song(self, song):
        if song != self.song:
            mixer.play_bgm(song)
            self.song = song

    def warp_to(self, warp):
        self.location = locations.locations[warp.location]
        self.map = self.location.map_data[warp.map]
        self.change_song(self.location.song)

    def print_where_am_i(self):
        print self.location.name, self.map.debug_name, ":\n"

    def land_on_destination(self):
        landing_tile = legends.walkable_legend[self.map.walkable[self.destination[0]][self.destination[1]]]
        if landing_tile == "WALKABLE":
            self.position = self.destination
            print "Landed on: ", self.destination

