# Store all the constants
class Constants:
    FRAME_BLANK = 50
    GRID_LEHGTH = 70
    SIZE = 15
    WIN = 5
    WIDTH = FRAME_BLANK * 2 + (SIZE - 1) * GRID_LEHGTH
    HEIGHT = WIDTH
    DIAMETER = GRID_LEHGTH - 10
    PLAYER1 = 'Player'
    PLAYER2 = 'Computer'
    DIST_TLRC = GRID_LEHGTH // 2
    NO_STONE = 0
    RECT_THKNS = 100
    DELAY_TIME = 1000
    START_TIME = 0
    DIRECTIONS = [(1, 1), (1, -1), (0, 1), (1, 0)]
    GRIDX = 0
    GRIDY = 1
    GRIDZ = 2
    START = 0
    STEP = 1

    GRID = []
    for i in range(SIZE):
        for j in range(SIZE):
            GRID.append((i, j))

    @staticmethod
    def dist(n):
        # from (x, y) to real distance
        # (0, 0) -> (100, 100), the left and up most cell
        return Constants.FRAME_BLANK + n * Constants.GRID_LEHGTH

    @staticmethod
    def in_range(grid):
        x = grid[Constants.GRIDX]
        y = grid[Constants.GRIDY]
        return x >= Constants.START and x < Constants.SIZE and\
            y >= Constants.START and y < Constants.SIZE
