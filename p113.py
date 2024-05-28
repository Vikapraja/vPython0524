#'w' and 'r' mode

file=open("abc.txt","w")
file.write("jay ho\n")
file.write("hi")
file.close()


file=open("abc.txt","r")
a=file.read()
file.close()

print(a)

