"""
Minesweeper Game
"""
import random
from tkinter import ttk, Tk, PhotoImage, Canvas, ALL, SUNKEN, X, StringVar, NW

N_IMAGES = 13  # empty, 1-8, mine, covered, marked, wrong marked
CELL_SIZE = 15

COVER_FOR_CELL = 10
MARK_FOR_CELL = 10
EMPTY_CELL = 0  # uncovered
MINE_CELL = 9
COVERED_MINE_CELL = MINE_CELL + COVER_FOR_CELL  # 19
MARKED_MINE_CELL = COVERED_MINE_CELL + MARK_FOR_CELL  # 29

DRAW_MINE = 9
DRAW_COVER = 10
DRAW_MARK = 11
DRAW_WRONG_MARK = 12

N_MINES = 30
N_COLS = 20
N_ROWS = 10
N_CELLS = N_COLS * N_ROWS

BOARD_WIDTH = N_COLS * CELL_SIZE
BOARD_HEIGHT = N_ROWS * CELL_SIZE


class Board(Canvas):
    def __init__(self, app):
        super().__init__(app.root, width=BOARD_WIDTH, height=BOARD_HEIGHT,
                         highlightthickness=0)
        self.app = app
        self.images = []
        self.field = None
        self.covered = None
        self.marks_left = None
        self.playing = False

        self.load_images()
        self.new_game()
        self.bind('<Button>', self.mouse_pressed)

    def load_images(self):
        """loads images from the disk"""
        for i in range(N_IMAGES):
            self.images.append(PhotoImage(file=f"res/{i}.png"))

    def new_game(self):
        # create minefield as 2d array
        self.field = [[COVER_FOR_CELL] * N_COLS for _ in range(N_ROWS)]

        # set mines
        for pos in random.sample(range(N_CELLS), N_MINES):
            col = pos % N_COLS
            row = pos // N_COLS
            self.field[row][col] = COVERED_MINE_CELL
            self.walk_around(row, col, self.count_up)

        self.covered = N_CELLS - N_MINES
        self.marks_left = N_MINES
        self.set_status_msg()
        self.playing = True
        self.draw_board()

    def walk_around(self, row, col, consumer):
        """周囲8セルに対して、consumerの処理をする"""
        # left
        if col > 0:
            c = col - 1
            r = row - 1
            if r >= 0:
                consumer(r, c)

            consumer(row, c)

            r = row + 1
            if r < N_ROWS:
                consumer(r, c)

        # center
        r = row - 1
        if r >= 0:
            consumer(r, col)

        r = row + 1
        if r < N_ROWS:
            consumer(r, col)

        # right
        if col < (N_COLS - 1):
            c = col + 1
            r = row - 1
            if r >= 0:
                consumer(r, c)

            consumer(row, c)

            r = row + 1
            if r < N_ROWS:
                consumer(r, c)

    def count_up(self, r, c):
        if self.field[r][c] != COVERED_MINE_CELL:
            self.field[r][c] += 1

    def uncover(self, r, c):
        if MINE_CELL < self.field[r][c] <= COVERED_MINE_CELL:  # exclude marked
            self.field[r][c] -= COVER_FOR_CELL
            self.covered -= 1
            if self.field[r][c] == EMPTY_CELL:
                self.uncover_empty_cells(r, c)

    def uncover_empty_cells(self, r, c):
        self.walk_around(r, c, self.uncover)  # recursive

    def mouse_pressed(self, e):
        if not self.playing:
            self.new_game()
            return

        r = e.y // CELL_SIZE
        c = e.x // CELL_SIZE
        if e.num == 3:  # right click
            if self.field[r][c] > MINE_CELL:  # covered
                if self.field[r][c] <= COVERED_MINE_CELL:  # unmarked
                    if self.marks_left > 0:  # mark
                        self.field[r][c] += MARK_FOR_CELL
                        self.marks_left -= 1
                        self.set_status_msg()
                        self.judge_win()
                    else:  # do nothing
                        return
                else:  # marked then unmark
                    self.field[r][c] -= MARK_FOR_CELL
                    self.marks_left += 1
                    self.set_status_msg()
            else:  # uncovered then do nothing
                return
        else:  # left or middle click
            if self.field[r][c] > COVERED_MINE_CELL:  # marked
                return
            if self.field[r][c] == COVERED_MINE_CELL:  # covered mine
                do_draw = True
                self.playing = False
                self.set_status_msg("Game lost.")
            elif MINE_CELL < self.field[r][c] < COVERED_MINE_CELL:  # covered
                self.field[r][c] -= COVER_FOR_CELL
                self.covered -= 1
                if self.field[r][c] == EMPTY_CELL:
                    self.uncover_empty_cells(r, c)
                self.judge_win()
            else:  # uncovered then do nothing
                return

        self.draw_board()

    def set_status_msg(self, msg=None):
        msg = msg or f"{self.marks_left} marks left."
        self.app.status_bar.set(msg)

    def judge_win(self):
        if self.covered == 0 and self.marks_left == 0:
            self.playing = False
            self.set_status_msg("Game won!")

    def draw_board(self):
        self.delete(ALL)  # とりあえず全描画方式にしておく

        for r in range(N_ROWS):
            for c in range(N_COLS):
                cell = self.field[r][c]
                if self.playing:
                    if cell > COVERED_MINE_CELL:  # 20~28
                        cell = DRAW_MARK
                    elif cell > MINE_CELL:  # 10~18
                        cell = DRAW_COVER
                else:  # game over
                    if cell == MARKED_MINE_CELL:  # 29
                        cell = DRAW_MARK
                    elif cell == COVERED_MINE_CELL:  # 19
                        cell = DRAW_MINE
                    elif cell > COVERED_MINE_CELL:  # 20~28
                        cell = DRAW_WRONG_MARK
                    elif cell > MINE_CELL:  # 10~18
                        cell = DRAW_COVER

                self.create_image(c * CELL_SIZE, r * CELL_SIZE,
                                  image=self.images[cell], anchor=NW)


class Minesweeper:
    def __init__(self):
        self.root = Tk()
        self.root.title("Minesweeper")
        self.root.resizable(False, False)
        self.status_bar = StringVar()
        self.board = Board(self)
        self.board.pack()
        ttk.Label(self.root, textvariable=self.status_bar,
                  relief=SUNKEN, padding="2 1").pack(fill=X)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    minesweeper = Minesweeper()
    minesweeper.run()
