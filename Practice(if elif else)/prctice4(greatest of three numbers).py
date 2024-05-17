'''WAP to find the greatest of three numbers entered through
keyboard.'''

a=int(input('Enter a number='))
b=int(input('Enter b number='))
c=int(input('Enter c number='))
if a>b and a>c:
    print(f'{a} is greatest')
elif b>a and b>c:
    print(f"{b} is greatest")
elif c>a and c>b:
    print(f"{c} is greatest")
