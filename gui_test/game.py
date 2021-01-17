import sys, pygame, os.path
from gui import *

class Game():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.GUI = None
        self.init()

    def init(self):
        pygame.init()
        pygame.display.set_caption("GUI Test")
        #---
        gui_view = GUI_View(height, width)
        gui_controller = GUI_Controller()
        self.gui = GUI(gui_view, gui_controller)


    def update(self):
        self.GUI.update()
    
    def start(self):
        while(True):
            self.update()