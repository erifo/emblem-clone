from random import randint

class Stats():
    def __init__(self):
        self.attack = randint(1,5)
        self.defense = randint(0,1)
        self.health = randint(3,7)
        self.initiative = randint(1,10)