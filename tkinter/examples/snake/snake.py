"""
This is a simple Snake game clone.
"""
import sys
import random
from tkinter import Tk, PhotoImage, Canvas, ALL, NW, Button

BOARD_WIDTH, BOARD_HEIGHT = 300, 300
CENTER_X, CENTER_Y = BOARD_WIDTH // 2, BOARD_HEIGHT // 2
DELAY = 100
DOT_SIZE = 10
MAX_RAND_POS = 28


class Board(Canvas):

    def __init__(self, master):
        super().__init__(master, width=BOARD_WIDTH, height=BOARD_HEIGHT,
                         background="black", highlightthickness=0)
        self.load_images()
        self.init_game()

    def load_images(self):
        """loads images from the disk"""
        self.dot_img = PhotoImage(file="dot.png")  # require Tcl/Tk8.6
        self.head_img = PhotoImage(file="head.png")
        self.apple_img = PhotoImage(file="apple.png")

    def init_game(self):
        """initializes game"""

        self.delete(ALL)

        self.playing = True
        self.score = 0

        # initial direction (Left)
        self.dx, self.dy = DOT_SIZE, 0

        # apple coordinates
        self.apple_x, self.apple_y = 0, 0

        self.create_objects()
        self.locate_apple()

        self.bind_all("<Key>", self.on_key_pressed)

        self.on_timer()  # start

    def locate_apple(self):
        """places the apple object on Canvas"""
        self.apple_x = random.randint(1, MAX_RAND_POS) * DOT_SIZE
        self.apple_y = random.randint(1, MAX_RAND_POS) * DOT_SIZE
        self.moveto(self.apple, self.apple_x, self.apple_y)

    def create_objects(self):
        """creates objects on Canvas"""
        self.score_txt = self.create_text(
            30, 10, text=f"Score: {self.score}", fill="white")
        self.apple = self.create_image(
            self.apple_x, self.apple_y, image=self.apple_img, anchor=NW)
        self.snake = [
            self.create_image(50, 50, image=self.head_img, anchor=NW),  # head
            self.create_image(40, 50, image=self.dot_img, anchor=NW),  # dot
            self.create_image(30, 50, image=self.dot_img, anchor=NW),
        ]

    def check_apple_collision(self):
        """checks if the head of snake collides with apple"""
        x1, y1, x2, y2 = self.bbox(self.snake[0])
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for ovr in overlap:
            if self.apple == ovr:
                self.score += 1
                x, y = self.coords(self.apple)
                self.snake.append(self.create_image(x, y, image=self.dot_img, anchor=NW))
                self.locate_apple()

    def move_snake(self):
        """moves the Snake object"""
        z = len(self.snake) - 1
        while z > 0:
            c = self.coords(self.snake[z - 1])
            self.moveto(self.snake[z], c[0], c[1])
            z -= 1

        self.move(self.snake[0], self.dx, self.dy)

    def check_collisions(self):
        """checks for collisions"""
        x1, y1, x2, y2 = self.bbox(self.snake[0])
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for dot in self.snake[1:]:
            for over in overlap:
                if over == dot:
                    self.playing = False

        if x1 < 0 or x1 > BOARD_WIDTH - DOT_SIZE or \
                y1 < 0 or y1 > BOARD_HEIGHT - DOT_SIZE:
            self.playing = False

    def draw_score(self):
        """draws score"""
        self.itemconfigure(self.score_txt, text=f"Score: {self.score}")

    def game_over(self):
        """deletes all objects and draws game over message"""
        self.delete(ALL)
        self.create_text(CENTER_X, CENTER_Y - 30,
                         text=f"Game Over with score {self.score}",
                         fill="white")
        button = Button(self, text="Restart", padx=10, pady=2, command=self.init_game)
        self.create_window(CENTER_X, CENTER_Y + 10, window=button)
        button.focus()

    def on_key_pressed(self, e):
        """controls direction variables with cursor keys"""
        key = e.keysym
        if key == "Left" and self.dx <= 0:
            self.dx = -DOT_SIZE
            self.dy = 0
        elif key == "Right" and self.dx >= 0:
            self.dx = DOT_SIZE
            self.dy = 0
        elif key == "Up" and self.dy <= 0:
            self.dx = 0
            self.dy = -DOT_SIZE
        elif key == "Down" and self.dy >= 0:
            self.dx = 0
            self.dy = DOT_SIZE

    def on_timer(self):
        """creates a game cycle each timer event"""
        self.check_collisions()
        if self.playing:
            self.check_apple_collision()
            self.move_snake()
            self.draw_score()
            self.after(DELAY, self.on_timer)
        else:
            self.game_over()


class Snake(Tk):
    def __init__(self):
        super().__init__()
        self.title("Snake")
        self.resizable(False, False)
        self.board = Board(self)
        self.board.pack()


if __name__ == '__main__':
    snake = Snake()
    snake.mainloop()
