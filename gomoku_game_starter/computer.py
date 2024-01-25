# Set a player and their movement
from stone import Stone
from constants import Constants as C
import random


class Computer():
    def __init__(self, board, name, player):
        self.name = name
        self.board = board
        self.last_move = ()
        self.opposite = player
        self.players = [self, self.opposite]

        self.next_move = ()
        self.left_end = ()  # positive direction
        self.right_end = ()  # negative direction

    # Main function to find next move
    def find_move(self):
        # First step! Milestone!
        if self.last_move == ():
            self.random_around()

        else:
            # 1 - when 1 step last to win
            if self.n_m_ends(5, 2) or self.n_m_ends(5, 1) or\
               self.n_m_ends(5, 0):
                return

            # intersection:
            if self.n_m_intersection(4, 2, 4, 2):
                return
            if self.n_m_intersection(4, 2, 4, 1):
                return
            if self.n_m_intersection(4, 1, 4, 1):
                return
            if self.n_m_intersection(3, 2, 4, 2):
                return
            if self.n_m_intersection(3, 2, 4, 1):
                return

            # 2 - when have 2+0+1 - 2 or 0+0+3 - 2
            if self.n_m_ends(4, 2):
                return

            # intersection:
            if self.n_m_intersection(3, 2, 3, 2):
                return
            if self.n_m_intersection(2, 2, 3, 2):
                return

            # 3 - when have 2 - 2 or 1+0+1 - 2
            if self.n_m_ends(3, 2):
                return
            if self.n_m_intersection(2, 2, 2, 2):
                return

            # 4 - when have 1 - 2
            if self.n_m_ends(4, 1):
                return
            if self.n_m_ends(2, 2):
                return

            self.random_all()

    # Make next move
    def make_move(self):
        self.find_move()
        this_stone = Stone(self.next_move, self)
        if self.board.place_stone(self.next_move, this_stone):
            print("---------------------------------------")
            self.last_move = self.next_move
            self.clear()
            return True
        return False

    # Find a row of n with ends of m in the whole board
    # At an empty cell with stone(s) around
    # Mine first, opposite next
    def n_m_ends(self, n, m):
        for player in self.players:
            for i in C.GRID:
                if self.around_grid(i):
                    if self.n_m_ends_helper(i, n, m, player):
                        print(player.name + " row " + str(
                            n) + ", " + str(m) + " at " + str(i))
                        return True
                    self.clear()
        return False

    # Find a row of n in the whole board
    # Of one player
    def n_m_ends_helper(self, grid, n, m, player):
        for d in C.DIRECTIONS:
            if self.n_m_helper(n, m, grid, player, d):
                self.next_move = grid
                print('move:' + str(self.next_move))
                return True

    # Find intersection in the whole board
    # At an empty cell with stone(s) around
    # Mine first, opposite next
    def n_m_intersection(self, n1, m1, n2, m2):
        for player in self.players:
            for i in C.GRID:
                if self.around_grid(i):
                    if self.n_m_intersection_helper(i, n1, m1, n2, m2, player):
                        print(player.name + " intersention: of " + str(
                            n1) + ' and ' + str(n2) + " at " + str(i))
                        return True
        return False

    # Find intersection in the whole board
    # of one player
    def n_m_intersection_helper(self, grid, n1, m1, n2, m2, player):
        for d1 in C.DIRECTIONS:
            temp_ds = C.DIRECTIONS[:]
            temp_ds.remove(d1)
            for d2 in temp_ds:
                if self.n_m_helper(n1, m1, grid, player, d1):
                    if self.n_m_helper(n2, m2, grid, player, d2):
                        self.next_move = grid
                        print('move:' + str(self.next_move))
                        return True
        self.clear()

    # Base Case
    # Fine a row of n at one grid in one direction
    def n_m_helper(self, n, m, grid, player, d):
        line = self.count_one_line_player(grid, d, player)
        empty = self.count_one_line_room(grid, d, player)

        if sum(line) >= n and sum(line) + sum(empty) - C.STEP >= C.WIN:
            one_side = line[C.GRIDX]
            other_side = line[C.GRIDZ]

            startX = grid[C.GRIDX]
            startY = grid[C.GRIDY]
            dx = d[C.GRIDX]
            dy = d[C.GRIDY]
            self.left_end = (
                startX + dx*(one_side+C.STEP), startY + dy*(one_side+C.STEP))
            self.right_end = (
                startX - dx*(other_side+C.STEP), startY - dy*(other_side+C.STEP))

            empty_ends = set()
            if self.board.is_cell_empty(self.left_end):
                empty_ends.add(self.left_end)
            if self.board.is_cell_empty(self.right_end):
                empty_ends.add(self.right_end)

            if len(empty_ends) == m:
                return True  # elements written

        self.clear()
        return False

    # Count one player's stone at one direction of one grid
    def count_one_dir(self, grid, d, player):  # range:(0,size)
        count = C.START
        grid = (grid[C.GRIDX] + d[C.GRIDX], grid[C.GRIDY] + d[C.GRIDY])

        while C.in_range(grid) and self.board.get_player(grid) == player:
            count += C.STEP
            grid = (grid[C.GRIDX] + d[C.GRIDX], grid[C.GRIDY] + d[C.GRIDY])

        return count

    # Count one player's stone and empty grid at one direction of one grid
    # Until meet the opposite's stone or boundry
    def count_one_dir_room(self, grid, d, player):  # range:(0,size)
        count = C.START
        grid = (grid[C.GRIDX] + d[C.GRIDX], grid[C.GRIDY] + d[C.GRIDY])

        while C.in_range(grid) and (self.board.get_player(grid) == player or self.board.get_player(grid) is None):
            if self.board.get_player(grid) is None:
                count += C.STEP
            grid = (grid[C.GRIDX] + d[C.GRIDX], grid[C.GRIDY] + d[C.GRIDY])

        return count

    # Count one player's stone at both directions of one grid
    def count_one_line_player(self, grid, d, player):
        count = C.STEP  # Count the current grid
        one_side = self.count_one_dir(grid, d, player)
        other_side = self.count_one_dir(grid, self.converse(d), player)

        return [one_side, count, other_side]

    # Count one player's stone and empty grid at both directions of one grid
    # Until meet the opposite's stone or boundry
    def count_one_line_room(self, grid, d, player):
        count = C.STEP  # Count the current grid
        one_side = self.count_one_dir_room(grid, d, player)
        other_side = self.count_one_dir_room(grid, self.converse(d), player)

        return [one_side, count, other_side]

    # Random pick one empty grid from those around one stone
    def random_around(self):
        oplm = self.opposite.last_move
        plmX = oplm[C.GRIDX]
        plmY = oplm[C.GRIDY]
        x_min = max(C.START, plmX - C.STEP)
        y_min = max(C.START, plmY - C.STEP)
        x_max = min(self.board.size, plmX + 2)
        y_max = min(self.board.size, plmY + 2)

        find = False
        while not find:
            nextX = random.randrange(x_min, x_max)
            nextY = random.randrange(y_min, y_max)
            if self.board.is_cell_empty((nextX, nextY)):
                self.next_move = (nextX, nextY)
                print("random at " + str(self.next_move))
                return

    # Random pick one empty grid from all empty grids
    def random_all(self):
        while True:
            move = random.choice(C.GRID)
            if self.board.is_cell_empty(move):
                self.next_move = move
                break

    # Check if there are any stones around the grid
    def around_grid(self, grid):
        if self.board.get_player(grid) is None:
            x = grid[C.GRIDX]
            y = grid[C.GRIDY]
            x_min = max(C.START, x-C.STEP)
            y_min = max(C.START, y-C.STEP)
            x_max = min(self.board.size, x+2)
            y_max = min(self.board.size, y+2)
            around = set()
            for x in range(x_min, x_max):
                for y in range(y_min, y_max):
                    around.add((x, y))
            around.remove(grid)

            for i in around:
                if not self.board.is_cell_empty(i):
                    return True
        return False

    # Give the opposite direction of the given direction
    def converse(self, d):
        return (-d[C.GRIDX], -d[C.GRIDY])

    # clean the record of last move or unsuccessful search
    def clear(self):
        self.next_move = ()
        self.left_end = ()
        self.right_end = ()
