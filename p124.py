#raise keyword:it is used to generate exception forcefully

age=int(input("Enter age="))
if age<0:
    raise ValueError("-ve age found")
dob=2024-age
print(dob)
