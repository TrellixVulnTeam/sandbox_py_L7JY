from tkinter import *
from tkinter import ttk

root = Tk()

style = ttk.Style()
style.configure('TFrame', background='pink')

frame = ttk.Frame(root)
frame.config(height=50, width=200)
frame.config(relief=FLAT)  # default
# frame.config(padding=(30, 15))  # horizontal vertical
# frame.config(padding=(30, 15, 30))  # left vertical right
frame.config(padding='5 5 15 15')  # left top right bottom
frame.pack(fill=BOTH, padx=5, pady=5)

# relieves
ttk.Frame(root, height=50, width=200, relief=RAISED).pack(fill=BOTH, padx=5, pady=5)
ttk.Frame(root, height=50, width=200, relief=SUNKEN).pack(fill=BOTH, padx=5, pady=5)
ttk.Frame(root, height=50, width=200, relief=SOLID).pack(fill=BOTH, padx=5, pady=5)
ttk.Frame(root, height=50, width=200, relief=RIDGE).pack(fill=BOTH, padx=5, pady=5)
ttk.Frame(root, height=50, width=200, relief=GROOVE).pack(fill=BOTH, padx=5, pady=5)

l_frame = ttk.LabelFrame(root, height=100, width=200, text='My Frame')
l_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

# notebook
notebook = ttk.Notebook(l_frame)
notebook.pack(fill=BOTH, expand=True)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='い')
notebook.add(frame2, text='ろ')
ttk.Button(frame1, text='Click Me').pack()

frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='は')
notebook.forget(1)
notebook.add(frame3, text='は')

print(notebook.select())
notebook.select(2)
print(notebook.index(notebook.select()))

notebook.tab(1, state='disabled')
notebook.tab(1, state='hidden')
notebook.tab(1, state='normal')
print(notebook.tab(1, 'text'))
print(notebook.tab(1))

root.mainloop()
