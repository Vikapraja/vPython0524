from tkinter import *
import time

win=Tk()
win.title("Nanking-Automation")
win.state('zoomed')
win.resizable(width=False,height=False)
win.configure(bg='orange')

title=Label(win,text='Banking Automation',bg='orange',font=('arial',40,'bold','underline'))
title.pack()

#date
dt=time.strftime('%d %B,%Y')
date=Label(win,text=dt,font=('arial',15),fg='blue',bg='orange')
date.place(relx=.90,rely=.1)

#main_window

def main_screen():        
    frm=Frame(win,bg='powder blue')
    frm.place(relx=0,rely=.14,relwidth=1,relheight=.95)

    lbl_acn=Label(frm,text='Account No',font=('arial',15,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)

    lbl_pass=Label(frm,text='Password',font=('arial',15,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)

    e_acn=Entry(frm,font=('arial',15),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()

    e_pass=Entry(frm,font=('arial',15),show='*',bd=5)
    e_pass.place(relx=.4,rely=.2)
    e_pass.focus()

    btn_login=Button(frm,text="Login",font=('arial',15,'bold'),bd=5)
    btn_login.place(relx=.42,rely=.3)

    btn_clear=Button(frm,text="Clear",font=('arial',15,'bold'),bd=5)
    btn_clear.place(relx=.5,rely=.3)

    btn_forg=Button(frm,text="Forgot Password",font=('arial',15,'bold'),bd=5)
    btn_forg.place(relx=.42,rely=.4)

    btn_newu=Button(frm,text="Create New User",font=('arial',15,'bold'),bd=5)
    btn_newu.place(relx=.42,rely=.5)

main_screen()




























win.mainloop()
