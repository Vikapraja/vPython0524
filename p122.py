print("hi")
li=[10,20,30,40]
try:
    index=int(input("Enter index[0-3]="))
    print(li[index])
except: #default except block
    print("index out of range...")
print("bye")
