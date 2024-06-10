x#grid-layout 

from tkinter import Tk,Button
win=Tk()                                
win.geometry("600x400")               
win.configure(bg="yellow")          

b1=Button(win,text="submit-1",font=("arial",20,'bold'),bd=5)            
b2=Button(win,text="submit-2",font=("arial",20,'bold'),bd=5)            
b3=Button(win,text="submit-3",font=("arial",20,'bold'),bd=5)              
b4=Button(win,text="submit-4",font=("arial",20,'bold'),bd=5)              

b1.grid(row=0,column=0)
b2.grid(row=0,column=1) 
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)

win.mainloop                        

