import sys, pygame
from assets import Assets, ImageTypes
from element import Element

#Pixels
CELL_SIZE = 50
WALL_WIDTH = 1

#RGB
GRID_COLOR = (10,10,10)

class GFX():
    def __init__(self, board, originY, originX):
        self.board = board
        self.originY = originY
        self.originX = originX
        self.screenSize = (self.board.WIDTH*CELL_SIZE)+10, (self.board.HEIGHT*CELL_SIZE)+10 #tuple
        self.screen = pygame.display.set_mode(self.screenSize)
        self.assets = Assets()

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

    def drawElements(self, elementList):
        for element in elementList:
            y = self.originY + (element.y * CELL_SIZE)
            x = self.originX + (element.x * CELL_SIZE)
            image = self.assets.images[element.imageType]
            image = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
            self.screen.blit(image, (x,y))

    def drawBoard(self):
            #Draw Background
            black = (0,0,0)
            self.screen.fill(black)
            self.drawElements(self.board.cells)
            self.drawElements(self.board.units)
            self.drawElements( [self.board.player] )
            self.drawGrid()
            pygame.display.flip()