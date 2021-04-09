from tkinter import *

WIDTH, HEIGHT = 800, 500
SIZE = 50


class Ball:
    def __init__(self, tag):
        self.shape = canvas.create_oval(
            0, 0, SIZE, SIZE, fill="black", tags=tag)
        self.dx = 10
        self.dy = 10

    def ball_update(self):
        canvas.move(self.shape, self.dx, self.dy)
        left, top, right, bottom = canvas.coords(self.shape)
        if left <= 0 or right >= WIDTH:
            self.dx *= -1
        if top <= 0 or bottom >= HEIGHT:
            self.dy *= -1


# Double buffering
def cycle():
    global switcher
    canvas.tag_raise("bg")
    if switcher:
        ball2.ball_update()
        canvas.tag_raise("ball")
    else:
        ball.ball_update()
        canvas.tag_raise("ball2")
    root.update_idletasks()
    switcher = not switcher
    root.after(10, cycle)


switcher = True

root = Tk()
root.resizable(False, False)
canvas = Canvas(root, width=WIDTH, height=HEIGHT,
                bg="blue", bd=0, highlightthickness=0)
canvas.pack()

bg = canvas.create_rectangle(-1, -1, WIDTH, HEIGHT,
                             fill="lightgray", tags="bg")
ball = Ball("ball")
ball.ball_update()
ball2 = Ball("ball2")

cycle()
root.mainloop()
