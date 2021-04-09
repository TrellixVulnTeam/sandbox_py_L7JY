from tkinter import *
from tkinter import ttk

root = Tk()

# variables must be declared after root window (or Misc object) created
entry_var = StringVar()
entry_var.trace_add(['write', 'read', 'unset'], lambda *args: print(args))
ttk.Entry(root, textvariable=entry_var)\
    .pack(fill=X, expand=True, padx=5, pady=5)

pg_value = DoubleVar()
pg_value.trace_add(['write', 'read', 'unset'], lambda *args: print(args))
ttk.Label(root, textvariable=pg_value).pack(padx=5, pady=5)
ttk.Progressbar(root, orient=HORIZONTAL, length=200,
                maximum=10.0, variable=pg_value)\
    .pack(fill=X, expand=True, padx=5, pady=5)
ttk.Scale(root, orient=HORIZONTAL,
          length=200, variable=pg_value,
          from_=0, to=10.0)\
    .pack(fill=X, expand=True, padx=5, pady=5)

ttk.Button(root, text="Set", command=lambda: pg_value.set(5.0))\
    .pack(side=LEFT, padx=5, pady=5)
ttk.Button(root, text="Get",
           command=lambda: print(entry_var.get(), pg_value.get()))\
    .pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
