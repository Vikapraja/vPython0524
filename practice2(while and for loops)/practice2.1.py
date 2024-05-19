#1.	WAP to print all even and odd numbers between 1 and 100;

a=1
while a<=100:
    if a%2==0:
        print(a,' even')
    else:
        print(a,' odd')
    a+=1
#or
for i in range(1,101):
    if i%2==0:
        print(i,' even')
    else:
        print(i,' odd')
    
    
