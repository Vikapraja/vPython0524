'''Admission to professional course in a college according to
following conditions:
Marks in Mathematics are greater than or equal to 60 and marks in
physics are greater than or equal to 50 and marks in chemistry are
greater than or equal to 40

OR

Total marks in mathematics, physics and chemistry are greater than
or equal to 200.

OR

Total marks in mathematics and physics are greater than or equal to
150.
Marks of all three subjects will be entered through the keyboard.
WAP to tell whether a student is qualifying for admission or not.'''

print("Admission to professional course in a college")

math=float(input("Enter Mathematics marks ="))
physics=float(input("Enter Physics marks ="))
chemistry=float(input("Enter Chemistry marks ="))

total=math+physics+chemistry
print(f"Total marks of three subjects={total}")
if total>=150:
    print("Qualified for Addmission")
else:
    print("")






