from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str(int((download/GB)*100))+ "%")
        text.set("{} / {} GB completed".format(download, GB)) 
        window.update_idletasks()

window = Tk()
text = StringVar()

percent = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
textLabel = Label(window, textvariable=text).pack()

button = Button(window, text='download', command=start).pack()


window.mainloop()