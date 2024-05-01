#Logical Operators
    #to combine result of 2 comparisions
    #represented by keywords not symbols

a=5
b=10

#Logical and
    # True and True--->True
    # True and False-->False
    # False and True-->False
    # False and False->False
print(b>a and b<20)
print(b>a and b<5)
print(a>b and a==5)

#Logical or
    #True or True--->True
    #True or False-->True
    #False or True-->True
    #False or False->False
print(b>a or b<20) 
print(b>a or b<5)
print(a>b or a==5)
print(a>b or a==15)

#Logical not
    #not True--->False
    #not False-->True

print(b>a)
print(not b>a)




