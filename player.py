from unit import Unit

class Player(Unit):
    def __init__(self, y, x, name, faction):
        super().__init__(y, x, name, faction)
        self.experience = 0
    
    def earnXP(self, amount):
        self.experience += amount
    
    def move(self, yMod, xMod):
        self.y += yMod
        self.x += xMod