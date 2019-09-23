from tkinter import *
from tkinter import ttk

root = Tk()

entry_value = StringVar()
entry_value.trace_add(['write', 'read', 'unset'], lambda *args: print(args))

entry = ttk.Entry(root, textvariable=entry_value)
entry.pack(fill=X, expand=True, padx=5, pady=5)

pg_value = DoubleVar()
pg_value.trace_add(['write', 'read', 'unset'], lambda *args: print(args))

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200,
                              maximum=10.0, variable=pg_value)
progressbar.pack(fill=X, expand=True, padx=5, pady=5)
scale = ttk.Scale(root, orient=HORIZONTAL,
                  length=200, variable=pg_value,
                  from_=0, to=10.0)
scale.pack(fill=X, expand=True, padx=5, pady=5)

set_btn = ttk.Button(root, text="Set", command=lambda: pg_value.set(5.0))
set_btn.pack(side=LEFT, padx=5, pady=5)
get_btn = ttk.Button(root, text="Get",
                     command=lambda: print(entry_value.get(), pg_value.get()))
get_btn.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
