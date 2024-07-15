from tkinter import*
import random

win=Tk()
win.title("Random Button")
win.geometry("999x899")

a=random.randint(1,900)
b=random.randint(1,900)

def chenged():
    global win
    for i in win.winfo_children():
        i.grid_remove()
    
    frm=Frame(bg='powder blue')
    frm.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    a=random.randint(1,900)
    b=random.randint(1,900)
    l1=Label(frm,text=f'x={a},y={b}',font=('arial',15,'bold')).place(x=a+13,y=b-25)
    b1=Button(frm,text="I am runable",font=("arial",15),bg='orange',bd=8,command=chenged).place(x=a,y=b)

b1=Button(win,text="I am runable",font=("arial",15),bg='orange',command=chenged).place(x=50,y=50)

chenged()

win. mainloop()
