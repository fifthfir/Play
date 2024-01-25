# Make a stone in specific color
from constants import Constants as C


class Stone:
    def __init__(self, grid, player):
        self.grid = grid  # 0, 1, 2
        self.x = grid[C.GRIDX]
        self.y = grid[C.GRIDY]
        self.player = player
        self.diameter = C.DIAMETER

    def display(self):
        strokeWeight(4)
        if self.grid == self.player.last_move:
            stroke(255, 235, 50)
        else:
            stroke(255)
        if self.player.name == C.PLAYER1:
            fill(102, 195, 180)
        if self.player.name == C.PLAYER2:
            fill(234, 115, 85)

        ellipse(C.dist(self.x), C.dist(self.y), self.diameter, self.diameter)

    def get_s_player(self):
        return self.player
