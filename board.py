from random import randint
from cell import Cell
from assets import ImageTypes
from player import Player
from unit import Unit


class Board():
    def __init__(self, height, width):
        self.HEIGHT = height #cells
        self.WIDTH = width #cells
        self.player = Player(2, 2, "Ratel", 0, ImageTypes.UNIT_HERO)
        self.cells = []
        self.units = []
        self.generateCells()
        self.terraform()
        self.generateUnits()
    
    def generateCells(self):
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                self.cells.append(Cell(y, x, ImageTypes.NONE))
    
    def getCellAt(self, y, x):
        for cell in self.cells:
            if cell.y == y and cell.x == x:
                return cell
        print("ERROR: Cell", y, x, "does not exist!")
    
    def isUnitAt(self, y, x):
        for unit in self.units:
            if unit.y == y and unit.x == x:
                return True
        return False

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
    
    def generateUnit(self):
        while (True):
            y = randint(0, self.HEIGHT-1)
            x = randint(0, self.WIDTH-1)
            if not self.getCellAt(y, x).passable:
                continue
            if self.isUnitAt(y, x):
                continue
            break
        return Unit(y, x, "Bandit", 1, ImageTypes.UNIT_BANDIT)

    def generateUnits(self):
        for i in range(5): #Amount of Units to create.
            self.units.append(self.generateUnit())