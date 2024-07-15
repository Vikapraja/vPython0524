#pattern 9

x=int(input("Enter a no to print pattern ="))

for i in range(x,0,-1):
    for j in range(x,x-i+1,-1):
        print(" ",end=" ")
    for k in range(x,i-1,-1):
        if k<=x:
            print(k,end=" ")
    for l in range(x,x-1+1,-1):
        print(" ",end=" ")
    for m in range(i+1,x+1):
        if m<=(x):
            print(m,end=" ")
    print(" ")

for i in range(1,x+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(x,i,-1):
        print(k,end=" ")
    for m in range(2+i,x+1):
        print(m,end=" ")
    for l in range(1,i):
        print(" ",end=" ")
    print(" ")
        
