__author__ = 'New'




class Context:

    def __init__(self):
        self.window = None
        self.trainer = None
        self.pokedex = None
        self.sequence = None
        self.options = None
        self.navigation_registry = None
        self.controller = None
        self.direction = None
        self.global_frame_count = None
        self.destination = None
        self.controller_start = 0

    def change_controller(self, cont):
        self.controller_start = self.global_frame_count
        self.controller = cont

