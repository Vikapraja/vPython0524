print("hi")
li=[10,20,30,40]
try:
    index=int(input("Enter index[0-3]="))
    print(li[index])
except IndexError:
    print("index out of range...")
finally:
    print("this i finally")
print("bye")

#try:
    #it contains those stmts whose execution may raise exception

#except:
    #It is the handler of exception
    #It is only executed if exception raised from try block

#Finally:
    #it is optional block and is executed irrespect of exception in try block
    #generally, we use finally to free/close the resources.









