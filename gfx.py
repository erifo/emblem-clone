import sys, pygame
from assets import Assets, ImageTypes

#Pixels
CELL_SIZE = 50
WALL_WIDTH = 1

#RGB
GRID_COLOR = (10,10,10)


class GFX():
    def __init__(self, board, player, originY, originX):
        self.board = board
        self.player = player
        self.originY = originY
        self.originX = originX
        self.screenSize = (self.board.WIDTH*CELL_SIZE)+10, (self.board.HEIGHT*CELL_SIZE)+10 #tuple
        self.screen = pygame.display.set_mode(self.screenSize)
        self.assets = Assets()

    def drawCells(self):
        for cell in self.board.cells:
            y = self.originY + (cell.y * CELL_SIZE)
            x = self.originX + (cell.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            image = self.assets.images[cell.imageType]
            image = pygame.transform.scale(image, (width, height))
            self.screen.blit(image, (x,y))

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
            height = CELL_SIZE
            width = CELL_SIZE
            image = self.assets.images[unit.imageType]
            image = pygame.transform.scale(image, (width, height))
            self.screen.blit(image, (x,y))
            

    def drawBoard(self):
            #Draw Background
            black = (0,0,0)
            self.screen.fill(black)
            self.drawCells()
            self.drawUnits()
            self.drawGrid()
            pygame.display.flip()