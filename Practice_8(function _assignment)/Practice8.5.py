#5 Write the function to print the Fibonacci series. The number of terms for Fibonacci series will be entered through keyboard.

def fibonacci(x):
    flist=[]
    a=0
    b=1
    f=0
    for i in range(x+1):
        flist.append(f)
        a+=1
        a=b
        b=f
        f=a+b

        
    print(flist)

     
a=int(input("Enter a terms="))
fibonacci(a)
