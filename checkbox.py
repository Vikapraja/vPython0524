from tkinter import *
top=Tk()
top.geometry('500x500')
top.title('writer')
Label(text='What would u like to have?',font=20,pady=20).pack()
radio=Checkbutton(text='dosa').pack()
radio=Checkbutton(text='bada').pack()
radio=Checkbutton(text='idli').pack()
radio=Checkbutton(text='uttapam').pack()
radio=Checkbutton(text='upma').pack()
top.mainloop()
