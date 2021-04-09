# valid percent substitutions (from the Tk entry man page)
# note: you only have to register the ones you need; this
# example registers them all for illustrative purposes
#
# %d = the type of action (1=insert, 0=delete, -1 for others)
# %i = index of char string to be inserted/deleted, or -1
# %P = value of the entry if the edit is allowed
# %s = value of entry prior to editing
# %S = the text string being inserted or deleted, if any
# %v = the type of validation that is currently set
# %V = the type of validation that triggered the callback
#      (key, focusin, focusout, forced)
# %W = the tk name of the widget

from tkinter import *
from tkinter import ttk


def on_validate(d, i, P, s, S, v, V, W):
    text.delete("1.0", END)
    text.insert(END, "on_validate:\n")
    text.insert(END, "d='%s'\n" % d)
    text.insert(END, "i='%s'\n" % i)
    text.insert(END, "P='%s'\n" % P)
    text.insert(END, "s='%s'\n" % s)
    text.insert(END, "S='%s'\n" % S)
    text.insert(END, "v='%s'\n" % v)
    text.insert(END, "V='%s'\n" % V)
    text.insert(END, "W='%s'\n" % W)

    # Disallow anything but lowercase letters
    return S == S.lower()


def on_invalid():
    root.bell()
    print('Invalid')


root = Tk()

vcmd = (root.register(on_validate),
        '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
entry = ttk.Entry(root, validate="all", validatecommand=vcmd,
                  invalidcommand=on_invalid)
text = Text(root, height=10, width=40)
entry.pack(side=TOP, fill=X)
text.pack(side=BOTTOM, fill=BOTH, expand=True)

root.mainloop()
