#8.	Write a Python program to get the Fibonacci series between 0 to 50.  
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
a=0
b=1
s=[]
for i in range(51):
    s.append(a)
    a,b=b,a+b
    if a>51:
        break
print(s)    

#or
c=0
d=1
s1=[]
while c<=51:
    s1.append(c)
    c,d=d,c+d
print(s1)
    
