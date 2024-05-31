

file=open("data.txt","r")
text=file.read()
file.close()
print(text)

#reguler expression for phone no

import re
li=re.findall('[6-9][0-9]{9}',text)
pn=open("data_phone.txt","w")
for i in li:
    pn.write(i)
    pn.write('\n')
pn.close()


file=open("data_phone.txt","r")
text=file.read()
file.close()
print(text)

pn.close()



    
    
    
