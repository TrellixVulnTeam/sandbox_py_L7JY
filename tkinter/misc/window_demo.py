from tkinter import *
from tkinter import ttk, messagebox

root = Tk()  # root window
root.geometry('320x240-300+200')
root.resizable(False, False)
root.iconbitmap('tie.ico')
print(root.geometry())
print(root.winfo_rootx(), root.winfo_rooty())
print(root.winfo_x(), root.winfo_y())
print(root.winfo_screenwidth(), root.winfo_screenheight())


def on_closing():
    if messagebox.askokcancel("Close", "Do you want to close?"):
        window.destroy()


# child window
window = Toplevel(root)
window.title('New Window')
window.protocol("WM_DELETE_WINDOW", on_closing)  # close window hook

# center in screen
w, h = 320, 240
left = (root.winfo_screenwidth() - w) // 2
top = (root.winfo_screenheight() - h) // 2
window.geometry(f'{w}x{h}+{left}+{top}')
print(window.geometry())
window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True, True)

print(window.state())


def set_window_status(status):
    window.state(status)
    print(window.state())


ttk.Button(root, text='normal', command=lambda: set_window_status(NORMAL)).pack()
ttk.Button(root, text='zoomed', command=lambda: set_window_status('zoomed')).pack()
ttk.Button(root, text='iconic', command=lambda: set_window_status('iconic')).pack()
ttk.Button(root, text='withdrawn', command=lambda: set_window_status('withdrawn')).pack()

ttk.Button(root, text='iconify', command=lambda: window.iconify()).pack()
ttk.Button(root, text='deiconify', command=lambda: window.deiconify()).pack()
ttk.Button(root, text='lower', command=lambda: window.lower()).pack()
ttk.Button(root, text='lift(root)', command=lambda: window.lift()).pack()

ttk.Button(root, text='destroy', command=lambda: window.destroy()).pack()

root.mainloop()
