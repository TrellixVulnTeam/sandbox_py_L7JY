from tkinter import *
from tkinter import ttk

root = Tk()

label1 = ttk.Label(root, text='Label 1', relief=SOLID, padding='10 5')
label2 = ttk.Label(root, text='Label 2', relief=SOLID, padding='10 5')
label1.pack(pady=(10, 5))
label2.pack(pady=(5, 10))

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label 1'))
label1.bind('<1>', lambda e: print('<1> Label 1'))

root.bind('<1>', lambda e: print('<1> Root'))

# label1.unbind('<1>')
# label1.unbind('<ButtonPress>')

root.bind_all('<Escape>', lambda e: print('Escape!'))

root.mainloop()
