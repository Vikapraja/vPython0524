'''9. WAP that implements the simple calculator that has following menu:
Enter 1 to find the addition of two numbers.
Enter 2 to find the subtraction of two numbers.
Enter 3 to find the multiplication of two numbers.
Enter 4 to find the division of two numbers.
Enter 5 to find the inverse of a number.
Enter 6 to find the square of a number.
Enter 7 to find the cube of a number.'''

a=input('''Calculator's option \n-------------------------
Enter 1 to find the addition of two numbers.
Enter 2 to find the subtraction of two numbers.
Enter 3 to find the multiplication of two numbers.
Enter 4 to find the division of two numbers.
Enter 5 to find the inverse of a number.
Enter 6 to find the square of a number.
Enter 7 to find the cube of a number.\n Choose a option=''')

if a=='1':
    print("addition of two numbers:")
    num1=float(input('Enter a number='))
    num2=float(input('Enter b number='))
    add=num1+num2
    print(f'Addition of {num1} and {num2} is {add}')

elif a=='2':
    print("Subtraction of two numbers:")
    num1=float(input('Enter a number='))
    num2=float(input('Enter b number='))
    sub=num1-num2
    print(f'Subtraction of {num1} and {num2} is {sub}')
elif a=='3':
    print("Multiplication of two Numbers:")
    num1=float(input('Enter a number='))
    num2=float(input('Enter b number='))
    mul=num1*num2
    print(f'Multiplication of {num1} and {num2} is {mul}')
elif a=='4':
    print("Division of two Numbers:")
    num1=float(input('Enter a number='))
    num2=float(input('Enter b number='))
    div=num1/num2
    print(f'Division of {num1} and {num2} is {div}')
elif a=='5':
    print("Inverse of a Number:")
    num=float(input('Enter a number for inverse='))
    inv=1/num
    print(f'Inverse of {num} is {inv}')
elif a=='6':
    print("Squre of number:")
    num=float(input('Enter a number='))
    print(f'Square of {num} is {num**2}')
elif a=='7':
    print("Cube of a Number:")
    num1=float(input('Enter a number='))
    print(f'Cube of {num1} is {num1**3}')
else:
    print('Invailid option')










