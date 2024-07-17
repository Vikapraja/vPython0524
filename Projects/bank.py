from tkinter import *
import time
from tkcalendar import Calendar
from tkinter.ttk import Combobox
from tkinter import messagebox
import sqlite3

try:
    con=sqlite3.connect('vbank.sqlite')
    cur=con.cursor()
    cur.execute("create table acn(acn_no integer primary key autoincrement,acn_adhar int,acn_name text,acn_age int,acn_gender text,acn_phone int,acn_email text,acn_opendate date,acn_pass text,acn_bal float)")
    cur.close()
    print('table created')
except:
    print('something went wrong may be table already exists !')


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

    def welcome_screen():

        def logout():
            frm.destroy()
            main_screen()
        
        frm=Frame(win,bg='powder blue')
        frm.place(relx=0,rely=.14,relwidth=1,relheight=.95)    

        lbl_head=Label(frm,text='Welcome user',font=('arial',20,'bold'),fg='green')
        lbl_head.pack()
    
        btn_logout=Button(frm,text='Logout',font=('arial',15,'bold'),width=10,bd=5,command=logout)
        btn_logout.place(relx=.89,rely=.01)
    
        btn_back=Button(frm,text='Back',font=('arial',15,'bold'),width=10,bd=5,command=main_screen)
        btn_back.place(relx=.01,rely=.01)

    def clear():
        frm.destroy()
        main_screen()
        #or
        #e_acn.delete(0,'end')
        #e_pass.delete(0,'end')
        #e_acn.focus()

    def login():
        a=e_acn.get()
        b=e_pass.get()
        if len(a)==0 or len(b)==0:
            messagebox.showwarning('Validation','Without Account No and Password you can not login !')
            return
        
        elif len(a)!=0 and len(b)!=0:
            welcome_screen()
            return
             

    lbl_head=Label(frm,text='Login Page',font=('arial',20,'bold'),fg='green')
    lbl_head.pack()

    lbl_acn=Label(frm,text='Account No',font=('arial',15,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)

    e_acn=Entry(frm,font=('arial',15),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()

    lbl_pass=Label(frm,text='Password',font=('arial',15,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',15),show='*',bd=5)
    e_pass.place(relx=.4,rely=.2)

    btn_login=Button(frm,text="Login",font=('arial',15,'bold'),bd=5,command=login)
    btn_login.place(relx=.42,rely=.3)

    btn_clear=Button(frm,text="Clear",font=('arial',15,'bold'),bd=5,command=clear)
    btn_clear.place(relx=.5,rely=.3)

    btn_fp=Button(frm,text="Forgot Password",font=('arial',15,'bold'),bd=5,command=forgotpass_screen)
    btn_fp.place(relx=.42,rely=.4)

    btn_newu=Button(frm,text="Create New User",font=('arial',15,'bold'),bd=5,command=newuser_screen)
    btn_newu.place(relx=.42,rely=.5)
    
def forgotpass_screen():

    def pass_db():
        acn_no=e_acn.get()
        acn_email=e_email.get()
        con=sqlite3.connect('vbank.sqlite')
        cur=con.cursor()
        cur.execute('select acn_pass from acn where acn_no=? and acn_email=?',(acn_no,acn_email))
        tup=cur.fetchall()
        messagebox.showinfo('Password founded',f'password={tup[0]}')

    frm=Frame(win,bg='powder blue')
    frm.place(relx=0,rely=.14,relwidth=1,relheight=.95)

    lbl_head=Label(frm,text='Forgot Password Page',font=('arial',20,'bold'),fg='green')
    lbl_head.pack()

    btn_back=Button(frm,text='Back',font=('arial',15,'bold'),width=10,bd=5,command=main_screen)
    btn_back.place(relx=.01,rely=.01)

    lbl_acn=Label(frm,text='Account No',font=('arial',15,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)
    
    e_acn=Entry(frm,font=('arial',15),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()

    lbl_email=Label(frm,text='Email:',font=('arial',15,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.2)
    
    e_email=Entry(frm,font=('arial',15),bd=5)
    e_email.place(relx=.4,rely=.2)

    lbl_phone=Label(frm,text='Phone No:',font=('arial',15,'bold'),bg='powder blue')
    lbl_phone.place(relx=.3,rely=.3)
    
    e_phone=Entry(frm,font=('arial',15),bd=5)
    e_phone.place(relx=.4,rely=.3)
    
    btn_submit=Button(frm,text='Submit',font=('arial',15,'bold'),width=10,bd=5,command=pass_db)
    btn_submit.place(relx=.4,rely=.4)

def newuser_screen():
    frm=Frame(win,bg='powder blue')
    frm.place(relx=0,rely=.14,relwidth=1,relheight=.95)

    def new_db():
        acn_adhar=e_adhar.get()
        acn_opendate=time.strftime('%d %B,%Y')
        acn_name=e_name.get()
        acn_age=e_age.get()
        acn_gender=cb_gender.get()
        acn_phone=e_phone.get()
        acn_email=e_email.get()
        acn_pass=e_confirmpass.get()
        acn_bal=0
        con=sqlite3.connect('vbank.sqlite')
        cur=con.cursor()
        cur.execute('insert into acn(acn_adhar,acn_name,acn_age,acn_gender,acn_phone,acn_email,acn_opendate,acn_pass,acn_bal) values(?,?,?,?,?,?,?,?,?)',(acn_adhar,acn_name,acn_age,acn_gender,acn_phone,acn_email,acn_opendate,acn_pass,acn_bal))
        con.commit()
        #con.close()
        print('inserted'+acn_adhar,acn_opendate)
        con=sqlite3.connect('vbank.sqlite')
        cur.execute('select acn_no from acn where acn_phone=? and acn_email=?',(acn_phone,acn_email))
        tup=cur.fetchone()
        messagebox.showinfo('account Created \n ',message=f'User Account No. is{tup[0]} and password={acn_pass}')
        cur.close()
        
        e_adhar.delete(0,'end')
        e_name.delete(0,'end')
        e_age.delete(0,'end')
        cb_gender.delete(0,'end')
        e_phone.delete(0,'end')
        e_email.delete(0,'end')
        e_confirmpass.delete(0,'end')

        
        newuser_screen()

    lbl_head=Label(frm,text='Create New User Page',font=('arial',20,'bold'),fg='green')
    lbl_head.pack()

    btn_back=Button(frm,text='Back',font=('arial',15,'bold'),width=10,bd=5,command=main_screen)
    btn_back.place(relx=.01,rely=.01)

    lbl_adhar=Label(frm,text='Adhar No',font=('arial',15,'bold'),bg='powder blue')
    lbl_adhar.place(relx=.3,rely=.1)
    
    e_adhar=Entry(frm,font=('arial',15),bd=5)
    e_adhar.place(relx=.4,rely=.1)
    e_adhar.focus()

    lbl_name=Label(frm,text='Name:',font=('arial',15,'bold'),bg='powder blue')
    lbl_name.place(relx=.3,rely=.2)

    e_name=Entry(frm,font=('arial',15),bd=5)
    e_name.place(relx=.4,rely=.2)

    lbl_age=Label(frm,text="Age:",bg='powder blue',font=('arial',15,'bold'))
    lbl_age.place(relx=.6,rely=.2)

    e_age=Entry(frm,font=('arial',15),bd=5)
    e_age.place(relx=.7,rely=.2)

    lbl_gender=Label(frm,text='Gender:',font=('arial',15,'bold'),bg='powder blue')
    lbl_gender.place(relx=.3,rely=.3)

    cb_gender=Combobox(frm,value=['---select gender----','MALe','FEMALE'],font=('arial',15,'bold'))
    cb_gender.place(relx=.4,rely=.3)
    
    lbl_email=Label(frm,text='Email:',font=('arial',15,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.4)
    
    e_email=Entry(frm,font=('arial',15),bd=5)
    e_email.place(relx=.4,rely=.4)

    lbl_phone=Label(frm,text='Phone No:',font=('arial',15,'bold'),bg='powder blue')
    lbl_phone.place(relx=.3,rely=.5)
    
    e_phone=Entry(frm,font=('arial',15),bd=5)
    e_phone.place(relx=.4,rely=.5)

    lbl_createpass=Label(frm,text='Create Password:',font=('arial',10,'bold'),bg='powder blue')
    lbl_createpass.place(relx=.3,rely=.6)
    
    e_createpass=Entry(frm,font=('arial',15),bd=5)
    e_createpass.place(relx=.4,rely=.6)

    lbl_confirmpass=Label(frm,text='Confirm Password:',font=('arial',10,'bold'),bg='powder blue')
    lbl_confirmpass.place(relx=.3,rely=.7)
    
    e_confirmpass=Entry(frm,font=('arial',15),bd=5)
    e_confirmpass.place(relx=.4,rely=.7)
    
    btn_submit=Button(frm,text='Submit',font=('arial',15,'bold'),width=10,bd=5,command=new_db)
    btn_submit.place(relx=.4,rely=.8)

main_screen()




























win.mainloop()
