#eval() =>to solve  expression written in str
from tkinter import Tk,Button,Label,Entry,messagebox

def result():
    a=e1.get()      
    res=eval(a)     #eval function for soltion of expression written in str
    print(res)
    lb3=Label(win,text=f"result={res}",font=("arial",20,"bold"),bg="pink",bd=5)
    lb3.place(x=250,y=30)
    messagebox.showinfo("Solution",f"{res}")

win=Tk()                                
win.geometry("600x400")
win.configure(bg="yellow")

lb1=Label(win,text="Enter Expression",font=("arial",20,"bold"),bg="yellow",bd=5)
lb1.place(x=80,y=100)

e1=Entry(win,font=("aria",15),bd=5)
e1.place(x=350,y=100)

b1=Button(win,text="Solution",font=("arial",15,"bold"),bg="pink",bd=5,command=result)
b1.place(x=350,y=300)



win.mainloop()
