from cell import Cell
from assets import ImageTypes


class Board():
    def __init__(self, height, width):
        self.HEIGHT = height #cells
        self.WIDTH = width #cells
        self.cells = []
        self.units = []
        self.generateCells()
        self.terraform()
    
    def generateCells(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                self.cells.append(Cell(y, x))
    
    def getCellAt(self, y, x):
        for cell in self.cells:
            if cell.y == y and cell.x == x:
                return cell
        print("ERROR: Cell", y, x, "does not exist!")

    def terraform(self):
        #Default to grasslands
        for cell in self.cells:
            cell.imageType = ImageTypes.TILE_GRASS

        #Add L-shaped river
        for y in range(self.HEIGHT):
            if y > (self.HEIGHT//3*2)+2:
                break
            if y <= self.HEIGHT//3*2:
                for x in range((self.WIDTH//2)-1, (self.WIDTH//2)+1):
                    c = self.getCellAt(y,x)
                    c.imageType = ImageTypes.TILE_WATER
                    c.passable = False
            else:
                for x in range((self.WIDTH//2)-1, self.WIDTH):
                    c = self.getCellAt(y,x)
                    c.imageType = ImageTypes.TILE_WATER
                    c.passable = False
        
        #Add two bridges
        for y in range((self.HEIGHT//3)-2, self.HEIGHT//3):
            for x in range((self.WIDTH//2)-1, (self.WIDTH//2)+1):
                c = self.getCellAt(y,x)
                c.imageType = ImageTypes.TILE_WOOD
                c.passable = True
        
        for y in range((self.HEIGHT//3*2)+1, (self.HEIGHT//3*2)+3):
            for x in range((self.WIDTH//3*2)+2, (self.WIDTH//3*2)+4):
                c = self.getCellAt(y,x)
                c.imageType = ImageTypes.TILE_WOOD
                c.passable = True