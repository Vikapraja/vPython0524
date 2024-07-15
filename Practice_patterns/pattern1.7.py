#pattern 7

for i in range(5,0,-1):
    for j in range(5-i,0,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print(" ")
