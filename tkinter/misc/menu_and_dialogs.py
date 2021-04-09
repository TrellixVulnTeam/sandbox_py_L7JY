from tkinter import *
from tkinter import messagebox, colorchooser, filedialog


def open_file():
    filename = filedialog.askopenfile(filetypes=[('Python files', '*.py'), ('All files', '*')])
    print(filename.name if filename else 'Nothing')


def open_dir():
    dirname = filedialog.askdirectory()
    print(dirname if dirname else 'Nothing')


def save_as_file():
    # 上書き注意
    filename = filedialog.asksaveasfile()
    print(filename.name if filename else 'Nothing')


root = Tk()
root.option_add('*tearOff', False)  # menuの切り離しを無効にする

menubar = Menu(root)
root.config(menu=menubar)
file = Menu(menubar)
radio = Menu(menubar)
check = Menu(menubar)
help_ = Menu(menubar)

menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=radio, label='Radio')
menubar.add_cascade(menu=check, label='Check')
menubar.add_cascade(menu=help_, label='Help')

file.add_command(label='New', command=lambda: print('New File'))
file.add_separator()
file.add_command(label='Open File...', command=open_file)
file.add_command(label='Open Directory...', command=open_dir)
file.add_command(label='Save As...', command=save_as_file)
file.add_separator()
file.add_command(label="Exit", command=lambda: root.quit())

file.entryconfig('New', accelerator='Ctrl+N')  # display only
file.entryconfig('New', state='disabled')

choice = IntVar()
radio.add_radiobutton(label='One', variable=choice, value=1)
radio.add_radiobutton(label='Two', variable=choice, value=2)
radio.add_radiobutton(label='Three', variable=choice, value=3)

check.add_checkbutton(label='One')
check.add_checkbutton(label='Two')


def info():
    print(messagebox.showinfo(title="Info", message='Info message'))


def warning():
    print(messagebox.showwarning("Warning", "Warning message"))


def error():
    print(messagebox.showerror("Error", "Error message"))


def yesno():
    print(messagebox.askyesno(title='Hungry?', message='Do you want SPAM?'))


def choose_color():
    color = colorchooser.askcolor(initialcolor="#FFFFFF")
    root.config(bg=color[1])
    print(color)


help_.add_command(label='Info', command=info)
help_.add_command(label='Warning', command=warning)
help_.add_command(label='Error', command=error)
help_.add_command(label='Yes/No', command=yesno)
help_.add_separator()
help_.add_command(label='Choose Color', command=choose_color)
help_.add_separator()
help_.add_command(label='Beep', command=root.bell)
help_.add_separator()
help_.add_command(label='Compound')
help_.add_separator()
help_.add_command(label='Other')

logo = PhotoImage(file='../widgets/python_logo.gif').subsample(10, 10)  # Change path as needed
help_.entryconfig('Compound', image=logo, compound='left')
help_.entryconfig('Info', accelerator='Ctrl+A')

help_.delete('Other')
other = Menu(help_)
help_.add_cascade(menu=other, label='Other')
other.add_command(label='Hoge', command=lambda: print('Hoge!'))
other.add_command(label='Fuga', command=lambda: print('Fuga!'))

# popup
pop_menu = Menu(root)
pop_menu.add_command(label='One')
pop_menu.add_command(label='Two')
pop_menu.add_command(label='Three')


def popup(event):
    pop_menu.post(event.x_root, event.y_root)  # absolute screen position


root.bind('<Button-3>', popup)

root.mainloop()
