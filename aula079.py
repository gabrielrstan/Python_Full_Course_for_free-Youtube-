from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir="/home/stanzione/Aulas/Python Full Course for free (Youtube)/pasta2",
                                    defaultextension='.txt', 
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    #filetext = input("Enter some text I guess   ")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text="save", command=save_file)
button.pack()
text = Text(window, font=("century schoolbook l", 20))
text.pack()
window.mainloop()
