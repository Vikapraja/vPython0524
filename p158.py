#colorchooser

from tkinter import Tk,Button,Label,Entry

def upperc():
    a=e1.get()
    b=a.upper()
    e1.delete(0,"end")
    e1.insert(0,b)

def lowerc():
    a=e1.get()
    b=a.lower()
    e1.delete(0,"end")
    e1.insert(0,b)
    
win=Tk()                                
win.geometry("600x400")
win.configure(bg="yellow")


lb1=Label(win,text="Text",font=("arial",20,"bold"),bg="yellow",bd=5)
lb1.place(x=80,y=100)

e1=Entry(win,font=("aria",15),bd=5)
e1.place(x=350,y=100)

b1=Button(win,text="Upper",font=("arial",15,"bold"),bd=5,command=upperc)
b1.place(x=350,y=200)

b1=Button(win,text="lower",font=("arial",15,"bold"),bd=5,command=lowerc)
b1.place(x=450,y=200)

win.mainloop()
