# Set a player and their movement
from constants import Constants as C
from stone import Stone


class Player():
    def __init__(self, board, name):
        self.name = name
        self.board = board
        self.last_move = ()

    def make_move(self, mouse_move):
        mouseX = mouse_move[C.GRIDX]
        mouseY = mouse_move[C.GRIDY]
        for i in C.GRID:
            x = i[C.GRIDX]
            y = i[C.GRIDY]
            if abs(C.dist(x) - mouseX) < C.DIST_TLRC and\
               abs(C.dist(y) - mouseY) < C.DIST_TLRC:
                if self.board.place_stone((x, y), Stone((x, y), self)):
                    self.last_move = (x, y)
                    return True
        return False
