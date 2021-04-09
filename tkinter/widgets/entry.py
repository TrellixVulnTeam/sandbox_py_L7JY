from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)  # number of characters
entry.pack()

# virtual events
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))
entry.bind('<<Cut>>', lambda e: print('Cut'))

# enter key
entry.bind('<Return>', lambda e: print(entry.get()))

entry.delete(0, 1)  # slice like
entry.delete(0, END)
entry.insert(0, 'Enter your password')
print(entry.get())

# entry.config(show='*')
# entry.state(['readonly'])
# entry.state(['disabled'])
# entry.state(['!disabled'])

root.mainloop()
