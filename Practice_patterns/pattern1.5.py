#pattern 5

for i in range(1,6):
    for j in range(0,5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
