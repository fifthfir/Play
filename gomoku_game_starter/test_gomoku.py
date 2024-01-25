from constants import Constants as C  # Size = 5
from board import Board
from computer import Computer
from game_controller import GameController
from player import Player
from stone import Stone


# Innitialization
b = Board(C.SIZE)
p1 = Player(b, C.PLAYER1)
p2 = Computer(b, C.PLAYER2, p1)
gc = GameController(b, p1, p2)

# Mouse move
m1 = (50, 50)

# Grid
g1 = (0, 0)
g2 = (1, 1)

g3 = (0, 1)
g4 = (0, 2)
g5 = (0, 3)
g6 = (0, 4)

# Stone
st1 = Stone(g2, p1)


# Tests
# Player
def test_make_move():
    assert p1.make_move(m1)


# Stone
def test_get_s_player():
    assert st1.get_s_player() == p1


# Board
def test_get_player():
    assert b.get_player(g1) == p1
    assert b.get_player(g2) is None
    assert b.get_player(g3) is None


def test_get_size():
    assert b.get_size() == C.SIZE


def test_is_cell_empty():
    assert not b.is_cell_empty(g1)
    assert b.is_cell_empty(g2)


def test_place_stone():
    assert b.place_stone(g2, st1)
    assert b.get_player(g2) == p1


def test_is_draw():
    for i in C.GRID:
        if b.is_cell_empty(i):
            stone = Stone(i, p1)
            b.place_stone(i, stone)
    assert b.is_draw()


def test_is_win():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    st2 = Stone(g1, p1)
    b.place_stone(g1, st2)
    st3 = Stone(g3, p1)
    b.place_stone(g3, st3)
    st4 = Stone(g4, p1)
    b.place_stone(g4, st4)
    st5 = Stone(g5, p1)
    b.place_stone(g5, st5)
    st6 = Stone(g6, p1)
    b.place_stone(g6, st6)

    assert b.is_win(g1)
    assert b.is_win(g3)
    assert b.is_win(g4)
    assert b.is_win(g5)
    assert b.is_win(g6)


def test_count_stones():
    assert b.count_stones(g1, 1, 1) == 0
    assert b.count_stones(g1, 0, 1) == 4
    assert b.count_stones(g1, 1, 0) == 0
    assert b.count_stones(g2, -1, 1) == 0


# Computer
def test_find_and_make_move():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.make_move()


def test_n_m_ends():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.n_m_ends(5, 1)

    b.place_stone((1, 1), Stone((1, 1), p1))
    b.place_stone((2, 1), Stone((2, 1), p1))
    b.place_stone((3, 1), Stone((3, 1), p1))

    assert p2.n_m_ends(4, 1)
    assert p2.n_m_ends(3, 2)
    assert p2.n_m_ends(2, 1)
    assert p2.n_m_ends(3, 1)
    assert p2.n_m_ends(2, 2)


def test_n_m_ends_helper():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.n_m_ends_helper((4, 0), 4, 1, p1)


def test_n_m_intersection():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 1), Stone((1, 1), p1))
    b.place_stone((3, 1), Stone((3, 1), p1))

    assert p2.n_m_intersection(3, 1, 2, 2)


def test_n_m_intersection_helper():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 1), Stone((1, 1), p1))
    b.place_stone((3, 1), Stone((3, 1), p1))

    assert p2.n_m_intersection_helper((2, 2), 3, 1, 2, 2, p1)


def test_n_m_helper():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.n_m_helper(4, 1, (4, 0), p1, (1, 0))


def test_count_one_dir():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.count_one_dir((3, 0), (1, 0), p1) == 0
    assert p2.count_one_dir((2, 0), (1, 0), p1) == 1
    assert p2.count_one_dir((2, 0), (-1, 0), p1) == 2


def test_count_one_dir_room():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    b.place_stone((5, 0), Stone((5, 0), p2))

    assert p2.count_one_dir_room((3, 0), (1, 0), p1) == 1
    assert p2.count_one_dir_room((3, 0), (-1, 0), p1) == 0


def test_count_one_line_player():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.count_one_line_player((4, 0), (1, 0), p1) == [0, 1, 4]
    assert p2.count_one_line_player((2, 0), (1, 0), p1) == [1, 1, 2]


def test_count_one_line_room():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    b.place_stone((5, 0), Stone((5, 0), p2))

    assert p2.count_one_line_room((3, 0), (1, 0), p1) == [1, 1, 0]
    assert p2.count_one_line_room((2, 0), (1, 0), p1) == [1, 1, 0]


def test_random_around():
    p2.random_around()
    assert b.is_cell_empty(p2.next_move)
    assert p2.next_move in [(0, 1), (1, 1), (1, 0)]


def test_random_all():
    p2.random_all()
    assert b.is_cell_empty(p2.next_move)


def test_around_grid():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))

    assert p2.around_grid((1, 1))
    assert p2.around_grid((0, 1))
    assert not p2.around_grid((0, 5))


def test_converse():
    d = (1, 1)
    assert p2.converse(d) == (-1, -1)


def test_clear():
    p2.next_move = (1, 1)
    p2.left_end = (1, 1)
    p2.right_end = (1, 5)
    p2.clear()

    assert p2.next_move == ()
    assert p2.left_end == ()
    assert p2.right_end == ()


# GameController
def test_check_end():
    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    b.place_stone((0, 0), Stone((0, 0), p1))
    b.place_stone((1, 0), Stone((1, 0), p1))
    b.place_stone((2, 0), Stone((2, 0), p1))
    b.place_stone((3, 0), Stone((3, 0), p1))
    b.place_stone((4, 0), Stone((4, 0), p1))

    gc.check_end((4, 0))
    assert gc.game_ends

    for i in C.GRID:
        b.grids[i[C.GRIDX]][i[C.GRIDY]] = C.NO_STONE
        assert b.is_cell_empty(i)

    gc.game_ends = False

    for i in C.GRID:
        stone = Stone(i, p1)
        b.place_stone(i, stone)

    gc.check_end((4, 0))
    assert gc.game_ends


def test_name_record():
    winner_name = 'test'

    with open("score.txt", "r+") as f:
        records = [line.strip() for line in f.readlines()]
        found = False

        if records:
            for i in range(len(records)):
                i_lst = records[i].split()

                if i_lst[0] == winner_name:
                    found = True

        assert not found
        f.close()

    gc.name_record(winner_name)

    with open("score.txt", "r+") as f:
        records = [line.strip() for line in f.readlines()]
        found = False

        for i in range(len(records)):
            i_lst = records[i].split()
            records[i] = i_lst

            if records[i][0] == winner_name:
                found = True
                assert int(records[i][1]) == 1

        assert found
        f.close()

    gc.name_record(winner_name)

    with open("score.txt", "r+") as f:
        records = [line.strip() for line in f.readlines()]
        found = False

        for i in range(len(records)):
            i_lst = records[i].split()
            records[i] = i_lst

            if records[i][0] == winner_name:
                found = True
                assert int(records[i][1]) == 2

        assert found
        f.close()

    with open("score.txt", "r+") as f:
        records = [line.strip() for line in f.readlines()]
        found = False
        dict_to_sort = {}

        for i in range(len(records)):
            i_lst = records[i].split()
            records[i] = i_lst
            dict_to_sort[records[i][0]] = int(records[i][1])

        sorted_dict = dict(sorted(
            dict_to_sort.items(),
            key=lambda item: item[1],
            reverse=True))

        del sorted_dict[winner_name]

        for key in sorted_dict:
            assert key != winner_name

        # rewrite the txt
        f.seek(0)
        f.truncate()
        for i in sorted_dict:
            f.write(str(i[0]) + '\t' + str(i[1]) + '\n')
