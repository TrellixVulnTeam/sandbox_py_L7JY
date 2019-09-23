from tkinter import *


def main():
    root = Tk()
    root.geometry("330x220+100+100")
    root.title("Shapes")

    canvas = Canvas(root, bg='white')
    canvas.create_oval(10, 10, 80, 80, outline="#f11", fill="#1f1", width=2)
    canvas.create_oval(100, 10, 200, 80, outline="#f11", fill="#1f1", width=2)
    canvas.create_rectangle(220, 10, 280, 80, outline="#f11",
                            fill="#1f1", width=2)
    canvas.create_arc(30, 200, 90, 100, start=0,
                      extent=210, outline="#f11", fill="#1f1", width=2)
    points = [150, 100, 200, 120, 240, 180, 210, 200, 150, 150, 100, 200]
    canvas.create_polygon(points, outline='#f11', fill='#1f1', width=2)

    canvas.pack(fill=BOTH, expand=True)
    root.mainloop()


if __name__ == '__main__':
    main()
