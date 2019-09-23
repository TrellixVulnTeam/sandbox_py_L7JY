import turtle

painter = turtle.Turtle()
painter.speed(0)


def fractal(size, depth=0):
    if depth <= 0:
        painter.forward(size)  # 直線
    else:
        fractal(size / 3, depth - 1)
        painter.left(60)  # 1/3の長さでフラクタル描画、左に60度向く

        fractal(size / 3, depth - 1)
        painter.left(-120)  # 1/3の長さでフラクタル描画、右に120度向く

        fractal(size / 3, depth - 1)
        painter.left(60)  # 1/3の長さでフラクタル描画、左に60度向く

        fractal(size / 3, depth - 1)  # 1/3の長さでフラクタル描画


# fractal(200)
# painter.reset()
# fractal(200, 1)
# painter.reset()
# fractal(200, 2)
# painter.reset()
# fractal(200, 3)

painter.goto(-150, -150)
painter.clear()
for _ in range(5):
    fractal(200, 3)
    painter.left(360 / 5)

turtle.done()
