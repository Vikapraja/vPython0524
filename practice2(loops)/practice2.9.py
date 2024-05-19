#Calculate the cube of all numbers from 1 to a given number.

a=int(input('Enter a number='))
b=0
c=[]
for i in range(a+1):
    b=i**3
    c.append(b)
    
print(c)
