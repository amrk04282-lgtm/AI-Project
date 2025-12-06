import random
import math


from ai.algorithm import minimax, move_generator

class AdvancedAgent(BaseAgent):
    """Uses Minimax with higher depth (e.g., 4)."""
    def get_move(self, game_state):
        # Depth 4 أصعب ويأخذ وقتاً أطول قليلاً في التفكير
        _, move = minimax(game_state, 4, -math.inf, math.inf, True, self.color)
        return move