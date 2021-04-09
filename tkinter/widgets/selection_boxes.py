import calendar
from tkinter import *
from tkinter import ttk

root = Tk()

# Combobox(Entry)
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.config(values=[calendar.month_name[m] for m in range(1, 13)])
combobox.state(['readonly'])
combobox.bind("<<ComboboxSelected>>", lambda e: print(month.get()))
combobox.pack()
month.set('Not a month!')

# Spinbox(Entry)
year = StringVar()
ttk.Spinbox(root, from_=1900, to=2100, textvariable=year,
            command=lambda: print(year.get())).pack()

# OptionMenu(Menubutton)
option = StringVar()
options = ['none', 'bold', 'italic']
ttk.OptionMenu(root, option, options[0], *options,
               command=lambda: print(option.get())).pack()

root.mainloop()
