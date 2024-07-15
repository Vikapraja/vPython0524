#Write a function that takes two numbers entered through keyboard and return greatest of them.

def greatest():
    a=int(input("Enter 1st num="))
    b=int(input("Enter 2nd num="))
    if a>b:
        print(a,'is greatest')
    elif b>a:
        print(b,'is greatest')
    else:
        print('a and b are equal')

while True:
    greatest()
