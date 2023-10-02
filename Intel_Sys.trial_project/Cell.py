from Tile import Tile

# Using this class to possibly handle how we may generate cells in the maze
# This way it would be easier to check for connections between the neighboring cells, and any open entrances in the maze
# Created this class, if there is enough time to implement
class Cell():

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
