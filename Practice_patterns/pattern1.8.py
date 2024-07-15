#pattern 8

x=int(input("Enter a no to print pattern ="))

for i in range(x+1,1,-1):
    for j in range(x+1-i,x):
        print(" ",end=" ")
    for k in range(1,x+3-i):
        if k<=x:
            print(k,end=" ")
    for l in range(x+1,j):
        print(" ",end=" ")
    for m in range(x+1-i,0,-1):
        if m<=(x-1):
            print(m,end=" ")
    print(" ")

for i in range(1,x+1):
    for j in range(1,i+2):
        print(" ",end=" ")
    for k in range(1,x+1-i):
        print(k,end=" ")
    for m in range(x-1-i,0,-1):
        print(m,end=" ")
    for l in range(1,i):
        print(" ",end=" ")
    print(" ")
        
