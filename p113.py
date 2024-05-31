#'w' mode 
    #for write in the file
    #it create file if not found

file=open("abc.txt","w")
file.write("jay ho\n")
file.write("hi")
file.close()

#'r' mode
    #for read() only
file=open("abc.txt","r")
a=file.read()
file.close()

print(a)

