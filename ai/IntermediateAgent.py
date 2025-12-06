import random
import math

# نقوم باستيراد الخوارزمية من الملف المجاور
from ai.algorithm import minimax, move_generator

class IntermediateAgent(BaseAgent):
    """Uses Minimax with low depth (e.g., 2)."""
    def get_move(self, game_state):
        # Depth 2 سريع ومناسب للمستوى المتوسط
        _, move = minimax(game_state, 2, -math.inf, math.inf, True, self.color)
        return move