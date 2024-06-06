#Inheritance
    #it is a technique to creating new class by reusing existing class code.
    #eisting class is known as Parent/Super/Base class and newly created class is known as child/Sub/Derived class.

#Types of Inheritance
    #Single level
    #Multi level
    #Mulptiple
    #Hybrid
    #Hierarchical

#Single level
class telephone:
    def makecall(self):
        print("This is makecall")

class mobile(telephone):
    def msg(self):
        print("this is msg")

obj=mobile()
obj.makecall()
obj.msg()        
    
