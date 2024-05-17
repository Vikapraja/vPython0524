'''Enter 1 to find out whether the entered number is even or odd.
Enter 2 to find out whether the entered number is positive or
negative.'''

#solution
print('after entering number press enter key:')
a=float(input('Plz Enter the Number ='))
b=input('''Menu  for entered Number:

1. To know even or odd
2. To know positive or negative

plz enter the option=''')

if b=='1':
    if a%2==0:
        print(f'{a} is even')
    else:
        print(f'{a} is odd')
elif b=='2':
    if a>=0:
        print(f"{a} is positive")
    else:
        print(f"{a} is negative")
else:
    print("invailid option")
















    
