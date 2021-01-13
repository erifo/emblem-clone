import sys, pygame, os.path
from board import Board
from gfx import GFX
from controls import Actions, translateActions
from player import Player
from logic import Logic
from assets import ImageTypes
    
#Squares
HEIGHT = 14
WIDTH = 16

#Pixels
ORIGIN_Y = 5
ORIGIN_X = 5

def main():
    pygame.init()
    pygame.display.set_caption("Emblem Clone")
    
    board = Board(HEIGHT, WIDTH)
    player = Player(2, 2, "Ratel", 0)
    board.units.append(player)
    logic = Logic() 
    gfx = GFX(board, player, ORIGIN_Y, ORIGIN_X)

    gfx.drawBoard() #Initial display

    while (True):
        actions = []
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                actions.append(translateActions(event))
            if (event.type == pygame.QUIT):
                sys.exit()
        logic.handleActions(actions, player, board)
        gfx.drawBoard()

if __name__ == "__main__":
    main()
