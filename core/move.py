class Move:
    def __init__(self, r, c, player):
        self.r = r
        self.c = c
        self.player = player

    def __repr__(self):
        return f"Move({self.r}, {self.c}, Player {self.player})"