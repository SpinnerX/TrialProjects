import pygame
from pygame.locals import *
from MazeGenerator import MazeGenerator
import sys
from Dijkstras import Dijkstras
from Button import Button
from Tile import Tile
from Animation import Animations
import sys

def renderLine(window, color, offset, thickness):
    pygame.draw.line(window, color, *offset, width=thickness)

def main():
    pygame.init()
    size = width, height = 1202, 920
    FPS = 60 # Frame rate per second
    
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Intelligent Systems Trial Project")

    surface = pygame.Surface(size)
    clock = pygame.time.Clock()

    mazeSize = (25, 20) # rows and cols for maze dimensions
    tileSize = 40 # Amt of tiles to generate in the window, for the maze (since we generate a tile and using DFS to generate and visualize actual maze before using Dijkstras to solve the maze)

    maze = MazeGenerator(mazeSize)
    dijkstra = Dijkstras(maze)

    shortestPath = [] # Shortest path, so we can draw the path and represent it as a line
    boardX, boardY = (20, 20)

    start = None
    end = None
    mouseCurrentTile = Tile(0, 0, 0) # Setting x=0, y=0, dist=0 by default
    currentTileAnimate = None # This contains the current instance of the tile the algorithm is on and is what renders the actual Dijkstra's algorithhm
    isRunning = True

    # wallsColor = pygame.Color('white')
    wallsColor = pygame.Color((255,229,180)) # Marigold RGB
    cyanColor = pygame.Color(224, 255, 255) # Light cyan
    # coloredLine = pygame.Color('yellow') #
    coloredLine = pygame.Color((144, 238, 144)) # light green
    thickness = 10
    
    # Loading assets
    background_wallpaper = pygame.image.load('assets/background2.jpg')
    background_pos = (0, 0)
    
    # Creating button to generate new maze
    generateNewButton = Button(cyanColor, x=1050, y=150, width=130, height=50, text="New Maze")
    clearButton = Button(cyanColor,x=1050, y=250, width=130, height=50, text="Clear")
    quitButton = Button(cyanColor, x=1050, y=350, width=130, height=50, text="Quit App")

    # animation = Animations(mazeSize, coloredLine)

    while isRunning:
        window.blit(surface, (0, 0))
        # sideWindow.blit(surface, (0, 0))
        # sideWindow.fill((255, 255, 255))

        surface.blit(background_wallpaper, background_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Handling key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            #  Handling mouse clicker events
            # These are thhe different types of mouse clicks
            # 1 - left click
            # 2 - middle click
            # 3 - right click
            # 4 - scroll up
            # 5 - scroll down
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left-clicked
                    mouseX,mouseY = event.pos
                    x = (mouseX-boardX)//tileSize
                    y = (mouseY-boardY)//tileSize
                    if x >= 0 and y >= 0 and x < mazeSize[0] and y < mazeSize[1]:
                        start = Tile(x, y, -1)
                    
                if event.button == 2: # Middle-click 
                    start = None
                    end = None
                    maze.generate()
                    

                if event.button == 3: # Right-click
                    mouseX,mouseY = event.pos
                    x = (mouseX-boardX) // tileSize
                    y = (mouseY-boardY) // tileSize
                    if x >= 0 and y >= 0 and x < mazeSize[0] and y < mazeSize[1]:
                        end = Tile(x, y, -1)
            
            # Checking if the buttons have been clicked
            # Generate new maze
            if clearButton.processEvents(event, pygame.mouse.get_pos()) == True:
                start = None
                end = None

            # Clear current maze, and does not randomize creating a new maze
            if generateNewButton.processEvents(event, pygame.mouse.get_pos()) == True:
                start = None
                end = None
                maze.generate()
            
            # Quit button just so user can simply quit the application
            if quitButton.processEvents(event, pygame.mouse.get_pos()) == True:
                pygame.quit()
                sys.exit()

        # Handling the position of the mouse specifics in the maze whhen detected through event handler
        # top-right corner = (x, y) = ()
        mouseX,mouseY = pygame.mouse.get_pos()
        # print(f"MOUSE (X, Y) - ({mouseX}, {mouseY})")

        x = (mouseX-boardX) // tileSize
        y = (mouseY-boardY) // tileSize

        print(f"CURRENT (X, Y) = ({x}, {y})")

        # This is how we animate the tile onto the maze
        # Bounds checking
        if x >= 0 and y >= 0 and x < mazeSize[0] and y < mazeSize[1]:
            mouseCurrentTile = Tile(x,y)
            if currentTileAnimate != mouseCurrentTile:
                currentTileAnimate = mouseCurrentTile
        else:
            currentTileAnimate = None
        # animation.start(currentTileAnimate)
        # animation.update(mouseCurrentTile, x, y)

        # We are checking if the starting and ending positions variables are clear and deciding if we need to render anythihng or not
        # Backtracking
        if end == None and start == None:
            shortestPath.clear()
        elif end == None and start != None:
            dijkstra.solve(start, mouseCurrentTile)
            shortestPath = dijkstra.resultedShortestPath()
        elif end != None and start == None:
            dijkstra.solve(end, mouseCurrentTile)
            shortestPath = dijkstra.resultedShortestPath()
        else:
            dijkstra.solve(start, end)
            shortestPath = dijkstra.resultedShortestPath()

        if currentTileAnimate != None:
            cyanColor.a = 250 # Setting thhe transparency
            # Tile selector
            pygame.draw.rect(window, cyanColor, pygame.Rect(boardX+currentTileAnimate.x*tileSize, boardY+currentTileAnimate.y*tileSize,tileSize, tileSize), width=0) # Used for currentTileAnimate the box

        # animation.render(window, tileSize, boardX, boardY, cyanColor)



        # We iterate through thhe entire maze
        # Getting the offset to create the maze, top, right, bottom, left, borders for thhe maze and the cells (walls)
        for x in range(mazeSize[0]):
            for y in range(mazeSize[1]):
                # Top-right corner X, Y = 1020, 23
                # doesContainStartingCoords = (x+y == 0) # This allows us to check if this is a starting point, if it is to not draw a wall
                doesContainStartingCoords = (x == 0 and y == 0) # This allows us to check if this is a starting point, if it is to not draw a wall
                # doesContainStartingCoords = (x == mazeSize[0]-1 and y == 0) # This allows us to check if this is a starting point, if it is to not draw a wall
                # doesContainStartingCoords = (x == 24 and y == 0) # This allows us to check if this is a starting point, if it is to not draw a wall

                doesContainEndingCoords = (x == mazeSize[0] - 1 and y == mazeSize[1] - 1) # This is basically what will be rendering the exiting point of thhe maze


                # Calculating thhe maze's cells, borders offsets
                # Just noting that these are offsets for chhecking the x and y coordinates of theh maze as we iterate through the maze
                # By this allows us to chheck for walls either opened, or closed
                # right_border_offset = (Tile((boardX+x*tileSize, boardY+y*tileSize)), Tile((boardX+x*tileSize, boardY+(y+1) * tileSize)))
                right_border_offset = ((boardX+x*tileSize, boardY+y*tileSize),(boardX+x*tileSize, boardY+(y+1) * tileSize)) # Vertical lines offset
                right_border_offset1 = ((boardX+x*tileSize - tileSize // 2, boardY + y * tileSize + tileSize // 2),(boardX + x * tileSize + tileSize//2,boardY+y*tileSize + tileSize//2))  # Handle corners from vertical lines
                
                left_border_offset = ((boardX+(x+1)*tileSize, boardY+y*tileSize),(boardX+(x+1)*tileSize, boardY+(y+1)*tileSize)) # Horizontal lines
                left_border_offset1 = ((boardX+x*tileSize + tileSize//2, boardY+y*tileSize + tileSize//2),(boardX+x*tileSize + 3*(tileSize//2),boardY+y*tileSize + tileSize // 2)) # Represent diagonal lines

                tileMazeCell_offset = ((boardX + x * tileSize, boardY + y * tileSize), (boardX + ( x + 1 ) * tileSize, boardY + y * tileSize)) # horizontal lines towards the top of the maze
                tileMazeCell_offset1 = ((boardX + x * tileSize + tileSize//2, boardY+y*tileSize - tileSize//2),(boardX+x*tileSize + tileSize // 2, boardY + y * tileSize + tileSize // 2)) # diagonal for top right and left of tiles

                bottom_border_offset = ((boardX + x * tileSize, boardY+(y+1) * tileSize),(boardX+(x+1)*tileSize, boardY+(y+1)*tileSize)) # Starting and ending coordinates for thhe bottomside of tiles
                bottom_border_offset1 = ((boardX+x*tileSize + tileSize // 2, boardY+y*tileSize + tileSize//2),(boardX+x*tileSize + tileSize//2, boardY+y*tileSize + 3*(tileSize//2))) # Handles thhe bottom left and right corners of the tile.
                
                # Manually checking if the top, right, left, bottom walls are connected or if the next term is a wall

                # neighboringCells = [1, -1]
                # for i in range(len(neighboringCells)):
                #     if not (x-1, y, x, y) in maze.openedEntranceToCells and not doesContainStartingCoords:
                #         pygame.draw.line(window, wallsColor, *right_border_offset, width=thickness)
                #         # renderLine(window, wallsColor, *right_border_offset, thickness)
                #         # pygame.draw.rect(window, wallsColor, pygame.Rect(*right_border_offset))

                #         # pygame.draw.line(window, wallsColor, (right_border_offset[0].x, right_border_offset[0].y), (right_border_offset[1].x, right_border_offset[1].y), width=lineThickness)
                #     else:
                #         if (x+i, y) in shortestPath and (x,y) in shortestPath:
                #             pygame.draw.line(window, coloredLine, *right_border_offset1, width=thickness)

                #     if not (x,y,x+i,y) in maze.openedEntranceToCells:
                #         pygame.draw.line(window, wallsColor, *left_border_offset, width=thickness)
                #     else:
                #         if (x, y) in shortestPath and (x+i,y) in shortestPath:
                #             pygame.draw.line(window, coloredLine, *left_border_offset1, width=thickness)
                        
                #     if not (x,y+i,x,y) in maze.openedEntranceToCells:
                #         pygame.draw.line(window, wallsColor, *tileMazeCell_offset, width=thickness)
                #     else:
                #         if (x, y+i) in shortestPath and (x,y) in shortestPath:
                #             pygame.draw.line(window, coloredLine, *tileMazeCell_offset1, width=thickness)
                        
                #     if not (x,y,x,y+1) in maze.openedEntranceToCells and not doesContainEndingCoords:
                #         pygame.draw.line(window, wallsColor, *bottom_border_offset, width=thickness)
                #     else:
                #         if (x, y) in shortestPath and (x, y+i) in shortestPath:
                #             pygame.draw.line(window, coloredLine, *bottom_border_offset1, width=thickness)
                #             # pygame.draw.rect(surface, coloredLine, pygame.Rect(*bottom_border_offset1))

                if not (x-1, y, x, y) in maze.openedEntranceToCells and not doesContainStartingCoords:
                    pygame.draw.line(window, wallsColor, *right_border_offset, width=thickness)
                    # renderLine(window, wallsColor, *right_border_offset, thickness)
                    # pygame.draw.rect(window, wallsColor, pygame.Rect(*right_border_offset))

                    # pygame.draw.line(window, wallsColor, (right_border_offset[0].x, right_border_offset[0].y), (right_border_offset[1].x, right_border_offset[1].y), width=lineThickness)
                else:
                    if (x-1, y) in shortestPath and (x,y) in shortestPath:
                        pygame.draw.line(window, coloredLine, *right_border_offset1, width=thickness)

                if not (x,y,x+1,y) in maze.openedEntranceToCells:
                    pygame.draw.line(window, wallsColor, *left_border_offset, width=thickness)
                else:
                    if (x, y) in shortestPath and (x+1,y) in shortestPath:
                        pygame.draw.line(window, coloredLine, *left_border_offset1, width=thickness)
                    
                if not (x,y-1,x,y) in maze.openedEntranceToCells:
                    pygame.draw.line(window, wallsColor, *tileMazeCell_offset, width=thickness)
                else:
                    if (x, y-1) in shortestPath and (x,y) in shortestPath:
                        pygame.draw.line(window, coloredLine, *tileMazeCell_offset1, width=thickness)
                    
                if not (x,y,x,y+1) in maze.openedEntranceToCells and not doesContainEndingCoords:
                    pygame.draw.line(window, wallsColor, *bottom_border_offset, width=thickness)
                else:
                    if (x, y) in shortestPath and (x, y+1) in shortestPath:
                        pygame.draw.line(window, coloredLine, *bottom_border_offset1, width=thickness)
                        # pygame.draw.rect(surface, coloredLine, pygame.Rect(*bottom_border_offset1))

        generateNewButton.draw(window)
        clearButton.draw(window)
        quitButton.draw(window)
        pygame.display.update()

        clock.tick(FPS)

if __name__ == "__main__":
    main()