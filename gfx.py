import sys, pygame

#Pixels
CELL_SIZE = 30
WALL_WIDTH = 1

#RGB
CELL_COLOR = {
    "grass": (50,150,50),
    "water": (50,50,150),
    "wood": (101, 67, 33)
}
GRID_COLOR = (10,10,10)

class GFX():
    def __init__(self, board):
        self.board = board
        self.screenSize = (self.board.WIDTH*CELL_SIZE)+10, (self.board.HEIGHT*CELL_SIZE)+10 #tuple
        self.screen = pygame.display.set_mode(self.screenSize)

    def drawCell(self, originY, originX):
        for cell in self.board.cells:
            y = originY + (cell.y * CELL_SIZE)
            x = originX + (cell.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            pygame.draw.rect(self.screen, CELL_COLOR[cell.type], [x, y, width, height])

    def drawWalls(self, originY, originX):
        for cell in self.board.cells:
            y = originY + (cell.y * CELL_SIZE)
            x = originX + (cell.x * CELL_SIZE)
            height =  CELL_SIZE
            width = CELL_SIZE
            linesToDraw = []
            linesToDraw.append([(x+width, y), (x+width, y+height)]) #Right
            linesToDraw.append([(x, y), (x, y+height)]) #Left
            linesToDraw.append([(x, y+height), (x+width, y+height)]) #Down
            linesToDraw.append([(x, y), (x+width, y)]) #Up
            for line in linesToDraw:
                pygame.draw.line(self.screen, GRID_COLOR, line[0], line[1], width=WALL_WIDTH)

    def drawBoard(self, originY, originX):
            #Draw Background
            black = (0,0,0)
            self.screen.fill(black)
            self.drawCell(originY, originX)
            self.drawWalls(originY, originX)
            pygame.display.flip()