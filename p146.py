
from tkinter import Tk,Button
win=Tk()                                
win.geometry("600x400")               
win.configure(bg="yellow")          

b1=Button(win,text="submit",fg="red",width=7,font=("arial",20,'bold'),bd=5,bg='pink')            
b2=Button(win,text="ok",width=7,font=("arial",20,'bold'),bd=5,bg='powder blue')                

#relative place[for responsive window]
b1.place(relx=.2,rely=.4)
b2.place(relx=.5,rely=.4)
win.mainloop()                          

#[ responsive window=components change position and resize on run time according window resizable]
