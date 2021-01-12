from enum import Enum
import pygame

class Actions(Enum):
    MOVE_UP = 0
    MOVE_DOWN = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3


def translateActions(event):
    if event.key == pygame.K_w:
        return Actions.MOVE_UP
    elif event.key == pygame.K_a:
        return Actions.MOVE_LEFT
    elif event.key == pygame.K_s:
        return Actions.MOVE_DOWN
    elif event.key == pygame.K_d:
        return Actions.MOVE_RIGHT