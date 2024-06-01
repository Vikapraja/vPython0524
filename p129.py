class account:
    def deposit(self):
        print("this is deposit method")

a1=account()
a1.deposit()#by interpreter a1.deposit(a1)

a2=account()
a2.deposit()#by interpreter a2.deposit(a2)

#note: when we call a method by python method takes a agrument defaultly
        #that are object self
    #[for it we should give a parameter at method definition time].
    #aelf is a parameter that use object as argument in method

class ticket:
    def bus_n(self,a):
        print(f"bus no={a}")

t1=ticket()
t1.bus_n(20)#by interpreter t1.price(t2,20)
