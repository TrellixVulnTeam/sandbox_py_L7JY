from tkinter import *
from tkinter import ttk

root = Tk()

# can be used as a Listbox
treeview = ttk.Treeview(root)
treeview.pack(fill=BOTH, expand=True)
treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')

logo = PhotoImage(file='python_logo.gif').subsample(10, 10)  # Change path as needed
treeview.insert('item2', 'end', 'python', text='Python', image=logo)

treeview.config(height=5)
treeview.move('item2', 'item1', 'end')
treeview.item('item1', open=True)
treeview.item('item2', open=True)
print(treeview.item('item1', 'open'))

treeview.detach('item3')  # only invisible, stay in memory yet
treeview.move('item3', 'item2', '0')
treeview.delete('item3')

treeview.configure(column='version')
treeview.column('version', width=50, anchor='center')
treeview.column('#0', width=150)
treeview.heading('version', text='Version')
treeview.set('python', 'version', '3.4')
treeview.item('python', tags=('software',))
treeview.tag_configure('software', background='yellow')

# virtual events
treeview.bind('<<TreeviewSelect>>', lambda e: print(treeview.selection()))
treeview.bind('<<TreeviewOpen>>', lambda e: print('Open'))
treeview.bind('<<TreeviewClose>>', lambda e: print('Close'))

# "extended" (default: multiple items), "browse" (single item), "none"
treeview.config(selectmode='browse')
print(treeview.selection_add('python'))
print(treeview.selection_remove('python'))
print(treeview.selection_toggle('python'))

root.mainloop()
