#4 Write the function to calculate the factorial of a entered number.

def fact(x):
    f=1
    for i in range(x,0,-1):
        f=f*(i)
    print(f)

a=int(input("Enter a num="))
fact(a)
