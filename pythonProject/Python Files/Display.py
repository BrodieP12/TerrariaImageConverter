import pygame
from PIL import Image
import typing
from math import sqrt
from itertools import groupby
import random
import math
import TerrariaColorMatcher as TCM
from six.moves import zip_longest # for both (uses the six compat library)

class Grid:
    def __init__(self):
        self.img = Image.open("Abeemination.png").convert("RGB")
        self.moddedImg = TCM.modifyPic(self.img)
        self.moddedImg.show()
        self.width, self.height = self.moddedImg.size
        self.width += 1
        self.grid_size = 5
        ExtBlockList = []
        ExtColorList = []
        if isinstance(self.width/self.grid_size, float):
            self.grid_x = math.floor(self.width/self.grid_size)
            self.grid_xR = self.width%self.grid_size
            for i in range(self.grid_xR):
                ExtBlockList.append("Sail")
                ExtColorList.append((0,0,0))
        else:
            self.grid_x = self.width / self.grid_size
            self.grid_xR = 0
        if isinstance(self.height / self.grid_size, float):
            self.grid_y = math.floor(self.height / self.grid_size)
            self.grid_yR = self.height % self.grid_size
        else:
            self.grid_y = self.height / self.grid_size
            self.grid_yR = 0
        print(self.grid_x)
        print(self.grid_y)
        print(self.grid_xR)
        print(self.grid_yR)
    def createFullGrid(self):
        self.FullGrid = []
        self.FullBlockImage = []
        self.FullColorImage = []
        for y in range(self.height):
            self.FullGrid.append([])
            for x in range(self.width):
                self.FullGrid[y].append([])
            #self.FullBlockImage.append(self.Block0)
            #self.FullColorImage.append(self.Blocks2)

        #print(self.FullBlockImage)
    def splitLists(self, size):
        self.SplitBlocks = []
        self.SplitColors = []
        for j in range(self.width):
            self.Blocks2, self.Block0 = TCM.createRowInstructions(self.moddedImg, j, True, ["Colors", "Blocks Pixel Art"])
            self.SplitBlocks.append(list(self.grouper(5, self.Block0, "x")))
            self.SplitColors.append(list(self.grouper(5, self.Blocks2, (0, 0, 0))))
        self.AllSplitBlocks = list(self.grouper(5, self.SplitBlocks, "x"))
        self.AllSplitColors = list(self.grouper(5, self.SplitColors, "x"))
        print(self.SplitBlocks)
    def createGrids(self):
        self.BlockGrids = []
        self.ColorGrids = []
        #(self.AllSplitBlocks)
        count = 0
        for i in range(len(self.AllSplitBlocks[0])-1):
            self.BlockGrids.append([])
            self.ColorGrids.append([])
            for j in range(len(self.SplitBlocks[0])):
                self.BlockGrids[i].append([])
                self.ColorGrids[i].append([])
                for k in range(5):
                    self.BlockGrids[i][j].append(self.SplitBlocks[k][j])
                    self.ColorGrids[i][j].append(self.SplitColors[k][j])
        print(self.BlockGrids[0])

        print(self.ColorGrids[0])
    def grouper(self, n, iterable, padvalue=None):
        "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
        return zip_longest(*[iter(iterable)] * n, fillvalue=padvalue)







g = Grid()
g.splitLists(5)
g.createGrids()
#for i in range(moddedImg.size[1]):

pygame.init()
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pixel Art Helper")
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
grid = []
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5
for row in range(5):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(5):
        grid[row].append(0)
# -------- Main Program Loop -----------
while running:
    # --- Main event loop
    # Here is one event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = g.ColorGrids[0][0][0][0]
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
pygame.quit()