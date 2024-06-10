#frame(child window) 

from tkinter import Tk,Button,Frame
win=Tk()                                
win.geometry("600x400")               
win.configure(bg="yellow")

frm=Frame(win)
frm.place(x=100,y=100,width=350,height=200)
frm.configure(bg="powder blue")



b1=Button(frm,text="submit-1",font=("arial",20,'bold'),bd=5)            
b2=Button(frm,text="submit-2",font=("arial",20,'bold'),bd=5)            
b3=Button(frm,text="submit-3",font=("arial",20,'bold'),bd=5)              
b4=Button(frm,text="submit-4",font=("arial",20,'bold'),bd=5)              

b1.grid(row=0,column=0)
b2.grid(row=0,column=1) 
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)

win.mainloop                        

