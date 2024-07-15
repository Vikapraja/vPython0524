#Write the function to find that entered number even or odd.


def evenodd(a):
    if a%2==0:
        print(a," is even ")
    else:
        print(a,"is odd")


x=int(input("Enter a num="))
evenodd(x)
