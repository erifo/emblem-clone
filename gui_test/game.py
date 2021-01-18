import pygame
from menu import Menu
from menu_model import MenuModel
from menu_view import MenuView
from menu_controller import MenuController

class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Menu Test")
        self.font = pygame.font.Font("gui_test/snesfont.ttf", 40)
        self.screen = pygame.display.set_mode((self.width, self.height))
        #---
        self.menu = Menu(MenuModel(10, 10),
                         MenuView(self.screen, self.font),
                         MenuController())


    def update(self):
        self.screen.fill((0,255,0)) #Screen baseline color.
        self.menu.update()
        pygame.display.flip()
    
    def start(self):
        while(True):
            self.update()