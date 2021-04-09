from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text='Yellow', background='Yellow').grid(
    row=0, column=2, rowspan=2, sticky=NSEW)
ttk.Label(root, text='Blue', background='Blue').grid(
    row=1, column=0, columnspan=2, sticky=NSEW)
ttk.Label(root, text='Green', background='Green').grid(
    row=0, column=0, padx=10, pady=10, sticky=NSEW)
ttk.Label(root, text='Orange', background='Orange').grid(
    row=0, column=1, ipadx=10, ipady=10)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.columnconfigure(2, weight=1)

# 一括設定変更
for widget in root.grid_slaves():
    # widget.grid_configure(sticky=NSEW)
    print(widget.grid_info())

root.grid_propagate(False)  # childrenのサイズの影響を受けない

root.mainloop()
