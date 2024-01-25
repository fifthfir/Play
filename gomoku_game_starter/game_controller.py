# Control the game flow
from constants import Constants as C


class GameController:
    def __init__(self, board, player1, player2):
        self.board = board

        self.player = player1
        self.computer = player2

        self.game_ends = False
        self.winner = None

        self.delay_time = C.DELAY_TIME
        self.start_time = C.START_TIME
        self.waiting_for_computer = False

    def mouse_click(self):
        if not self.game_ends and not self.waiting_for_computer:
            # my turn
            if self.player.make_move((mouseX, mouseY)):  # move successfully
                self.check_end(self.player.last_move)
                self.waiting_for_computer = True  # opposite turn
                self.start_time = millis()  # time start

    def update_computer(self):
        if not self.game_ends and self.waiting_for_computer:
            # computer's turn
            current_time = millis()
            if current_time - self.start_time >= self.delay_time:
                # wait to act naturally
                self.computer.make_move()
                self.check_end(self.computer.last_move)
                self.waiting_for_computer = False  # my turn

    def check_end(self, move):  # move: (x, y)
        if self.board.is_win(move):
            self.winner = self.board.winner
            self.game_ends = True
        elif self.board.is_draw():
            self.game_ends = True

    def update_win(self):
        if self.game_ends:
            textSize(70)
            textAlign(CENTER, CENTER)
            rectMode(CENTER)

            if self.winner == self.player:
                strokeWeight(0)
                fill(255, 192, 0)
                rect(C.WIDTH // 2, C.HEIGHT // 2, C.WIDTH, C.RECT_THKNS)
                fill(255)
                text("YOU WIN!", C.WIDTH // 2, C.HEIGHT // 2 - 10)

            elif self.winner == self.computer:
                strokeWeight(0)
                fill(255, 192, 0)
                rect(C.WIDTH // 2, C.HEIGHT // 2, C.WIDTH, C.RECT_THKNS)
                fill(255)
                text("COMPUTER WINS!", C.WIDTH // 2, C.HEIGHT // 2 - 10)

            elif self.winner is None:
                strokeWeight(0)
                fill(255)
                rect(C.WIDTH // 2, C.HEIGHT // 2, C.WIDTH, C.RECT_THKNS)
                fill(160)
                text("DRAW", C.WIDTH // 2, C.HEIGHT // 2 - 10)

    def name_record(self, winner_name):
        if winner_name:  # has input
            with open("score.txt", "r+") as f:
                records = [line.strip() for line in f.readlines()]
                dict_to_sort = {}
                saved = False

                # make previous and new record into a dict
                for i in range(len(records)):
                    i_lst = records[i].split()
                    records[i] = i_lst
                    name_i = records[i][C.START]
                    score_i = int(records[i][C.STEP])  # ['Alice', 2]

                    if winner_name == name_i:
                        score_i += C.STEP
                        saved = True
                    dict_to_sort[name_i] = score_i

                if not saved:
                    dict_to_sort[winner_name] = C.STEP

                # sort it by value from high to low
                sorted_dict = sorted(
                    dict_to_sort.items(),
                    key=lambda item: item[C.STEP],
                    reverse=True)

                # rewrite the txt
                f.seek(0)
                f.truncate()
                for i in sorted_dict:
                    f.write(str(i[C.START]) + '\t' + str(i[C.STEP]) + '\n')

                f.close()
