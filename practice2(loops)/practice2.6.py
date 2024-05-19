#6.	WAP to check prime number entered through keyboard.

a=int(input('Enter a number to know prime no='))
for i in range(2,a):
    if a%i==0:
        print(a,' is not prime')
    else:
        print(a,' is prime')
        

        
        
