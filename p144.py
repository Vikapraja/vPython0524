from tkinter import Tk
win=Tk()                                #create window
#win.geometry("600x400")                 #initial size of window(WxH)
win.state("zoomed")                     #full screen vindow
win.resizable(width=True,height=False)  #disable resizing at runtime
win.configure(bg="yellow")              #set bgcolor of window
win.mainloop()                          #Make the window visible
