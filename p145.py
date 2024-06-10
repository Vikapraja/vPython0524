from tkinter import Tk,Button

win=Tk()                                #create window
win.geometry("600x400")                 #initial size of window(WxH)
win.configure(bg="yellow")              #set bgcolor of window

b1=Button(win,text="Submit")

#absolute place
win.mainloop()                          #Make the window visible
