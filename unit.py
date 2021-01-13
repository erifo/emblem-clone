from stats import Stats
from element import Element

class Unit(Element):
    def __init__(self, y, x, name, faction, imageType):
        super().__init__(y, x, imageType)
        self.name = name
        self.faction = faction
        self.stats = Stats()
    
    def move(self, yMod, xMod):
        self.y += yMod
        self.x += xMod