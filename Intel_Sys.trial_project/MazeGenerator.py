import random

class MazeGenerator:
    def __init__(self, size) -> None:
        self.size = size
        self.rows = size[0]
        self.cols = size[1]
        self.generate()

    def isConnected(self, cell, links):
        if self.vis[cell[0]][cell[1]]:
            return
        
        self.vis[cell[0]][cell[1]] = True

        for i in links[cell[0]][cell[1]]:
            self.isConnected(i,links)

    def checkingConnectedCellsVisited(self, cells, links):
        x1,y1,x2,y2 = cells
        self.vis = []
        
        for i in range(self.rows):
            self.vis.append([])
            for j in range(self.cols):
                self.vis[i].append(False)

        self.isConnected((x1,y1), links)
        if self.vis[x2][y2]:
            return True
        
        return False



    def generate(self):
        toProcess = []
        openedEntranceToCells = []
        cellsLinkedTogether = []

        for i in range(self.rows):
            cellsLinkedTogether.append([])
            for j in range(self.cols):
                cellsLinkedTogether[i].append([])
                toProcess.append((i,j))

        while len(toProcess) > 0:
            x,y = random.choice(toProcess)
            
            w = []
            if x-1 >= 0:
                if not (x-1, y, x, y) in openedEntranceToCells:
                    w.append((x-1, y, x, y))
            if x+1<self.size[0]:
                if not (x,y,x+1,y) in openedEntranceToCells:
                    w.append((x, y, x+1, y))
            if y-1>=0:
                if not (x,y-1,x,y) in openedEntranceToCells:
                    w.append((x, y-1, x, y))
            if y+1<self.size[1]:
                if not (x,y,x,y+1) in openedEntranceToCells:
                    w.append((x, y, x, y+1))
            

            random.shuffle(w)

            n_linked = 0
            for p in w:
                if not self.checkingConnectedCellsVisited(p, cellsLinkedTogether):
                    n_linked +=1
                    if n_linked == 1:
                        x1,y1,x2,y2 = p
                        openedEntranceToCells.append(p)
                        cellsLinkedTogether[x1][y1].append((x2,y2))
                        cellsLinkedTogether[x2][y2].append((x1,y1))
                    

            if n_linked <= 1:
                toProcess.remove((x,y))

        self.openedEntranceToCells = openedEntranceToCells
