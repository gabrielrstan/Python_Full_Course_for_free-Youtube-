from tkinter import * 

def submit():
    print("The temperature is {} degrees C".format(scale.get()))

window = Tk()

hot_image = PhotoImage(file='aula073a.png')
hot_label = Label(image=hot_image)
hot_label.pack()

scale = Scale(window,
               from_=100,
                 to= 0, 
                 length=400, 
                 orient=VERTICAL, #orientation od scale
                 font=("Consolas", 20),
                 tickinterval=10, #adds numeric indicators for value
                 #showvalue=0, #hide current value
                 resolution=5, #increment of slider
                 troughcolor='#69EAFF', 
                 fg='#FF1C00', 
                 bg='#111111'
                 )
scale.set(((scale['from'] - scale['to'])/2)+ scale['to']) # set current valeu of slider
scale.pack()

cold_image = PhotoImage(file='aula073b.png')
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()