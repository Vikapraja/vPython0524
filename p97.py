import math
a=math.sqrt(16)#returns sqrt of given num
print(a)
#or
print(math.sqrt(36))

print(math.gcd(20,30)) #returns greatest common divisor
print(math.factorial(5))#returns factorial of given num
print(math.cbrt(64))#returns cube root of given num
print(math.cos(0))#returns cosine of given angle

import random
print(random.randint(1000,9999))#returns random int in given range
print(random.choice([1,2,3,4,5,6]))#returns a random value from the given list
li=[1,2,3,4,5]
random.shuffle(li)#make the list unorder
print(li)

import time
print(time.ctime())#returns current date/time of system
print(time.strftime("%d-%m-%Y"))#returns formated date
print(time.strftime("%r"))
print(time.strftime("%d %A %b,%Y"))


#date directives-> %d %m %Y
#%d--->date
#%m--->month
#%y--->year in 2 digit
#%Y--->year in 4 digit
#%r--->Time in 12 hrs with AM/PM
#%A--->day name
#etc


#time.sleep(secs)-->suspend execution till given time
for i in range(1,11):
    print(i)
    time.sleep(.5)














