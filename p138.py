#key point about inheritance
    #1) object class(library) is the default parent for all python class. Object class contains morethan 20 methods.

help(object)

    #2) In case of multiple inheritance ,there may be a chance of method-ambiguity (same method in differant classes), MRO(Method Resolution Order) is
    #used to solve this ambiguity.

class A:
    def m1(self):
        print("this is m1 in A")

class B:
    def m1(self):
        print('this is m1 in B')

class C(A,B):
    def m2(self):
        print('this is m2 in C')

obj=C()
obj.m1()
obj.m2()

class C(B,A):
    def m2(self):
        print('this is m2 in C')

obj=C()
obj.m1()
obj.m2()
