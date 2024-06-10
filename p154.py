#action on button click
from tkinter import Tk,Button,Label,Entry,messagebox

def add():
    a=e1.get()      #to get data from entry
    b=e2.get()
    c=int(a)
    d=int(b)
    res=c+d
    print(res)
    lb3=Label(win,text=f"result={res}",font=("arial",20,"bold"),bg="pink",bd=5)
    lb3.place(x=250,y=30)
    messagebox.showinfo("Rresult",f"add={res}")

def mul():
    a=e1.get()      #to get data from entry
    b=e2.get()
    c=int(a)
    d=int(b)
    res=c*d
    print(res)
    lb3=Label(win,text=f"result={res}",font=("arial",20,"bold"),bg="green",bd=5)
    lb3.place(x=250,y=30)
    messagebox.showwarning("Rresult",f"Multiplication={res}")
    

win=Tk()                                
win.geometry("600x400")
win.configure(bg="yellow")

lb1=Label(win,text="Enter 1st Number",font=("arial",20,"bold"),bg="yellow",bd=5)
lb1.place(x=80,y=100)

e1=Entry(win,font=("aria",15),bd=5)
e1.place(x=350,y=100)

lb2=Label(win,text="Enter 2nd Number",font=("arial",20,"bold"),bg="yellow",bd=5)
lb2.place(x=80,y=200)

e2=Entry(win,font=("aria",15),bd=5)
e2.place(x=350,y=200)

b1=Button(win,text="Add",font=("arial",15,"bold"),bg="pink",bd=5,command=add)
b1.place(x=350,y=300)

b2=Button(win,text="Mul",font=("arial",15,"bold"),bg="green",bd=5,command=mul)
b2.place(x=450,y=300)


win.mainloop()
