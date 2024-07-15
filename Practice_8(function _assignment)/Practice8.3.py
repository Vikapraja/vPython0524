#3Write the function to find out whether entered number is prime or not.
#if num is divisable by any other num except 1,itself thats a prime num 


def isprime(x):#every num is dividable by 1
        if x<=3 and x>0:
                print(x," is prime")
        elif x>3:
                for i in range(2,x+1):
                        if x==i:
                                print(x," is prime")
                                break
                        elif x%i==0:
                                print(x,"is not prime")
                                break

a=int(input("Enter a num="))
isprime(a)
