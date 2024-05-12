#range(): It generates sequence of int values with equal gap

#1. range(start,end,step)
#2. range(start,end)        #default step=1
#3. range(end)              #default start=0,step=1

for x in range(5): #0,1,2,3,4
    print('hello',x)

print('--------------')
for x in range(2,10,3): #2,5,8
    print(x)

print('--------------')
for x in range(1,9,2): #1,3,5,7
    print(x)

print('--------------')
for x in range(1,9): 
    print(x)
