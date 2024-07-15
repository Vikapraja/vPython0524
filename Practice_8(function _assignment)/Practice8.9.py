#Write a function that takes a number entered through keyboard and find whether it is Armstrong number or not.



def isarmstrong(x):
    a=str(x)
    d=0
    for i in a:
        b=int(i)
        c=b**3
        d+=c
    if d==x:
        print("yes")
    else:
        print("no")


while 1<2:
    a=int(input("Enter num to check num is armstrong or not: "))
    isarmstrong(a)
