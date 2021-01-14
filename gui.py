from enum import Enum


class Menu():
    def __init__(self, y, x):
        self.active = False
        self.y = y
        self.x = x

class Option():
    def __init__(self, text, menu):
        self.text = text
        self.menu = menu

class SelectMenu(Menu):
    def __init__(self, y, x, options):
        super().__init__(y, x)
        self.text = text
        self.options = []

class CharacterMenu(Menu):
    def __init__(self, y, x):
        super().__init__(y, x)
        pass
        #Render Character info and portrait here.


class GUI():
    def __init__(self):
        self.setupMenus()
    
    def setupMenus(self):
        oCharacter = Option("Character", CharacterMenu())

        m_pause = SelectMenu(0, 0, [oCharacter])