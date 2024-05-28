#user(standard) I/O
    #output------>print()
    #input------->input()

#File I/O
    #open(file/path)


#mode 'r'--->read() only
#mode 'w'--->write() only
    #'w' mode create file if not found

#mode 'a'--->write()
    #It create file if not found


#file=cwd(from current working dir)
file=open("msg.txt","r")#filePath,mode
text=file.read()
print(text)
file.close()

#path=from given path(not from cwd)
file=open("C:/Users/admin/Desktop/okk.txt","r")#filePath,mode
text=file.read()
print(text)
file.close()
