from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog
from tkinter import ttk
from datetime import datetime
#import pymysql
taz=Tk()
#user_icon=ImageTk.PhotoImage(Image.open('images/user.png'))
tazTV = ttk.Treeview(height=8, columns=('Item Name''Rate','Type'))
tazTV1=ttk.Treeview(height=8,columns=('Date''Name','Type','Rate','total'))

def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False
callback1 = taz.register(only_numeric_input)  # registers a Tcl to Python callback

def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()

#### database Connection ################
def db_connect():
    global mycursor, connection
    connection = pymysql.connect(user="root", host="127.0.0.1", db="summer")
    mycursor = connection.cursor()
#### main heading ###########
def mainheading():
    label=Label(taz,text="Hotel Management System" ,bg="yellow",
                fg="red",font=("Comic Sans Ms","48","bold"),padx=270)
    label.grid(row=0,column=0,columnspan=5)

def OnDoubleClick(event):
    item = tazTV.selection()
    itemNameVar1 = tazTV.item(item, "text")
    item_detail = tazTV.item(item, "values")
    #print(itemNameVar1)
    #print(item_detail)
    itemnameVar.set(itemNameVar1)
    itemrateVar.set(item_detail[0])
    itemTypeVar.set(item_detail[1])

###### get item in tree view ######
def getItemInTreeView():
    # to delete already inserted item
    records = tazTV.get_children()

    for element in records:
        tazTV.delete(element)

    # insert data in treeview
    conn = pymysql.connect(host="localhost", user="root", db="summer")
    mycursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select * from itemlist"
    mycursor.execute(query)
    data = mycursor.fetchall()
    #print(data)

    for row in data:
        tazTV.insert('', 'end', text=row['item_name'], values=(row["item_rate"], row["item_type"]))
    tazTV.bind("<Double-1>", OnDoubleClick)
    conn.close()

################## add item window ##################
itemnameVar=StringVar()
itemrateVar=StringVar()
itemTypeVar=StringVar()
def additem():
    print(itemnameVar.get(),itemrateVar.get(),itemTypeVar.get())
    x=itemnameVar.get()
    y=itemrateVar.get()
    z=itemTypeVar.get()
    print(x,y,z)
    if x=='' or y=='' or z=='':
        messagebox.showerror("Insertion Error", " Please Enter All Fields")
    else:
        db_connect()
        quei="insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)"
        val=(x,y,z)
        mycursor.execute(quei,val)
        connection.commit()
        messagebox.showinfo("Data Insertion","Data Interted successfully")
        getItemInTreeView()
        itemnameVar.set('')
        itemrateVar.set('')
        itemTypeVar.set('')

def updateitem():
    x = itemnameVar.get()
    y = itemrateVar.get()
    z = itemTypeVar.get()
    print(x, y, z)
    db_connect()
    queup = "update itemlist set item_rate=%s, item_type=%s where item_name=%s"
    val = (y,z,x)
    mycursor.execute(queup, val)
    connection.commit()
    messagebox.showinfo("Data Updation", "Data Updated successfully")
    getItemInTreeView()

def deleteitem():
    x = itemnameVar.get()
    y = itemrateVar.get()
    z = itemTypeVar.get()
    print(x, y, z)
    db_connect()
    queup = "delete from itemlist  where item_name=%s"
    val = (x)
    mycursor.execute(queup, val)
    connection.commit()
    messagebox.showinfo("Data Deletion", "Data Deleted successfully")
    getItemInTreeView()

def hmanage():
    remove_all_widgets()
    mainheading()

    HotalmanagementLabel = Label(taz, text="Hotel Management", compound=LEFT, bg='red', font="Arial 34 bold")
    HotalmanagementLabel.grid(row=1, column=2)

    logoutButton = Button(taz, text="LogOut", font="Arial 20 bold", fg="green", bd=3,bg='pink',
                          command=loginwindow)
    logoutButton.grid(row=1, column=4)

    backButton = Button(taz, text="<- Back", font="Arial 20 bold", fg="green", bd=3,bg='pink',
                          command=welcomewindow)
    backButton.grid(row=1, column=0)

    ItemnameLabel = Label(taz, text="Item-Name", bg='cyan', font="Arial 20")
    ItemnameLabel.grid(row=8, column=0, pady=10)

    ItemrateLabel = Label(taz, text="Item-Rate", bg='cyan', font="Arial 20")
    ItemrateLabel.grid(row=9, column=0, pady=10)

    ItemtypeLabel = Label(taz, text="Item-Type", bg='cyan', font="Arial 20")
    ItemtypeLabel.grid(row=10, column=0, pady=10)

    ItemnameEntry = Entry(taz, textvariable=itemnameVar, font="Arial 20")
    ItemnameEntry.grid(row=8, column=1, pady=10)

    ItemrateEntry = Entry(taz, textvariable=itemrateVar, font="Arial 20")
    ItemrateEntry.grid(row=9, column=1, pady=10)
    #validation
    ItemrateEntry.configure(validate="key", validatecommand=(callback1,"%P"))

    ItemtypeEntry = Entry(taz,  textvariable=itemTypeVar, font="Arial 20")
    ItemtypeEntry.grid(row=10, column=1,pady=10)

    insertButton = Button(taz, text="Insert", font="Arial 20 bold", fg="green", bd=2,bg='light green',
                          command=additem)
    insertButton.grid(row=11, column=0,pady=10)

    updateButton = Button(taz, text="Update", font="Arial 20 bold", fg="green", bd=2,bg='light green',
                          command=updateitem)
    updateButton.grid(row=11, column=1,pady=10)

    deleteButton = Button(taz, text="Delete", font="Arial 20 bold", fg="green", bd=2,bg='light green',
                          command=deleteitem)
    deleteButton.grid(row=11, column=2,pady=10)

###################  treeview ###########################

    tazTV.grid(row=7, column=1, columnspan=4,padx=200,pady=50)
    style = ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview", fieldbackground="pink")
    scrollBar = Scrollbar(taz, orient="vertical", command=tazTV.yview)
    scrollBar.grid(row=7, column=3,padx=190,pady=50, sticky="NSE")

    tazTV.configure(yscrollcommand=scrollBar.set)

    tazTV.heading('#0', text="Item Name")
    tazTV.heading('#1', text="Rate")
    tazTV.heading('#2', text="Type")

    getItemInTreeView()

width=taz.winfo_screenwidth()
height=taz.winfo_screenheight()
#print(width,height)

#############bill window  ###################

global x
x=datetime.now()
datetimeVar=StringVar()
datetimeVar.set(x)

customernameVar=StringVar()
contactVar=StringVar()

combovariable=StringVar()

baserate=StringVar()

cost=StringVar()

qtyvariable=StringVar()

v=StringVar()


###################### Combo data ########
def comboinput():
    db_connect()
    mycursor.execute('select item_name from itemlist')
    data = []
    for row in mycursor.fetchall():
        data.append((row[0]))
    return data

############# rate autofill ########
def optionCallBack(*args):
    global itemname
    itemname=combovariable.get()
    print(itemname)
    aa=ratelist()
    baserate.set(aa)
    global v
    for i in aa:
        for j in i:
            v = j
################optionCallBack2############
def optionCallBack2(*args):
    global qty
    qty = qtyvariable.get()
    final = int(v) * int(qty)
    cost.set(final)
########### ratelist #######33
def ratelist():
    db_connect()
    que2="select item_rate from itemlist where item_name=%s"
    val=(itemname)
    mycursor.execute(que2,val)
    data=mycursor.fetchall()
    return data

########  SAVEbill #3333333
def savebill():
    db_connect()
    dt=datetimeVar.get()
    customer=customernameVar.get()
    contactNo=contactVar.get()
    itemname=itemnameVar.get()
    itemrate=v
    itemQuantity=qtyvariable.get()
    totalcost=cost.get()

    print(dt, customer)
    insqu="insert into bill(datetime,customer_name,contact_no,item_name,item_rate,item_quantity,cost)values(%s,%s,%s,%s,%s,%s,%s)"
    #insqu="INSERT INTO `bill`(`datetime`, `customer_name`, `contact_no`, `item_name`, `item_rate`, `item_quantity`, `cost`) VALUES ('[%s]','[%s]','[%s]','[%s]','[%s]','[%s]','[%s]','[%s]')"
    val=(dt,customer,contactNo,itemname,itemrate, itemQuantity,totalcost)
    mycursor.execute(insqu,val)
    connection.commit()
    messagebox.showinfo("Save data","Bill save Succesefully")
    dt.set("")
    customer.set("")
    contactNo.set("")
    itemname.set("")
    itemrate.set("")
    itemQuantity.set("")
    totalcost.set("")

######## print bill #########
def printBill():
    remove_all_widgets()
    mainheading()
    billLabel = Label(taz, text="Bill-Print ", compound=LEFT, font="Arial 30 bold", bg='red')
    billLabel.grid(row=1, column=1, padx=1, columnspan=2, pady=10)

    backButton = Button(taz, text="<- Back", font="Arial 20 bold", fg="green", bd=3, bg='pink',
                        command=billgenrate)
    backButton.grid(row=1, column=0)

    logoutButton = Button(taz, text="LogOut", font="Arial 20 bold", fg="green", bd=3, bg='pink',
                          command=loginwindow)
    logoutButton.grid(row=1, column=3)

    noteLabel = Label(taz, text=" Note-> To print bill, double click on bill ", compound=LEFT, font="Arial 15 bold", bg='orange')
    noteLabel.grid(row=10, column=0, padx=1, columnspan=2, pady=10)

  ####################treeview###########################
    tazTV1.grid(row=7,column=0,columnspan=4,padx=200,pady=80)
    style=ttk.Style(taz)
    style.theme_use('clam')
    style.configure("Treeview",fieldbackground="green")
    #scrollBar=Scrollbar(taz,orient="vertical",command=tazTV1.yview)
    #scrollBar.grid(row=7,column=2,padx=180, sticky="NSE")

    #tazTV1.configure(yscrollcommand=scrollBar.set)

    tazTV1.heading('#0', text="Date & Time")
    tazTV1.heading('#1', text="Customer Name")
    tazTV1.heading('#2', text="Mobile No")
    tazTV1.heading('#3', text="Selected Food")
    tazTV1.heading('#4', text="Total cost")
    displaybill()

#####################display bill########
def displaybill():
     # to delete already inserted item
     records=tazTV1.get_children()

     for element in records:
         tazTV.delete(element)

     # insert data in treeview
     conn=pymysql.connect(host="localhost", user="root", db="summer")
     mycursor=conn.cursor(pymysql.cursors.DictCursor)
     query="select * from bill"
     mycursor.execute(query)
     data=mycursor.fetchall()
     # print(data)
     for row in data:
         tazTV1.insert('','end',text=row['datetime'],values=(row["customer_name"],row['contact_no'],row['item_name'],row['cost']))
     conn.close()
     tazTV1.bind("<Double-1>", OnDoubleClick2)

#################OnDoubleClick2#############
def OnDoubleClick2(event):
    item=tazTV1.selection()
    global itemNameVar11
    itemNameVar11=tazTV1.item(item, "text")
    item_detail1=tazTV1.item(item, "values")
    receipt()

############### receipt ##############
def receipt():
    billstring=""
    billstring+="=============My Hotel Bill============\n\n"
    billstring +="===========Customer Detail============\n\n"

    db_connect()
    query="select * from bill where datetime='{}';".format(itemNameVar11)
    mycursor.execute(query)
    data=mycursor.fetchall()
    print(data)
    for row in data:
        billstring+="{}{:<20}{:<10}\n".format("DateTime","",row[1])
        billstring+="{}{:<20}{:<10}\n".format("Customer Name","",row[2])
        billstring+="{}{:<20}{:<10}\n".format("Contact No","",row[3])
        billstring+="\n============Item Detail============\n"
        billstring+="{:<10}{:<10}{:<15}{:<15}".format("Item Name","Rate","Quantity","Total Cost")
        billstring+="\n{:<10}{:<10}{:<25}{:<25}".format(row[4],row[5],row[6],row[7])
        billstring+="\n\n================================\n"
        billstring+="{}{:<10}{:<15}{:<10}\n".format("Total Cost"," "," ",row[7])
        billstring+="\n\n===========Thanks Please Visit Again=======\n"



    billFile=filedialog.asksaveasfile(mode="w",defaultextension="*.txt")
    if billFile is None:
        messagebox.showerror("File Name Error","Invalid File Name")
    else:
        billFile.write(billstring)
        billFile.close()


##################################

def billgenrate():
    remove_all_widgets()
    mainheading()

    billLabel = Label(taz, text="Bill-Generation ", compound=LEFT, font="Arial 30 bold",bg='red')
    billLabel.grid(row=1, column=1, padx=1, columnspan=2, pady=10)

    backButton = Button(taz, text="<- Back", font="Arial 20 bold", fg="green", bd=3, bg='pink',
                        command=welcomewindow)
    backButton.grid(row=1, column=0)

    logoutButton = Button(taz, text="LogOut", font="Arial 20 bold", fg="green", bd=3, bg='pink',
                          command=loginwindow)
    logoutButton.grid(row=1, column=4)

    datetimeLabel = Label(taz, text="Date & Time ", bg='cyan', font="Arial 20")
    datetimeLabel.grid(row=2, column=1, pady=5)

    customerNLabel = Label(taz, text=" Customer-Name  ", bg='cyan', font="Arial 20")
    customerNLabel.grid(row=3, column=1, pady=5)

    ccontactLabel = Label(taz, text="Contact No", bg='cyan', font="Arial 20")
    ccontactLabel.grid(row=4, column=1, pady=5)

    selectitemLabel = Label(taz, text="Select-item ", bg='cyan', font="Arial 20")
    selectitemLabel.grid(row=5, column=1, pady=5)

    itemrateLabel = Label(taz, text="Item-rate  ", bg='cyan', font="Arial 20")
    itemrateLabel.grid(row=6, column=1, pady=5)

    selectitemQLabel = Label(taz, text="Select item-Quantity ", bg='cyan', font="Arial 20")
    selectitemQLabel.grid(row=7, column=1, pady=5)

    castLabel = Label(taz, text="Select-item ", bg='cyan', font="Arial 20")
    castLabel.grid(row=8, column=1, pady=5)
###textboxes
    datetimeEntry = Entry(taz, textvariable=datetimeVar, font="Arial 15 bold")
    datetimeEntry.grid(row=2, column=2, pady=5)

    customerNEntry = Entry(taz, textvariable=customernameVar, font="Arial 15 bold")
    customerNEntry.grid(row=3, column=2, pady=5)
    #validation
    #customerNEntry.configur(validate="key", validatecommand=(callback2, "%P"))

    ccontactEntry = Entry(taz, textvariable=contactVar, font="Arial 15 bold")
    ccontactEntry.grid(row=4, column=2, pady=5)
    ###validation
    #ccontactEntry.configur(validate="key", validatecommand=(callback1, "%P"))

    selectitemEntry = Entry(taz, textvariable=combovariable, font="Arial 15")
    selectitemEntry.grid(row=5, column=2, pady=5)

    l=comboinput()
    c=ttk.Combobox(taz, textvariable=combovariable,font="Arial 15", values=l)
    c.set("select- item")
    combovariable.trace('w',optionCallBack)
    c.grid(row=5, column=2, pady=5)

    itemrateEntry = Entry(taz, textvariable=baserate, font="Arial 15 bold")
    itemrateEntry.grid(row=6, column=2, pady=5)


    global qtyvariable
    l2 =[1,2,3,4,5,6,7,8]
    qty = ttk.Combobox(taz, values=l2, textvariable=qtyvariable, font=("Arial 15 bold"))
    qty.set("Select Quantity")
    qtyvariable.trace('w', optionCallBack2)
    qty.grid(row=7, column=2, padx=20, pady=5)

    costEntry = Entry(taz, textvariable=cost, font="Arial 15 bold")
    costEntry.grid(row=8, column=2, pady=5)

    SaveButton = Button(taz, text=" Save ", font="Arial 20 bold", fg="green", bd=3, bg='pink',
                        command=savebill)
    SaveButton.grid(row=9, column=1, pady=50)

    PrintButton = Button(taz, text=" Print Bill ", font="Arial 20 bold", fg="green", bd=3, bg='pink',
                        command=printBill)
    PrintButton.grid(row=9, column=2, pady=50)


######### welcome window #############
def welcomewindow():
    remove_all_widgets()
    mainheading()
    WelcomeLabel = Label(taz, text="Welcom To Home Page", compound=LEFT, font="Arial 30 bold",bg='red')
    WelcomeLabel.grid(row=1, column=1, padx=50, columnspan=2, pady=10)

    HmanageButton = Button(taz, text="Hotel Management", font="Arial 15 bold", width=15, height=2, fg="green", bd=3,bg='pink', command=hmanage)
    HmanageButton.grid(row=4, column=1,columnspan=2, padx=50, pady=20)

    billButton = Button(taz, text="Bill Generation ", font="Arial 15 bold", width=15, height=2, fg="green", bd=3,bg='pink', command=billgenrate)
    billButton.grid(row=5, column=1, columnspan=2, pady=20)

    logoutButton = Button(taz, text="LogOut", font="Arial 15 bold",width=15, height=2, fg="green", bd=3,bg='pink', command=loginwindow)
    logoutButton.grid(row=6,columnspan=2, column=1, pady=20)


usernameVar = StringVar()
passwordVar = StringVar()

def  adminlogin():
    remove_all_widgets()
    a=usernameVar.get()
    b=passwordVar.get()
    if a=='' or b=='':
        messagebox.showerror("Login Error", " Please Enter Both Fields")
    else:
        db_connect()
        que = "select * from login_info where binary username=%s and binary password=%s"
        val = (a,b)
        mycursor.execute(que, val)
        data = mycursor.fetchall()
        flag = False
        for row in data:
            flag = True

        connection.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'either User Name or Password is incorrect')
            passwordVar.set('')
            usernameVar.set('')

########## login window ######################
def loginwindow():
    passwordVar.set('')
    usernameVar.set('')
    remove_all_widgets()
    mainheading()
    loginLabel = Label(taz, text="Admin Login", compound=LEFT, font="Arial 30")
    loginLabel.grid(row=1, column=1, padx=(70, 0), columnspan=2, pady=50)

    usernameLabel = Label(taz, text="Username", font="Arial 15")
    usernameLabel.grid(row=2, column=1, pady=5)

    passwordLabel = Label(taz, text="Password", font="Arial 15")
    passwordLabel.grid(row=3, column=1, pady=5)

    usernameEntry = Entry(taz, textvariable=usernameVar, font="Arial 15")
    usernameEntry.grid(row=2, column=2, pady=5)

    passwordEntry = Entry(taz, show='#', textvariable=passwordVar, font="Arial 15")
    passwordEntry.grid(row=3, column=2, pady=5)

    loginButton = Button(taz, text="Login", font="Arial 15 bold", width=25, height=3,bg="pink", fg="green", bd=3, command=welcomewindow)#command=adminlogin
    loginButton.grid(row=4, column=1, columnspan=2,pady=50)

width=taz.winfo_screenwidth()
height=taz.winfo_screenheight()
#print(width,height)

loginwindow()
taz.title("Hotel Management System")
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()

