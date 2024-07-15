#Write a function to find entered number through keyboard is whether palindrome or not.


def ispalidrome(x):
        a=str(x)
        b=a[-1::-1]
        if a==b:
            print("yes")
        else:
            print("no")

while 1<2:
    x=int(input("Enter a num to check num is palindrome or not ="))
    ispalidrome(x)


