from stats import Stats

class Unit():
    def __init__(self, y, x, name, factionID):
        self.y = y
        self.x = x
        self.name = name
        self.factionID = factionID
        self.stats = Stats()
        self.image = None