#2 types of function
    #1)function(function outside of class)
    #2)method(function in class )

#Note: function and method have same purpose to implement logic

def deposit():
    print("this is deposit function")

class account:
    def deposit(x):
        print("this is deposit method")

deposit()#deposit function call

a1=account()#object creation of account class

a1.deposit()#deposit method call (by interpreter a1.deposit(a1))

a2=account()#by interpreter a2.deposit(a2)

#method: >function that are defined in class known as method otherwise function
