# Make the board list and display the board and the stones in the list
from constants import Constants as C


class Board:
    def __init__(self, size):
        self.size = size
        self.grids = [[C.NO_STONE for i in range(size)] for j in range(size)]
        self.winner = None

    def display_grid(self):  # Grid won't change
        total_length = (self.size - C.STEP) * C.GRID_LEHGTH
        stroke(255)
        strokeWeight(4)
        for i in range(self.size):  # verticle lines
            x = C.FRAME_BLANK + i * C.GRID_LEHGTH
            line(x, C.FRAME_BLANK, x, C.FRAME_BLANK + total_length)
        for j in range(self.size):  # horizontal lines
            y = C.FRAME_BLANK + j * C.GRID_LEHGTH
            line(C.FRAME_BLANK, y, C.FRAME_BLANK + total_length, y)

    def display_stones(self):  # stones change
        for i in C.GRID:
            x = i[C.GRIDX]
            y = i[C.GRIDY]
            cur_cell = self.grids[x][y]
            if cur_cell != C.NO_STONE:
                cur_cell.display()

    def get_player(self, grid):
        if not C.in_range(grid):
            return None
        x = grid[C.GRIDX]
        y = grid[C.GRIDY]
        if self.grids[x][y] == C.NO_STONE:
            return None

        return self.grids[x][y].get_s_player()

    def get_size(self):
        return self.size

    def is_cell_empty(self, grid):
        x = grid[C.GRIDX]
        y = grid[C.GRIDY]
        if x >= C.START and x < self.size and y >= C.START and y < self.size:
            return self.grids[x][y] == C.NO_STONE
        else:
            return False

    def place_stone(self, grid, stone):
        if self.is_cell_empty(grid) and C.in_range(grid):
            self.grids[grid[C.GRIDX]][grid[C.GRIDY]] = stone
            return True
        return False

    def is_draw(self):
        for i in C.GRID:
            if self.is_cell_empty(i):
                return False
        return True

    def is_win(self, grid):
        for dx, dy in C.DIRECTIONS:
            count = 1  # Count the current stone
            count += self.count_stones(grid, dx, dy)  # Count in one direction
            count += self.count_stones(grid, -dx, -dy)  # Count opposite

            if count >= C.WIN:
                self.winner = self.get_player(grid)
                return True

        return False

    def count_stones(self, grid, dx, dy):  # range:(0,)
        player = self.get_player(grid)
        count = C.START
        # Shouldn't include self
        grid = (grid[C.GRIDX] + dx, grid[C.GRIDY] + dy)

        while C.in_range(grid) and self.get_player(grid) == player:
            count += C.STEP
            grid = (grid[0] + dx, grid[1] + dy)

        return count
