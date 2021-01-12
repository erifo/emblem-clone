import sys, pygame
from board import Board
from gfx import GFX
    
#Squares.
HEIGHT = 16
WIDTH = 16

#Pixels
ORIGIN_Y = 5
ORIGIN_X = 5

def showNewBoard():
    b = Board(HEIGHT, WIDTH)
    gfx = GFX(b)
    gfx.drawBoard(ORIGIN_Y, ORIGIN_X)

def main():
    pygame.init()
    pygame.display.set_caption("Emblem Clone")
    
    showNewBoard()

    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                showNewBoard()

if __name__ == "__main__":
    main()
