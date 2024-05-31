#regex for find (gmail)

file=open("data.txt","r")
text=file.read()
#print(text)
file.close()

import re
li=re.findall('[A-Za-z0-9_.]+@[a-zA-Z]+[.][a-zA-Z]{2,3}',text)
f=open("data_gmail.txt","w")
for i in li:    
    f.write(i)
    f.write('\n')

print('done')


f.close()

