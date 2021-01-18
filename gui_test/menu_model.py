from random import choice, randint

class MenuItem():
    def __init__(self, text, menu):
        self.text = text
        self.leadsToMenu = menu

class MenuModel(): 
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.active = True
        self.menuItems = []
        self.generateMenuItems() #Examples
    
    def generateMenuItems(self):
        self.menuItems = []
        for i in range(1, randint(4,6)+1):
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            text = ''.join(choice(letters) for i in range(randint(4,9)))
            item = MenuItem(text, None)
            self.menuItems.append(item)