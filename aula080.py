from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(initialdir="/home/stanzione/Aulas/Python Full Course for free (Youtube)/pasta2", 
                                          title="Open file okay?", 
                                          filetypes=(("text files", "*.txt"),
                                          ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

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

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

window = Tk()

open_image = PhotoImage(file="aula080b_20.png")
save_image = PhotoImage(file="aula080a_20.png")
close_image = PhotoImage(file="aula080c_20.png")

menubar = Menu(window)
window.config(menu=menubar)

file_Menu = Menu(menubar, tearoff=0, font=("urw palladio l", 15))
menubar.add_cascade(label="File", menu=file_Menu)
file_Menu.add_command(label='Open', command=open_file, image=open_image, compound=LEFT)
file_Menu.add_command(label='Save', command=save_file, image=save_image, compound=LEFT)
file_Menu.add_separator()
file_Menu.add_command(label='Exit', command=quit, image=close_image, compound=LEFT)

edit_Menu = Menu(menubar, tearoff=0, font=("urw palladio l", 15))
menubar.add_cascade(label="Edit", menu=edit_Menu)
edit_Menu.add_command(label='Cut', command=cut)
edit_Menu.add_command(label='Copy', command=copy)
edit_Menu.add_command(label='Paste', command=paste)

text = Text(window)
text.pack()

window.mainloop()