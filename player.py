from unit import Unit
from assets import ImageTypes

class Player(Unit):
    def __init__(self, y, x, name, faction, imageType):
        super().__init__(y, x, name, faction, imageType)
        self.experience = 0
    
    def earnXP(self, amount):
        self.experience += amount