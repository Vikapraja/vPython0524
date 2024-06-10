from tkinter import Tk,Button
win=Tk()                                
win.geometry("600x400")               
win.configure(bg="yellow")          

b1=Button(win,text="submit",fg="red",width=7,font=("arial",20,'bold'),bd=5,bg='pink')            
b2=Button(win,text="ok",width=7,font=("arial",20,'bold'),bd=5,bg='powder blue')              

#pack
b1.pack()     
b2.place(x=100,y=300)

win.mainloop()                         

