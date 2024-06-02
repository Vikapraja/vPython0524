#Method:
    #It is like a function defined inside a class
    #It is used to define a logic
#Types of Method:
    #Instance Method
        #define with self parameter
        #object is used for calling
    #Class Method
        #define with classmethod decorator(@classmethod)
        #class is used for calling
    #Static method
        #defined with staticmethod decorator(@staticmethod)
        #classname is used for calling

class test:
    def m1(self):   #instance method
        print("This is m1")

    @classmethod    #class method decorator(@->decorator)
    def m2(cls):
        print("This is m2")

    @staticmethod   #static method  [it no need argumnt ferther can given]
    def m3():
        print("this is m3")


t=test()
t.m1()  #by interpreter t.m1(t)

t.m2()
t.m3()

test.m2()   #by interpreter test.m2(test)
test.m3()   #by interpreter test.m3()
