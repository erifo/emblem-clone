from cell import Cell

class Board():
    def __init__(self, height, width):
        self.HEIGHT = height #cells
        self.WIDTH = width #cells
        self.cells = []
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
            cell.type = "grass"

        #Add L-shaped river
        for y in range(self.HEIGHT):
            if y > (self.HEIGHT//3*2)+2:
                break
            if y <= self.HEIGHT//3*2:
                for x in range((self.WIDTH//2)-1, (self.WIDTH//2)+1):
                    self.getCellAt(y,x).type = "water"
            else:
                for x in range((self.WIDTH//2)-1, self.WIDTH):
                    self.getCellAt(y,x).type = "water"
        
        #Add two bridges
        for y in range((self.HEIGHT//3)-2, self.HEIGHT//3):
            for x in range((self.WIDTH//2)-1, (self.WIDTH//2)+1):
                self.getCellAt(y,x).type = "wood"
        
        for y in range((self.HEIGHT//3*2)+1, (self.HEIGHT//3*2)+3):
            for x in range((self.WIDTH//3*2)+2, (self.WIDTH//3*2)+4):
                self.getCellAt(y,x).type = "wood"
        
