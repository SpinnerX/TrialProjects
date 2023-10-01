import pygame
from pygame.locals import *
from MazeGenerator import MazeGenerator
import sys
from Djikstra import Dijkstras
from Button import Button
from Tile import Tile
import random


class Animations():
    # Specifying specific specs that the animations need to work
    def __init__(self, mazeSize, color):
        self.mazeSize = mazeSize
        self.currentTileAnimated = None
        self.step = None

        # Animating ranges
        self.minAlpha = 0
        self.maxAlpha = 170
        self.color = color
        self.buffer = None

    def start(self, current: Tile):
        self.currentTileAnimated = current

    def reset(self):
        self.currentTileAnimated = None

    def update(self, mouseCurrentTile, x, y):
        if x >= 0 and y >= 0 and x >= self.mazeSize[0] and y  >= self.mazeSize[1]:
            mouseCurrentTile = Tile(x,y)

            if self.currentTileAnimated != mouseCurrentTile:
                self.currentTileAnimated = mouseCurrentTile
            else:
                self.reset()


    def render(self, window, tileSize, boardX, boardY, cyanColor):
        if self.currentTileAnimated != None:
            cyanColor.a =  250 # Setting alpha color to 250, whichh sets the transparency
            pygame.draw.rect(window, cyanColor, pygame.Rect(boardX+self.currentTileAnimated.x*tileSize, boardY+self.currentTileAnimated.y*tileSize,tileSize, tileSize), width=0) # Used for currentTileAnimate the box
        # pygame.draw.rect(window, self.color, pygame.Rect(boardX+self.currentTileAnimated.x*tileSize, boardY+self.currentTileAnimated.y*tileSize,tileSize, tileSize))