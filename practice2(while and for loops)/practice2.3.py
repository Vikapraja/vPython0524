#3.	WAP to print sum of numbers from 1 and 100;

a=1
b=0
while a<=100:
    b+=a#b=b+a
    if a==100:
        print(b)
    a+=1
    
#or
c=0
for i in range(1,101):
    c+=i#c=c+a
    if i==100:
        print(c)
