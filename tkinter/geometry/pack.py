from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text='Hello, Tkinter!', background='yellow').pack(
    side=RIGHT, anchor=NW)
ttk.Label(root, text='Hello, Tkinter!', background='blue').pack(
    side=LEFT, padx=10, pady=10)
label = ttk.Label(root, text='Hello, Tkinter!', background='green', anchor=SE)
label.pack(ipadx=20, ipady=20)
print(label)

# 一括設定変更
for widget in root.pack_slaves():
    # widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info())

# label.pack_forget()

root.pack_propagate(False)  # childrenのサイズ変更を反映しない

root.mainloop()
