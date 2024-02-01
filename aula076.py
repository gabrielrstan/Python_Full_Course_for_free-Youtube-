from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor()
    color_hex = color[1]
    window.config(bg=color_hex) #change background color
    #window.config(bg=colorchooser.askcolor()[1]) #just one line of code


window = Tk()
window.geometry("420x420")
button  = Button(text="click me", command=click)
button.pack()
window.mainloop()