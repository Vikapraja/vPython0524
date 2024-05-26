import os
print(os.getcwd())# returns path of cwd =current working directory

li=os.listdir('abc')#returns a list of all file/folder names predent
                    #inside abc older of cwd

#print(li) #or
for i in li:
    print(i)

li=os.listdir("D:/tig/vPython0524/abc/")#returns a list of all dirs inside 
print(li)                                        #abc folder of given path.


os.mkdir("test")#create test folder in cwd,error if already exists
