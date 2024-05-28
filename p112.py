#taken text from a file for send email

import gmail
con=gmail.GMail("vivekanandprajapati595@gmail.com","ood efrq gcgm xock")
file=open("msg.txt","r")
data=file.read()
file.close()
print("k")
msg=gmail.Message(to="vibekapotter0@gmail.com",subject="For 'gmail' Library testing in vPython",text=data)
con.send(msg)
print("mail sent")
