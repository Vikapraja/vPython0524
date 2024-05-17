a=5#global to program
b=6
def mul():
    global a
    a=10
    b=20
    print(a*b)


def add():
    print(a+b)

mul()
add()
print(a)

#Type of variable based on Scope
    #Local Variable
        #defined inside function block
        #can be used by same function only

    #Global variable
        #defined at top level(outside function block)
        #can be used by program

#note:
    #name of local var can be same as name of global var, in the
    #case function gives the priority to local

    #function can use global var by defining them global using 'global' keyword.









