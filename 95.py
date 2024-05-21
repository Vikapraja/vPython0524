#syntax to import a module from package
    #import package.module as alias
    #from package import module as alias

import mypack.area as ar
print(ar.circle(4))
print(ar.rectangle(4,5))

from mypack import area as ar
print(ar.circle(10))
print(ar.rectangle(10,20))

import mypack.calculator as calc
print(calc.add(4,6))
print(calc.mul(4,5))
