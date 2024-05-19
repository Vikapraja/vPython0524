#type of arguments
    #positional arguments
    #keyword args
    #Default args
    #Arbitary Positional args
    #Arbitary Keyword args

def show(a=0,b=1):  #Default args
    print(a,b)

show(10,20) #positional args
show(a=10,b=20) #keyword args
show(b=10,a=20) #keyword args

show(10)
show()
show(5,6)
show(50,b=60)
#show(a=50,60)   #error:we pass positional then keyword

#def a function to find a area of circle with defaut args
#call this 1st time using positional args
#call this 1st time using keyword args


def carea(r=1):
    pi=3.14
    a=pi*r**2
    print(a)

carea()#sefault agrs r=1
carea(2)#positional args
carea(3)#keyword args

def show(*a):   #arbitary lengt(0-N) positional args as tuple
    print(a)

show()
show(1,2)
show(1,2,3,4,5,6)

def show(**a):  #arbitary length(0-N) keyword args as dict
    print(a)
    
show(roll=1,name='sonu')
show(eid=102,esal=50000,dept='coddig')

#print(a)










