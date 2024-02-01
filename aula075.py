from tkinter import * 
from tkinter import messagebox 

def click():
 #   messagebox.showinfo(title="This is a info message box", message="You are a person")
 #   messagebox.showwarning(title="WARNING!  ", message="You have a VIRUS!!!")
 #   messagebox.showerror(title="ERROR!  ", message="Someting went wrong :(")
    
    '''if messagebox.askokcancel(title='Ask ok cancel', message="Do you want to do the thing?"):
        print("Tou did the thing")
    else:
        print("You canceled a thing")'''
    
    '''if messagebox.askretrycancel(title='Ask retry cancel', message="Do you want retry the thing?"):
        print("Tou retried the thing")
    else:
        print("You canceled a thing")'''
    
    '''if messagebox.askyesno(title='Ask yes or no', message="Do you like cake?"):
        print("I like cake too")
    else:
        print("Why do you not like cake?")'''
    
    '''answer = print(messagebox.askquestion(title="ask question", message="Do you like píe?"))
    if answer == "yes":
        print("I like pie too")
    else:
        print("Why do you not like pie?")'''
    
    answer = messagebox.askyesnocancel(title="Yes no cancel", message='Do you like to code?', icon='info')
    if answer == True:
        print("You like to code :)")

    elif answer == False:
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question")
window = Tk()

button = Button(window, command=click, text="click me")
button.pack()
window.mainloop()