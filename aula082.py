from tkinter import *

def create_windon():
    #new_window = Toplevel() #Toplevel() = new window 'on top' of other windows, linked to a 'botton' window
    new_window = Tk() #TK() = new independent window
    old_window.destroy() #close out of old window

old_window = Tk()

Button(old_window, text="Create a new window", command=create_windon).pack()

old_window.mainloop()