from unit import Unit
from assets import ImageTypes

class Player(Unit):
    def __init__(self, y, x, name, faction):
        super().__init__(y, x, name, faction)
        self.experience = 0
        self.imageType = ImageTypes.UNIT_HERO
    
    def earnXP(self, amount):
        self.experience += amount
    
    def move(self, yMod, xMod):
        self.y += yMod
        self.x += xMod