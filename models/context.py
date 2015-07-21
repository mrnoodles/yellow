__author__ = 'New'




class Context:

    def __init__(self):
        self.window = None
        self.trainer = None
        self.pokedex = None
        self.sequence = None
        self.options = None
        self.gps = None
        self.controller = None
        self.global_frame_count = 0
        self.controller_start = 0

    def change_controller(self, cont):
        self.controller_start = self.global_frame_count
        self.controller = cont
        print '"Changed controller" to: ' + cont

