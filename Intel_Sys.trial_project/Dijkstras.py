from MazeGenerator import MazeGenerator
from Tile import Tile

class Dijkstras():
    def __init__(self, maze):
        self.maze = maze
        self.row = maze.size[0]
        self.col = maze.size[1]

    def solve(self, start: Tile, end: Tile):
        if end == Tile(-1,-1):
            end = Tile(self.maze.size[0]-1, self.maze.size[1]-1)
        
        queue = [start]

        # For some reason python does not allow to create 2D lists in the 2D for-loop, so creating the one-liner
        dist = [[-1 for temp in range(self.maze.size[1])]for temp in range(self.maze.size[0])]
        # dist = []

        # for i in range(self.maze.size[1]):
        #     rows = []
        #     for j in range(self.maze.size[0]):
        #         rows.append(-1)
        #     dist.append(rows)

        while len(queue) > 0:
            current = queue.pop(0)
            
            # We are computing based on thhe distance with the neighboring tiles
            if dist[current.x][current.y] == -1 or dist[current.x][current.y] > current.distance:
                dist[current.x][current.y] = current.distance

                if (current.x, current.y, current.x+1, current.y) in self.maze.openedEntranceToCells and current.x+1 < self.maze.size[0]:
                    queue.append(Tile(current.x+1,current.y, current.distance+1))
                
                if (current.x, current.y, current.x, current.y+1) in self.maze.openedEntranceToCells and current.y+1 < self.maze.size[1]:
                    queue.append(Tile(current.x,current.y+1, current.distance+1))
                
                if (current.x-1, current.y, current.x, current.y) in self.maze.openedEntranceToCells and current.x-1 >= 0:
                    queue.append(Tile(current.x-1,current.y, current.distance+1))

                if (current.x, current.y-1, current.x, current.y) in self.maze.openedEntranceToCells and current.y-1 >= 0:
                    queue.append(Tile(current.x,current.y-1, current.distance+1))

        # This array of tiles contain thhe shohrtest pathh the thhe ending coordinates, of how we animate those together
        self.shortestPathVisitedSolution = [end] # Because we want to start from the end
        if end == Tile(0,0) or start == Tile(0,0):
            self.shortestPathVisitedSolution.append((-1,0))

        if end == Tile(self.maze.size[0]-1, self.maze.size[1]-1) or start == Tile(self.maze.size[0]-1, self.maze.size[1]-1):
            self.solution.append((self.maze.size[0]-1, self.maze.size[1]))

        # Starting from the ending distance
        distance = dist[end.x][end.y]
        
        # print(f"ENDING DIST: {end.x} and {end.y} is {dist[end.x][end.y]}")
        # exit(0)
        # distance = end.distance
        current = end
        while distance > 0:
            newTile = Tile(current.x, current.y, current.distance)
            if newTile.x+1 < self.maze.size[0] and dist[newTile.x+1][newTile.y] == distance-1 and (newTile.x, newTile.y, newTile.x+1, newTile.y) in self.maze.openedEntranceToCells:
                self.shortestPathVisitedSolution.append((newTile.x+1,newTile.y))
                current = Tile(newTile.x+1,newTile.y)
                print(f"Distance: {distance}")
                distance -= 1
            elif newTile.x-1 >= 0 and dist[newTile.x-1][newTile.y] == distance-1 and (newTile.x-1,newTile.y,newTile.x,newTile.y) in self.maze.openedEntranceToCells: 
                self.shortestPathVisitedSolution.append((newTile.x-1,newTile.y))
                current = Tile(newTile.x-1,newTile.y)
                print(f"Distance: {distance}")
                distance -= 1
            elif newTile.y+1 < self.maze.size[1] and dist[newTile.x][newTile.y+1] == distance-1 and (newTile.x,newTile.y,newTile.x,newTile.y+1) in self.maze.openedEntranceToCells:
                self.shortestPathVisitedSolution.append((newTile.x,newTile.y+1))
                current = Tile(newTile.x,newTile.y+1)
                distance -= 1
            elif newTile.y-1 >= 0 and dist[newTile.x][newTile.y-1] == distance-1 and (newTile.x,newTile.y-1,newTile.x,newTile.y) in self.maze.openedEntranceToCells:
                self.shortestPathVisitedSolution.append((newTile.x,newTile.y-1))
                current = Tile(newTile.x,newTile.y-1)
                print(f"Distance: {distance}")
                distance -= 1

    # Backtracking from ending point to starting point, since the mouse being dragged is thhe ending point.
    # This allows thhe maze solver to have changes when dragging the mouse
    def get_solution(self):
        return self.shortestPathVisitedSolution