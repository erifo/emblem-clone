import sys, pygame
from terrain import Terrain

#Pixels
CELL_SIZE = 40
WALL_WIDTH = 1

#RGB
CELL_COLOR = {
    Terrain.GRASS: (50,150,50),
    Terrain.WATER: (50,50,150),
    Terrain.WOOD: (101, 67, 33),
    Terrain.UNIT: (200, 40, 40)
}
GRID_COLOR = (10,10,10)

class GFX():
    def __init__(self, board, player, originY, originX):
        self.board = board
        self.player = player
        self.originY = originY
        self.originX = originX
        self.screenSize = (self.board.WIDTH*CELL_SIZE)+10, (self.board.HEIGHT*CELL_SIZE)+10 #tuple
        self.screen = pygame.display.set_mode(self.screenSize)

    def drawCells(self):
        for cell in self.board.cells:
            y = self.originY + (cell.y * CELL_SIZE)
            x = self.originX + (cell.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            pygame.draw.rect(self.screen, CELL_COLOR[cell.type], [x, y, width, height])

    def drawGrid(self):
        for cell in self.board.cells:
            y = self.originY + (cell.y * CELL_SIZE)
            x = self.originX + (cell.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            linesToDraw = []
            linesToDraw.append([(x+width, y), (x+width, y+height)]) #Right
            linesToDraw.append([(x, y), (x, y+height)]) #Left
            linesToDraw.append([(x, y+height), (x+width, y+height)]) #Down
            linesToDraw.append([(x, y), (x+width, y)]) #Up
            for line in linesToDraw:
                pygame.draw.line(self.screen, GRID_COLOR, line[0], line[1], width=WALL_WIDTH)

    def drawUnits(self):
        for unit in self.board.units:
            y = self.originY + (unit.y * CELL_SIZE)
            x = self.originX + (unit.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            pygame.draw.rect(self.screen, CELL_COLOR[Terrain.UNIT], [x, y, width, height])


    def drawBoard(self):
            #Draw Background
            black = (0,0,0)
            self.screen.fill(black)
            self.drawCells()
            self.drawUnits()
            self.drawGrid()
            pygame.display.flip()