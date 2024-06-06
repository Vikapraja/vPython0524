#Operator Overloading
    #implememnting an operator to a datatype/class
    #for each operator there is a magic method and we need to implement this magic method in our class

        #exp:
            #mgic method for + ------> __add__(self,other)
            #magic method for * -----> __mul__(self,other)
            #etc.

#list of matchig methods

class test():
    def __add__(self,other):
        return 0

    def __mul__(self,other):
        return 1

t1=test()
t2=test()
t3=test()
print(t1+t2)
print(t1*t2)

class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __add__(self,other):
        return self.x+other.x,self.y+other.y
p1=point(3,5)
p2=point(5,5)
print(p1+p2)
p3=point(6,9)

print(p2+p3)

#print(p1+p2+p3) #error

class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        p=x+y
        return p

p1=point(3,5)
p2=point(5,5)
p3=point(3,5)
p4=point(5,5)
p5=p1+p2+p3+p4
print(p5)












        
