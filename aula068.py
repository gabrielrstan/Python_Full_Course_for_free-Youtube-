from tkinter import *

window = Tk() #instanciando uma janela

photo = PhotoImage(file='aula68.png')

label = Label(window, 
              text="Bro, do you even code?", 
              font=('Ariel', 40, 'bold'), 
              fg='#00FF00', 
              bg='black', 
              relief=RAISED, 
              bd=10, 
              padx=20, 
              pady=20, 
              image=photo, 
              compound='bottom')
label.pack()
#label.place(x=0, y=0)

window.mainloop() #mostrando a janela