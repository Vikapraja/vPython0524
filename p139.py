#Nested Class
    #A class is said to be nested if it is defined inside block of other class.
    #Generally we defined nested class to create dependancy on It's outer class.
    #exp:
        #Brain can not exist without human
        #Humen will be outer and Brain will be nested

class A:    #outer/top level class
    def show(self):
        print('this is show')

    class B:
        def disp(self): #nested/inner class
            print('this is disp')

obj=A()
obj.show()

obj=A.B()
obj.disp()
