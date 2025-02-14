num=int(input("enter any no:"))
for i in range(num,0,-1):
    for j in range(0,num-i+1):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
    
