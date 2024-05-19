#2.	WAP to print all even and odd numbers between 100 and 1;
a=100
while a>=1:
    if a%2==0:
        print(a,' even')
    else:
        print(a,' odd')
    a-=1
    
#or
for i in range(100,0,-1):
    if i%2==0:
        print(i,' even')
    else:
        print(i,' odd')
    
