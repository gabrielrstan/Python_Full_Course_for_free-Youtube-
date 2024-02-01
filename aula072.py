from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered a hotdog")
    else:
        print("Huh?")

window = Tk()

pizza_image = PhotoImage(file='aula072a.png')
hamburger_image = PhotoImage(file='aula072b.png')
hotdog_image = PhotoImage(file='aula072c.png')
food_images = [pizza_image, hamburger_image, hotdog_image]


x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window, 
                               text=food[index], #add text to radiobuttons
                               variable=x, #groups radiobuttons together if they share the same variable
                               value=index, #assigns each radiobutton a different value
                               padx=25, #adds padding on x-axis
                               font=("Impact", 50), 
                               image=food_images[index], #adds image to radiobutton
                               compound='left', #adds image & text (left-side)
                               indicatoron=0, #eliminate circle indicators
                               width=550, #sets width of radiobuttons
                               command=order #set command of radiobutton to function
                               )
    radio_button.pack(anchor=W) 

window.mainloop()