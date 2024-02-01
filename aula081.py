from tkinter import *


window = Tk()

frame = Frame(window, bg='pink', bd=5, relief=SUNKEN)
#frame.pack(side=BOTTOM)
frame.place(x=100, y=100)

Button(frame, text="W", font=("helvetica", 25), width=3).pack(side=TOP)
Button(frame, text="A", font=("helvetica", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("helvetica", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("helvetica", 25), width=3).pack(side=LEFT)

window.mainloop()