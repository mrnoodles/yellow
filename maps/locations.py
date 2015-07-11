__author__ = 'andres'

import maps

class Warp:

    def __init__(self, dest_location, dest_map, dest_coord):
        self.location = dest_location
        self.map = dest_map
        self.pos = dest_coord


class Location:

    def __init__(self, song, name, type, warps=None, maps=1, map_data=None, landing=None):
        self.song = song
        self.name = name
        self.type = type
        self.warps = warps

        if (type == "OVERWORLD"):
            self.landing = landing
            self.map_data = map_data

        if (type == "BUILDING" or type == "DUNGEON"):
            self.maps = maps
            self.map_data = map_data



MY_HOUSE = Location(1, "MY_HOUSE", "BUILDING",
    warps=[
        Warp("My House", 0, (0, 7)),
        Warp("My House", 1, (0, 7))
    ],
    maps=2,
    map_data= [maps.maps[0], maps.maps[1]]
)

PALLET_TOWN = {
    "SONG": 1,
    "NAME": "PALLET TOWN",
    "EXITS": ["My House", "Bill's House", "Professor's Lab", "Route 1", "Route 21"],
    "TYPE": "OVERWORLD"
}

VIRIDIAN_CITY = {
    "SONG": 8,
    "NAME": "VIRIDIAN CITY",
    "EXITS": ["Route 1", "Route 2", "Route 22", "Viridian Gym"],
    "TYPE": "OVERWORLD"
}

PEWTER_CITY = {
    "SONG": 8,
    "NAME": "PEWTER CITY",
    "EXITS": ["Route 2", "Route 3", "Pokemon Museum", "Pewter Gym"],
    "TYPE": "OVERWORLD"
}

CERULEAN_CITY = {
    "SONG": 18,
    "NAME": "CERULEAN_CITY",
    "EXITS": ["Route 4", "Route 5", "Route 9", "Route 24", "Unknown Dungeon"],
    "TYPE": "OVERWORLD"
}

VERMILION_CITY = {
    "SONG": 22,
    "NAME": "VERMILION_CITY",
    "EXITS": ["Route 6", "Route 11"],
    "TYPE": "OVERWORLD"
}

LAVENDER_TOWN = {
    "SONG": 30,
    "NAME": "LAVENDER_TOWN",
    "EXITS": ["Route 8", "Route 10", "Route 12"],
    "TYPE": "OVERWORLD"
}

SAFFRON_CITY = {
    "SONG": 18,
    "NAME": "SAFFRON_CITY",
    "EXITS": ["North Saffron Gate", "South Saffron Gate", "East Saffron Gate", "Sylph Co"],
    "TYPE": "OVERWORLD"
}

CELADON_CITY = {
    "SONG": 18,
    "NAME": "CELADON_CITY",
    "EXITS": ["Route 7", "Route 16"],
    "TYPE": "OVERWORLD"
}

FUCHSIA_CITY = {
    "SONG": 18,
    "NAME": "FUCHSIA_CITY",
    "EXITS": ["Route 18", "Route 19"],
    "TYPE": "OVERWORLD"
}

CINNABAR_ISLAND = {
    "SONG": 38,
    "NAME": "CINNABAR_ISLAND",
    "EXITS": ["Route 20", "Route 21"],
    "TYPE": "OVERWORLD"
}

INDIGO_PLATEAU = {
    "SONG": 41,
    "NAME": "INDIGO_PLATEAU",
    "EXITS": ["Victory Road"],
    "TYPE": "OVERWORLD"
}


ROUTE_1 = {
    "SONG": 5,
    "NAME": "ROUTE 1",
    "EXITS": ["Pallet Town", "Viridian City"],
    "TYPE": "OVERWORLD"
}

ROUTE_2 = {
    "SONG": 5,
    "NAME": "ROUTE 2",
    "EXITS": ["Viridian City", "Viridian Forest", "Pewter City"],
    "TYPE": "OVERWORLD"
}

ROUTE_3 = {
    "SONG": 17,
    "NAME": "ROUTE 3",
    "EXITS": ["Pewter City", "Mt Moon"],
    "TYPE": "OVERWORLD"
}

ROUTE_4 = {
    "SONG": 17,
    "NAME": "ROUTE 4",
    "EXITS": ["Mt Moon", "Cerulean City"],
    "TYPE": "OVERWORLD"
}

ROUTE_5 = {
    "SONG": 17,
    "NAME": "ROUTE 5",
    "EXITS": ["Cerulean City", "North Saffron Gate", "North Underground Path"],
    "TYPE": "OVERWORLD"
}

ROUTE_6 = {
    "SONG": 17,
    "NAME": "ROUTE 6",
    "EXITS": ["South Underground Path", "Vermilion City", "South Saffron Gate"],
    "TYPE": "OVERWORLD"
}

ROUTE_7 = {
    "SONG": 17,
    "NAME": "ROUTE 7",
    "EXITS": ["West Underground Path", "West Saffron Gate", "Celadon City"],
    "TYPE": "OVERWORLD"
}

ROUTE_8 = {
    "SONG": 17,
    "NAME": "ROUTE 8",
    "EXITS": ["East Underground Path", "East Saffron Gate", "Lavender Town"],
    "TYPE": "OVERWORLD"
}

ROUTE_9 = {
    "SONG": 17,
    "NAME": "ROUTE 9",
    "EXITS": ["Cerulean City", "Route 10"],
    "TYPE": "OVERWORLD"
}

ROUTE_10 = {
    "SONG": 17,
    "NAME": "ROUTE 10",
    "EXITS": ["Route 9", "Rock Tunnel", "Power Plant", "Lavender Town"],
    "TYPE": "OVERWORLD"
}

ROUTE_11 = {
    "SONG": 24,
    "NAME": "ROUTE 11",
    "EXITS": ["Vermilion City", "Route 11 12 Gate"],
    "TYPE": "OVERWORLD"
}

ROUTE_11_12_GATE = {
    "SONG": 22,
    "NAME": "Route 11 12 Gate",
    "EXITS": ["Route 11", "Route 12"],
    "TYPE": "BUILDING"
}

ROUTE_12 = {
    "SONG": 24,
    "NAME": "ROUTE 12",
    "EXITS": ["Route 11 12 Gate", "Route 13", "Lavender Town"],
    "TYPE": "OVERWORLD"
}

ROUTE_13 = {
    "SONG": 24,
    "NAME": "ROUTE 13",
    "EXITS": ["Route 12", "Route 14"],
    "TYPE": "OVERWORLD"
}

ROUTE_14 = {
    "SONG": 24,
    "NAME": "ROUTE 14",
    "EXITS": ["Route 13", "Route 15"],
    "TYPE": "OVERWORLD"
}

ROUTE_15 = {
    "SONG": 24,
    "NAME": "ROUTE 15",
    "EXITS": ["Route 14", "East Fuchsia Gate"],
    "TYPE": "OVERWORLD"
}

ROUTE_16 = {
    "SONG": 17,
    "NAME": "ROUTE 16",
    "EXITS": ["Celadon City", "Route 17", "North Cycling Gate"],
    "TYPE": "OVERWORLD"
}

ROUTE_17 = {
    "SONG": 17,
    "NAME": "ROUTE 17",
    "EXITS": ["Route 16", "Route 18"],
    "TYPE": "OVERWORLD"
}

ROUTE_18 = {
    "SONG": 17,
    "NAME": "ROUTE 18",
    "EXITS": ["Route 17", "South Cycling Gate", "Fuchsia City"],
    "TYPE": "OVERWORLD"
}

ROUTE_19 = {
    "SONG": 17,
    "NAME": "SEA ROUTE 19",
    "EXITS": ["Fuchsia City", "Route 20"],
    "TYPE": "OVERWORLD"
}

ROUTE_20 = {
    "SONG": 17,
    "NAME": "SEA ROUTE 20",
    "EXITS": ["Route 19", "East Seafoam Island", "West Seafoam Island", "Cinnabar Island"],
    "TYPE": "OVERWORLD"
}

ROUTE_21 = {
    "SONG": 17,
    "NAME": "SEA ROUTE 21",
    "EXITS": ["Pallet Town", "Cinnabar Island"],
    "TYPE": "OVERWORLD"
}

ROUTE_22 = {
    "SONG": 17,
    "NAME": "ROUTE 22",
    "EXITS": ["Viridian City", "Elite Four Gate"],
    "TYPE": "OVERWORLD"
}

ROUTE_23 = {
    "SONG": 41,
    "NAME": "ROUTE 23",
    "EXITS": ["Elite Four Gate", "Victory Road"],
    "TYPE": "OVERWORLD"
}

ROUTE_24 = {
    "SONG": 20,
    "NAME": "ROUTE 24",
    "EXITS": ["Cerulean City", "Route 25"],
    "TYPE": "OVERWORLD"
}

ROUTE_25 = {
    "SONG": 20,
    "NAME": "ROUTE 25",
    "EXITS": ["Route 24", "Sea Cottage"],
    "TYPE": "OVERWORLD"
}

SEA_COTTAGE = {
    "SONG": 18,
    "NAME": "SEA COTTAGE",
    "EXITS": ["Route 25"],
    "TYPE": "BUILDING"
}

VIRIDIAN_FOREST = {
    "SONG": 11,
    "NAME": "VIRIDIAN FOREST",
    "EXITS": ["Route 2"],
    "TYPE": "OVERWORLD"
}


locations = {
    "My House": MY_HOUSE,
    "Pallet Town": PALLET_TOWN,
    "Viridian City": VIRIDIAN_CITY,
    "Pewter City": PEWTER_CITY,
    "Cerulean City": CERULEAN_CITY,
    "Vermilion City": VERMILION_CITY,
    "Lavender Town": LAVENDER_TOWN,
    "Saffron City": SAFFRON_CITY,
    "Celadon City": CELADON_CITY,
    "Fuchsia City": FUCHSIA_CITY,
    "Cinnabar Island": CINNABAR_ISLAND,
    "Indigo Plateau": INDIGO_PLATEAU,
    "Route 1": ROUTE_1,
    "Route 2": ROUTE_2,
    "Route 3": ROUTE_3,
    "Route 4": ROUTE_4,
    "Route 5": ROUTE_5,
    "Route 6": ROUTE_6,
    "Route 7": ROUTE_7,
    "Route 8": ROUTE_8,
    "Route 9": ROUTE_9,
    "Route 10": ROUTE_10,
    "Route 11": ROUTE_11,
    "Route 12": ROUTE_12,
    "Route 13": ROUTE_13,
    "Route 14": ROUTE_14,
    "Route 15": ROUTE_15,
    "Route 16": ROUTE_16,
    "Route 17": ROUTE_17,
    "Route 18": ROUTE_18,
    "Route 19": ROUTE_19,
    "Route 20": ROUTE_20,
    "Route 21": ROUTE_21,
    "Route 22": ROUTE_22,
    "Route 23": ROUTE_23,
    "Route 24": ROUTE_24,
    "Route 25": ROUTE_25,
    "Sea Cottage": SEA_COTTAGE,
    "Viridian Forest": VIRIDIAN_FOREST,
    "North Digglet's Cave": None,
    "South Digglet's Cave": None,
    "Mt Moon": None,
    "Rock Tunnel": None,
    "Power Plant": None,
    "Safari Zone": None,
    "Seafoam Island": None,
    "Pokemon Mansion": None,
    "Pokemon Tower": None,
    "Route 11 12 Gate": ROUTE_11_12_GATE
}
