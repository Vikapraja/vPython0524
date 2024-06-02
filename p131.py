#Constructor :
    #It is a special method in the class with name __init__(self).
    #It is executed once per object when object is created.
    #Generally,we use constructor to define instance data members.

#Syntax ti define instance data member from constructor
    #self.data=value

class account:
    def __init__(self):
        print("this is constructor")

a1=account()
a2=account()

class account:
    ifsc='abc123'#class data members
    def __init__(self,a,b):
        #instance data members
        self.acn=a
        self.bal=b

a1=account(101,1000)
a2=account(102,2000)

print(a1.acn,a1.bal,a1.ifsc)
print(a2.bal,a2.bal,a2.ifsc)

#chnges in members
a1.bal=a1.bal+500#instance data members changed
a2.bal=a2.bal+500

account.ifsc='123abc'#class data member chnged

print(a1.acn,a1.bal,a1.ifsc)
print(a2.bal,a2.bal,a2.ifsc)





