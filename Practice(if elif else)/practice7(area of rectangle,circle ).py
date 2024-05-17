'''Write a program that has following menu:
Enter 1 to find the area of rectangle.
Enter 2 to find the area of circle.
Values for length and width of a rectangle and value of a radius of
circle will be entered through keyboard.'''

#solution
a=input('''Choose a option:
a. Area of Rectangle
b. Area of circle
''')
if a=='a':
    length=float(input('Enter length of Rectangle ='))
    width=float(input('Enter width of Rectangle='))
    r_area=length*width
    print(f"area of rectangle={r_area}")
elif a=='b':
    radius=float(input('Enter radius of circle='))
    pi=3.14
    c_area=pi*radius**2
    print(f'area of circle={c_area}')
else:
    print('Envailid option ')
    
