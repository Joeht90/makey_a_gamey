class SceneConn:
    def __init__(self):
        self.connections = {}

    def add_connection(self, current_scene, north=None, south=None, east=None, west=None):
        self.connections[current_scene] = {"north": north, "south": south,
                                           "east": east, "west": west}

    def move_room(self, current_scene, direction):
        return self.connections[current_scene][direction]

  
