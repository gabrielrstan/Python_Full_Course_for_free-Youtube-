from tkinter import *

def doSomething(event):
    #print("You pressed {}".format(event.keysym))
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomething)
label = Label(window, font=('courier 10 pitch', 100))
label.pack()

window.mainloop()