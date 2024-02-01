from tkinter import *

window = Tk() #instanciando uma janela
window.geometry("420x420")
window.title("Primeiro programa GUI ")
icon = PhotoImage(file="aula067.png")
window.iconphoto(True, icon)
#window.config(background="black")
window.config(background="#5cfcff")

window.mainloop() #mostrando a janela
