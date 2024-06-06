#Polymorephism(one name many forms)
    #Poly------------>Many
    #Morphism-------->forms/roles

#Polymorephism: It is the ability of an entity to play multiple roles according to situation.

    #There are 2 implementations of polymorphism in python:
        #method overriding
        #Operator overriding

#Method Overriding
    #Process of reimplementing method of patrent class in child class is known as method overriding.
    #super() can be used to access parent definition from child 
class A:
    def m1(self):
        print('m1 in A')
        
    def m2(self):
        print('m2 in A')

class B(A):
    def m1(self):
        print('m2 in B')
        super().m1()

obj=B()
obj.m1()
obj.m2()
    
