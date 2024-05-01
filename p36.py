#home work
    #F to C
    #Km to Mtr
    #Dollar to Inr
    #Age compute from birth year
#1)
f=float(input('Enter fahrenheit(for conver in celsius)='))
c=(f-32)*5/9
print('tempreture in c',round(c,2))

#2)
km=float(input('Enter km='))
m=km*1000
print('Meter',m)

#3)
d=float(input("Enter dollar's value="))
x=float(input("Enter no. of doller="))
inr=d*x
print('inr=',round(inr,2))

#4)
y=int(input('Enter Birth year='))
cy=int(input('Enter current year='))
age=cy-y
print(age)
