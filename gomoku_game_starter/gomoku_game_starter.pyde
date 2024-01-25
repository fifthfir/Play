from constants import Constants as C
from board import Board
from player import Player
from game_controller import GameController
from computer import Computer


board = Board(C.SIZE)
player = Player(board, C.PLAYER1)
computer = Computer(board, C.PLAYER2, player)
gc = GameController(board, player, computer)

recorded = False
game_end = False


def setup():
    size(C.WIDTH, C.HEIGHT)
    background(239, 231, 214)
    board.display_grid()


def draw():
    global recorded, game_end
    if not game_end:
        # will have little bug when use gc.game_ends directly
        gc.update_computer()
        board.display_stones()
        if gc.game_ends:
            board.display_stones()
            gc.update_win()
            game_end = True
    else:
        if not recorded and gc.winner == player:
            winner = input('enter your name')
            gc.name_record(winner)
            recorded = True


def mouseClicked():
    gc.mouse_click()


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
