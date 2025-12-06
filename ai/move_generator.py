import math
import random


def move_generator(game_state):
    """
    Returns a list of all valid moves for the current player.
    """
    return game_state.get_valid_moves()

