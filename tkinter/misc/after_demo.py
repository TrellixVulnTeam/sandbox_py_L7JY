# after()による定期実行
# イベントループのタスクとして実行されるため（完全なノンブロッキングではない）、重い処理を行わないこと！
from tkinter import *

task_id = None


def task():
    global task_id
    print("Hello: {}".format(task_id))
    # root.after(5000)  # sleep in mainloop, dangerous!
    task_id = root.after(1000, task)  # reschedule


def cancel_task():
    root.after_cancel(task_id)
    print("Canceled: {}".format(task_id))


root = Tk()

Button(root, text="Push me!", command=cancel_task).pack()

task()

root.mainloop()
