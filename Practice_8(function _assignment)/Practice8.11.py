#Write a function that takes numbers entered through keyboard and return the sum of digits of entered numbers.



def digitsum():
    x=int(input("Enter number to get sum of it's digit="))
    a=str(x)
    dsum=0
    for i in a:
        dsum+=int(i)
    print(dsum)

while 1<2:
    digitsum()
