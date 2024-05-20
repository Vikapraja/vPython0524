#Module:
        #A module is a simply python file wich is imported in other program.

import calculator #module
print(calculator.add(5,6))
print(calculator.mul(5,6))


x=int(input('Enter 1st number='))
y=int(input('Enter 2st number='))
print(calculator.mul(x,y))

import calculator as calc #alias(assumed name)
print(calc.add(5,6))
print(calc.mul(5,6))
