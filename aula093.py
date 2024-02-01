from tkinter import *
import time

def update():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = time.strftime("%A")
    day_label.config(text=day_string)

    date_string = time.strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)
window = Tk()

time_label = Label(window, font=('nimbus sans l', 50), bg='black', fg='#00FF00')
time_label.pack()

day_label = Label(window, font=('clean', 25))
day_label.pack()

date_label = Label(window, font=('clean', 30))
date_label.pack()

update()

window.mainloop()