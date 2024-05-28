#gmail module
    #syntax

'''
import gmail
con=gamil.GMail("gmail id","app password")
msg=gmail.Message(to="reciever gmail id",subject="",text="hhi")
con.send(msg)
print("mail sent")

'''
import gmail
con=gmail.GMail("vivekanandprajapati595@gmail.com","ood efrq gcgm xock")
msg=gmail.Message(to="vibekapotter0@gmail.com",subject="For 'gmail' Library testing in vPython",text="Hi,\n\tMy name is Vivekanand Prajapati. Cuurently I am doing Python Full Stack Development at Ducat India, Noida sec-16.\n\t\tI am testing gmail Library in Python Programming.\n\t\t\tThank You.")
con.send(msg)
print("mail sent")
