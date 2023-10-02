import random


# Maze Generator
# This class helps generate a maze
# Meaning that this class handles, generation of maze using DFS.
# Where we check if cells and neighboring cells are connected, through a tilemap.

class MazeGenerator:
    def __init__(self, size) -> None:
        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.generate() # generating a new maze, when we create an object instance of this class

    # Checking if the cells are connected to other neighboring cells
    # looking if we visited that cell
    def isConnected(self, cell, connections):
        if self.vis[cell[0]][cell[1]]:
            return
        
        self.vis[cell[0]][cell[1]] = True

        for i in connections[cell[0]][cell[1]]:
            self.isConnected(i,connections)

    # Needed a way to check if a cell is connected or a neighboring cell is connected, and this is how we check for that
    # Helper function
    # If there is some kind of way in between cells, shows that there are connections for those tiles
    def checkingConnectedCellsVisited(self, cells, connections):
        x1,y1,x2,y2 = cells
        self.vis = []
        
        for i in range(self.rows):
            self.vis.append([])
            for j in range(self.cols):
                self.vis[i].append(False)

        self.isConnected((x1,y1), connections)
        if self.vis[x2][y2]:
            return True
        
        return False


    # Generating the maze
    # Properties
    # toProcess - are tiles that are need to be checked if visited still
    # openedEntrancesToCells - are to check if there are any cells opened
    # cellsLinkedTogether - checks for the tiles that are connected together, corners, neighbors, etc
    # Using queue data structure to do DFS (Depth First Search)
    def generate(self):
        toProcess = []
        openedEntranceToCells = []
        cellsLinkedTogether = []

        # init the maze
        for i in range(self.rows):
            cellsLinkedTogether.append([])
            for j in range(self.cols):
                cellsLinkedTogether[i].append([])
                toProcess.append((i,j))

        # Then we filter and actually visually change the tile grid into a maze
        while len(toProcess) > 0:
            x,y = random.choice(toProcess)
            
            weights = [] # Weights list are re-interpreted as connections to the maze that are valid from the current cell. Meaning if those cells when generated can be connected together

            # In python, simply think of if not as if (!), just for reference
            if x-1 >= 0:
                if not (x-1, y, x, y) in openedEntranceToCells:
                    weights.append((x-1, y, x, y))
            if x+1 < self.size[0]: # Bounds checking, so we can be assured that the current cell cannot go out of scope of the maze
                if not (x,y,x+1,y) in openedEntranceToCells:
                    weights.append((x, y, x+1, y))
            if y-1 >= 0:
                if not (x,y-1,x,y) in openedEntranceToCells:
                    weights.append((x, y-1, x, y))
            if y+1 < self.size[1]: # Bounds checking, so we can be assured that the current cell cannot go out of scope of the maze
                if not (x,y,x,y+1) in openedEntranceToCells:
                    weights.append((x, y, x, y+1))
            
            # Using random.shuffle is how we randomize the maze's transformation visually
            random.shuffle(weights)

            # Keeping track of the neighboring tiles connected to the current tile.
            sizeConnected = 0
            for p in weights:
                if not self.checkingConnectedCellsVisited(p, cellsLinkedTogether):
                    sizeConnected += 1
                    if sizeConnected == 1:
                        x1,y1,x2,y2 = p
                        openedEntranceToCells.append(p)
                        cellsLinkedTogether[x1][y1].append((x2,y2))
                        cellsLinkedTogether[x2][y2].append((x1,y1))
                    
            
            if sizeConnected <= 1:
                toProcess.remove((x,y))

        self.openedEntranceToCells = openedEntranceToCells
