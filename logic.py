from controls import Actions
from player import Player

class Logic():
    def __init__(self):
        pass

    def canMove(self, player, board, yMod, xMod):
        if (player.y+yMod < 0 or player.y+yMod >= board.HEIGHT):
            return False
        if (player.x+xMod < 0 or player.x+xMod >= board.WIDTH):
            return False
        if not board.getCellAt(player.y+yMod, player.x+xMod).passable:
            return False
        return True

    def handleMove(self, player, board, yMod, xMod):
        if self.canMove(player, board, yMod, xMod):
            player.move(yMod, xMod)

    def handleActions(self, actions, player, board):
        for action in actions:
            if action == Actions.MOVE_UP:
                self.handleMove(player, board, -1, 0)
            elif action == Actions.MOVE_DOWN:
                self.handleMove(player, board, 1, 0)
            elif action == Actions.MOVE_LEFT:
                self.handleMove(player, board, 0, -1)
            elif action == Actions.MOVE_RIGHT:
                self.handleMove(player, board, 0, 1)