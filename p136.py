#HYbrid Inheritance
class A:
    def m1(self):
        print("this is m1")
class B(A):
    def m2(self):
        print("this is m2")
class C:
    def m3(self):
        print("This is m3")
class D(B,C):
    def m4(self):
        print("this is m4")
        
obj=D()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
