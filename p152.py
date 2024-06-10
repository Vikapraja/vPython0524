#
from tkinter import Tk,Button,Label
from PIL import Image,ImageTk

win=Tk()                                
win.geometry("600x400")

lb1=Label(win,text="This is Python",font=("arial",30,"bold","underline"))
lb1.pack()

Image.open("c:/home/badal/Pictures/crome.png").resize((200,120))
img2=Image.PhotoImage(img)

lb12=Label(win,image=img2)
lb1.place(x=100,y=100)


win.mainloop()
