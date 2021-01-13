from controls import Actions
from player import Player

class Logic():
    def __init__(self):
        pass

    def canUnitMove(self, unit, board, yMod, xMod):
        if (unit.y+yMod < 0 or unit.y+yMod >= board.HEIGHT):
            return False
        if (unit.x+xMod < 0 or unit.x+xMod >= board.WIDTH):
            return False
        if not board.getCellAt(unit.y+yMod, unit.x+xMod).passable:
            return False
        return True

    def unitMovement(self, unit, board, yMod, xMod):
        if self.canUnitMove(unit, board, yMod, xMod):
            board.player.move(yMod, xMod)

    def handleActions(self, actions, board):
        for action in actions:
            if action == Actions.MOVE_UP:
                self.unitMovement(board.player, board, -1, 0)
            elif action == Actions.MOVE_DOWN:
                self.unitMovement(board.player, board, 1, 0)
            elif action == Actions.MOVE_LEFT:
                self.unitMovement(board.player, board, 0, -1)
            elif action == Actions.MOVE_RIGHT:
                self.unitMovement(board.player, board, 0, 1)