#5.	WAP to print calculate the factorial of number entered through keyboard;

a=int(input('enter num for factorial='))

f=1
for i in range(a,0,-1):
    f=f*i
print(f)

#or
b=int(input('enter num for factorial='))
c=1
while b>=1:
    c=c*b
    b-=1
print(c)    

