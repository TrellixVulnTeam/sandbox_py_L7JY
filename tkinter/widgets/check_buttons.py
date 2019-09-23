from tkinter import *
from tkinter import ttk

root = Tk()

checked = IntVar()

checkbutton = ttk.Checkbutton(root, text='Normal Checkbutton',
                              command=lambda: print(checked.get()))
print(checkbutton.instate(['alternate']))  # indeterminate: 未選択状態

checkbutton.config(variable=checked)
print(checkbutton.instate(['alternate']))

checkbutton.pack()

checkbutton.invoke()  # click

# String variable and value
spam = StringVar()
spam.set('Select SPAM')

check_spam = ttk.Checkbutton(root, variable=spam, textvariable=spam,
                             onvalue='SPAM Please!', offvalue='Boo SPAM!',
                             command=lambda: print(spam.get()))
check_spam.pack()

root.mainloop()
