def area(r):
    pi=3.14
    area=pi*r**2
    print(area)

area(2.5)
area(4)

def avg(m1,m2,m3): #m1,m2,m3 parameters
    a=(m1+m2+m3)/3
    print(a)

avg(1,2,3)#1,2,3 are arguments 

#define a function to simple interest.


def sinterest(p,r,t):
    s=(p*r*t)/100
    print('interest=',s)

sinterest(2,3,4)

#define a function to check even/odd of a no.

def evdd(a):
    if a%2==0:
        print('even')
    else:
        print('odd')

evdd(4)
evdd(5)


