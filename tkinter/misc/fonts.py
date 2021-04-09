from tkinter import font, Tk
from tkinter.ttk import Label

root = Tk()
root.geometry("+300+200")
root.title("Fonts")

txt = "Today is a beautiful day"
Label(root, text=txt).pack()
Label(root, text=txt, font="TkDefaultFont").pack()
Label(root, text=txt, font="TkTextFont").pack()
Label(root, text=txt, font="TkFixedFont").pack()
Label(root, text=txt, font="TkMenuFont").pack()
Label(root, text=txt, font="TkHeadingFont").pack()
Label(root, text=txt, font="TkCaptionFont").pack()
Label(root, text=txt, font="TkSmallCaptionFont").pack()
Label(root, text=txt, font="TkIconFont").pack()
Label(root, text=txt, font="TkTooltipFont").pack()
Label(root, text=txt, font="Helvetica 20 bold").pack()
Label(root, text=txt, font=("Times", "20", "bold", "italic",)).pack()
mono = font.Font(family="Monospace", size=20, weight="bold", name="myMono")
Label(root, text=txt, font=mono).pack()
print(mono, mono.measure(txt))
print()

for name in ["TkDefaultFont", "TkFixedFont"]:
    f = font.nametofont(name)
    print(f.actual())
    print(f.metrics())

print()
print(font.families())

root.mainloop()
