class Tile:
    # -1, -1 means there were no values stored
    # -2 means distance was not set
    def __init__(self, x=-1, y=-1, distance=-2):
        self.x = x
        self.y = y
        self.distance = distance