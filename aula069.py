from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk() #instanciando uma janela
#window.geometry("360x240")

photo = PhotoImage(file="aula069.png")

button = Button(window, 
                text="Click me!", 
                command=click, 
                font=("Comic Sans", 30), 
                fg="#00FF00", 
                bg='black', 
                activeforeground="#00FF00", 
                activebackground='black',
                state=ACTIVE, 
                image=photo, 
                compound="bottom")
button.pack()




window.mainloop() #mostrando a janela