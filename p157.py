#colorchooser

from tkinter import Tk,Button,colorchooser

def result():
    a=colorchooser.askcolor()  #colorchooser provide facility to choose color and returns tuple of RGB & color-code of choosen color 
    print(a)
    win.configure(bg=f"{a[1]}")
    
win=Tk()                                
win.geometry("600x400")
win.configure(bg="yellow")

b1=Button(win,text="Chnage bg color",font=("arial",15,"bold"),bg="pink",bd=5,command=result)
b1.pack()

win.mainloop()
