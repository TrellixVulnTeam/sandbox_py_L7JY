from tkinter import *


def key_press(event):
    print('event: {}'.format(event))


root = Tk()

root.bind('<KeyPress-Insert>', key_press)
root.bind('<Key-Delete>', key_press)

# mouse buttons not num keys
root.bind('<1>', key_press)
root.bind('<2>', key_press)
root.bind('<3>', key_press)
root.bind('<4>', key_press)
root.bind('<5>', key_press)

# num keys
root.bind('<Key-1>', key_press)
root.bind('<Key-2>', key_press)
root.bind('<Key-3>', key_press)
root.bind('<Key-4>', key_press)
root.bind('<Key-5>', key_press)
root.bind('<6>', key_press)
root.bind('<7>', key_press)
root.bind('<8>', key_press)
root.bind('<9>', key_press)
root.bind('<0>', key_press)

root.bind('<a>', key_press)
root.bind('<A>', key_press)
root.bind('<space>', key_press)
root.bind('<\'>', key_press)
root.bind('<">', key_press)
root.bind('<\>', key_press)
root.bind('<less>', key_press)
root.bind('<greater>', key_press)

# special
root.bind('<F1>', key_press)
root.bind('<F12>', key_press)
root.bind('<Right>', key_press)
root.bind('<Left>', key_press)
root.bind('<Up>', key_press)
root.bind('<Down>', key_press)
root.bind('<Alt_L>', key_press)  # _L: left
root.bind('<Shift_R>', key_press)  # _R: right
root.bind('<Win_R>', key_press)
root.bind('<App>', key_press)
root.bind('<Return>', key_press)
root.bind('<Prior>', key_press)  # PageUp
root.bind('<Next>', key_press)  # PageDown

# combo
root.bind('<Control-c>', key_press)
root.bind('<Control-C>', key_press)  # eventとしては別扱い
root.bind('<Control-v>', key_press)
root.bind('<Control-V>', key_press)
root.bind('<Shift-x>', key_press)  # no event
root.bind('<Shift-X>', key_press)
root.bind('<Control-Alt-q>', key_press)
root.bind('<Control-Alt-Shift-Y>', key_press)

root.mainloop()
