from tkinter import *

root = Tk()

for i in range(5):
    Button(root, text=i, command=lambda: print(i)).pack()

Label(root).pack()

# capture the value into the closure
for j in range(5):
    Button(root, text=j, command=lambda x=j: print(x)).pack()

root.mainloop()
